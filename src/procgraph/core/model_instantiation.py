import os, re, sys
from copy import deepcopy
from pyparsing import ParseResults

from .exceptions import SemanticError, x_not_found, aslist
from .registrar import default_library
from .model import Model
from .visualization import semantic_warning
from .parsing_elements import ParsedSignalList, VariableReference, \
     ParsedBlock, ParsedModel, ParsedSignal

from .visualization import debug as debug_main
from .block_config import resolve_config
from .block_meta import VARIABLE, DEFINED_AT_RUNTIME
from .model_io import ModelInput
from procgraph.core.visualization import info


def check_link_compatibility_input(previous_block, previous_link):
    assert isinstance(previous_link, ParsedSignalList)
    
    num_required = len(previous_link.signals)
    num_found = previous_block.num_output_signals()
    
    if num_required > num_found:
        raise SemanticError('Required %s, found only %s.' % 
                            (num_required, num_found), previous_link)
    # XXX, still something not quite right
    
    # We check that we have good matches for the previous                    
    for i, s in enumerate(previous_link.signals):
        assert isinstance(s, ParsedSignal)
        if s.block_name is not None:
            raise SemanticError('Could not give a block name when the '
                                ' conection is between two blocks.',
                                previous_link)
        if s.local_input is None:
            s.local_input = i
                    
        if not previous_block.is_valid_output_name(s.local_input):
            raise SemanticError('Could not find output name "%s"(%s) in %s' % \
                        (s.local_input, type(s.local_input), previous_block))
            
        s.local_input = previous_block.canonicalize_output(s.local_input)

def check_link_compatibility_output(block, previous_link):
    assert isinstance(previous_link, ParsedSignalList)
    
    # we check that we have good matches for the next    
    for i, s in enumerate(previous_link.signals):
        assert isinstance(s, ParsedSignal)
        
        if s.local_output is  None:
            s.local_output = i
                    
        if not block.is_valid_input_name(s.local_output):
            raise SemanticError('Could not find input name "%s" in %s' % \
                            (s.local_output, block))
            
        s.local_output = block.canonicalize_input(s.local_output)
 
def expand_references_in_string(s, function):
    ''' Expands references of the kind ${var} in the string s.
        ``function``(var) translates from var -> value '''
    while True:
        m = re.match('(.*)\$\{(\w+)\}(.*)', s)
        if not m:
            return s
        before = m.group(1)
        var = m.group(2)
        after = m.group(3)
        sub = function(var)
        s = before + sub + after



def create_from_parsing_results(parsed_model, name=None, config={},
                                library=None, STRICT=False):
    
    def debug(s):
        if False:
            debug_main('Creating %s:%s | %s' % (name, parsed_model.name, s))
    
    #debug_main('config: %s' % config)
    
    if library is None:
        library = default_library
    if not isinstance(parsed_model, ParsedModel):
        raise TypeError('I expect a ParsedModel instance, not a "%s".' % 
                        parsed_model.__class__.__name__)
        
    model = Model(name=name, model_name=parsed_model.name)
    model.define_input_signals_new(map(lambda x: x.name, parsed_model.input))
    model.define_output_signals_new(map(lambda x: x.name, parsed_model.output))
    
    
    # first we divide the config in normal, and recursive config
    normal_config = {}
    recursive_config = {}
    for key, value in config.items():
        if '.' in key:
            recursive_config[key] = value
        else:
            normal_config[key] = value
    
    # We mix the normal config with the defaults
    # FIXME: None -> no where information
    resolved = resolve_config(parsed_model.config, normal_config, None) 
    # we give none so that it can be filled in by the caller
    
    # Remember config statement
    key2element = {}
    for c in parsed_model.config:
        key2element[c.variable] = c
         
    # We collect here all the properties, to use in initialization.
    all_config = [] # tuple (key, value, parsing_element)
    
    # 1. We put the resolved configuration 
    for key, value in resolved.items():
        all_config.append((key, value, key2element.get(key, None)))

    # 2. We also put the recursive conf
    for key, value in recursive_config.items():
        all_config.append((key, value, key2element.get(key, None)))

    # 3. We process the assignments
    for assignment in parsed_model.assignments:
        # We make sure we are not overwriting configuration    
        if assignment.key in resolved:
            msg = ('Assignment to "%s" overwrites a config variable.' + \
                  ' Perhaps you want to change the default instead?') % \
                    assignment.key
            raise SemanticError(msg, assignment)

        all_config.append((assignment.key, assignment.value, assignment))

    
    # Next, define the properties hash, and populate it intelligentily
    # from the tuples in all_config.
    properties = {}
    # We keep track of what properties we use
    used_properties = set() # of strings
 
        
    def expand_value(value, element=None):
        ''' Function that looks for VariableReference and does the 
            substitution. 
        '''
        #if context is None:
        #    context = []
        # there's no recursion now...
        #    if value in context:
        #context.append(value)
        
        if isinstance(value, VariableReference):
            variable = value.variable
            if variable in os.environ:
                return os.environ[variable]
            if not variable in properties:
                raise SemanticError(
                    x_not_found('variable', variable, properties), element)
            used_properties.add(variable) 
            return expand_value(properties[variable], element=element)
        
        elif isinstance(value, str):
            return expand_references_in_string(value,
                    lambda s: expand_value(VariableReference(s),
                                           element=element))
            
        elif isinstance(value, dict):
            h = {}
            for key in value:
                h[key] = expand_value(value[key], element=element)
            return h 
        
        # XXX: we shouldn't have here ParseResults
        elif isinstance(value, list) or isinstance(value, ParseResults):
            return map(lambda s: expand_value(s, element), value)
        else:
            return value

    # We keep track of the blocks we reference so we can check it later
    referenced_blocks = [] # list of tuples (block name, parsed_element)
    for key, value, element in all_config:
        # if it is of the form  object.property = value
        if '.' in key:
            # TODO: put this in syntax
            object, property = key.split('.', 1)
            if not object in properties:
                properties[object] = {}
            else:    
                # XXX probably should be better
                if not isinstance(properties[object], dict):
                    raise SemanticError(
                    'Error while processing "%s=%s". I already now key.' % \
                            (key, value), element)
            referenced_blocks.append((object, element))
            properties[object][property] = value # XX or expand?
        else:
            properties[key] = expand_value(value, element=element) 
        pass  
    
    for x in parsed_model.imports:
        package = x.package
        if not package in sys.modules:
            info("Importing package %r..." % package)
            try:
                __import__(package)
            except Exception as e:
                raise SemanticError('Could not import package "%s": %s' % \
                                        (package, e), element=x)
    
     
    # Then we instantiate all the blocks
   
    # Iterate over connections 
    for connection in parsed_model.connections:
        previous_block = None
        previous_link = None
        
        # print "Looking at connection %s" % connection.elements
        for i, element in enumerate(connection.elements):
            if isinstance(element, ParsedSignalList):
                # We make a copy, because later we modify (for convenience)
                # its fields, in the check_compatibility_* functions
                # For example, we assign names to input/output.
                element = deepcopy(element)
                
                # if this is not the last one, just save it, it will be
                # processed together with the next block
                if i != len(connection.elements) - 1: 
                    previous_link = element
                else:
                    assert previous_block is not None
                    # This is the last one, we should process it with the 
                    # previous_block
                    previous_link = element
                    check_link_compatibility_input(previous_block,
                                                   previous_link)

                    for s in (previous_link.signals):
                        # We cannot have a local output
                        if s.local_output is not None:
                            raise SemanticError(('Terminator connection %s ' + 
                                'cannot have a local output') % s, element=s)  
             
                        if s.name in model.public_signal_names():           
                            msg = ('Public signal name %r already taken.' % 
                                   s.name)
                            raise SemanticError(msg, element=s)
                        
                        model.connect(block1=previous_block,
                                      block1_signal=s.local_input,
                                      block2=None, block2_signal=None,
                                      public_name=s.name)
             
                
            if isinstance(element, ParsedBlock):
                
                # before processing this block, let's create a phantom
                # signal list
                if previous_block is not None and previous_link is None:
                    previous_link = fill_anonymous_link(previous_block)

                # also we can check right now a common error
                if (previous_block is not None and 
                    previous_block.num_output_signals() == 0):
                    msg = 'This block does not define outputs yet it is not ' \
                          'the last in the sequence.'
                    raise SemanticError(msg, previous_block)
                
                block_type = expand_value(element.operation, element=element)

                # give a name if anonymous
                if element.name is None:
                    # give it, if possible the name of its type
                    if not  block_type in model.name2block:
                        element.name = block_type
                    else:
                        i = 2
                        while True:
                            element.name = "%s%d" % (block_type, i)
                            i += 1
                            if not element.name in model.name2block:
                                break

                # update the configuration if given
                block_config = {}
                block_config.update(element.config)
                if element.name in properties:
                    more_config_for_block = properties[element.name] 
                    # For example:
                    #   wait = 10       ->  { wait: 10 }
                    #   wait.time  = 3  ->  { wait: {time: 3} }
                    if isinstance(more_config_for_block, dict):
                        block_config.update(more_config_for_block)
                        # delete so we can keep track of unused properties
                        used_properties.add(element.name)
                
                for key, value in list(block_config.items()):
                    block_config[key] = expand_value(value, element=element)
                    

                
                if not library.exists(block_type):
                    raise SemanticError(x_not_found('block type', block_type,
                                                    library.get_known_blocks()),
                                        element=element)
                debug('instancing %s:%s config: %s' % \
                      (element.name, element.operation, block_config))
                
                try:
                    block = library.instance(block_type=block_type,
                                         name=element.name, config=block_config)
                    block.where = element.where
                except SemanticError as e:
                    # For config (see FIXME)
                    if e.element is None:
                        e.element = element
                    raise
                        
                
                # now define input and output
                generator = library.get_generator_for_block_type(block_type)
                
                define_input_signals(generator.input, block,
                                     previous_link, previous_block, model)
                define_output_signals(generator.output, block)
                
                # at this point input/output should be defined
                assert block.are_input_signals_defined()
                assert block.are_output_signals_defined()

                block.init()
                
                
                # first init(), then add because of ModelInput/Output
                block = model.add_block(name=element.name, block=block)
                
                
                previous_link = None                    
                previous_block = block
            # end if 
    
    
    # Check if any of the config referenced a nonexistent block
    # (before we warn it as just an unused variable in the next paragraph) 
    for block_name, element in referenced_blocks:
        if not block_name in model.name2block:
            raise SemanticError(
                x_not_found('block', block_name, model.name2block), element)
    
    unused_properties = set(properties.keys()).difference(used_properties)
    if unused_properties:
        msg = 'Unused properties: %s. (Used: %s.)' % \
            (aslist(unused_properties), aslist(used_properties)) 
        if STRICT:
            raise SemanticError(msg, element=parsed_model)
        else:
            semantic_warning(msg, parsed_model)
    
        
    # Process load statements
    model.init()
    
    return model

def define_output_signals(output, block):
    # this is a special case, in which the signal name
    # is not known before parsing the configuration
    if isinstance(block, ModelInput):
        block.define_output_signals_new([block.config.name])
        return

    output_is_defined_at_runtime = len(output) == 1 and \
                                   output[0].type == DEFINED_AT_RUNTIME
    
    if output_is_defined_at_runtime:
        names = block.get_output_signals()
        block.define_output_signals_new(names)
        return         
                        
    output_is_variable = len(output) == 1 and output[0].type == VARIABLE
        
    if output_is_variable:
        # define output signals with the same name as the input signals
        names = block.get_input_signals_names()
        # TODO: maybe add a suffix someday
        names = map(lambda x: x, names)
        
        block.define_output_signals_new(names)
        
    else:
        # simply define the output signals
        names = map(lambda x:x.name, output)                        
        block.define_output_signals_new(names)


def define_input_signals(input, block, previous_link, previous_block, model):
    # there are two cases: either we define named signals,
    # or we have a generic number of signals
    input_is_arbitrary = len(input) == 1 and input[0].type == VARIABLE 
         
    if input_is_arbitrary:
        # in this case, we have a minimum and maximum 
        # number of signals that we can accept
        min_expected = input[0].min
        max_expected = input[0].max
        
        if not min_expected:
            min_expected = 0
        if not max_expected:
            max_expected = 10000
        
        # if we don't have a previous block, then
        # we just define no input signals
        # (if we expect something, then we throw an error)
        if previous_link is None:
            if min_expected > 0:
                msg = 'I expected at least %d input signals' \
                      ' but the block is not connected to anything.'
                raise SemanticError(msg, block)
            else:
                # no inputs for this block
                block.define_input_signals_new([])
        else:
            # We have a previous link, we check that the number
            # of signals is compatible.
            num_given = len(previous_link.signals)
            ok = (min_expected <= num_given <= max_expected)
            if not ok:
                msg = 'I expected between %d and %d input signals, '\
                      'and I got %d.' % (min_expected, max_expected,
                                         num_given)
                raise SemanticError(msg, block)
            # Define input signals given the names
            names = []
            for i in range(num_given):
                # --> [local_input] name [local_output] -->    
                if previous_link.signals[i].local_output is not None:
                    name = previous_link.signals[i].local_output
                elif previous_link.signals[i].name is not None:
                    name = previous_link.signals[i].name
                elif previous_link.signals[i].local_input is not None:
                    name = previous_link.signals[i].local_input
                else:
                    print previous_link.signals[i]
                    assert False
                names.append(name)
            block.define_input_signals_new(names)
    else: # the input is not arbitrary
        # define right away the names, it does not depend 
        # on anything else
        names = map(lambda x:x.name, input)                        
        block.define_input_signals_new(names)

        # now check we were given the right input
        num_expected = len(names)
        
        # if we expect something and it is not given,
        # raise an exception
        if previous_link is None:
            if (num_expected > 0):
                msg = 'The block expected at least %d input signals'\
                  ' but none were given.' % num_expected
                raise SemanticError(msg, block)
        else: 
            # we have a previous block, the number of signals
            # should match
            num_given = len(previous_link.signals)
            
            if num_expected != num_given:
                msg = 'The block expected %d input signals, got %d.' % \
                      (num_expected, num_given)
                raise SemanticError(msg, block)
    

    # print "Defined block %s = %s " % (element.name , block)
    if previous_link is not None:
        check_link_compatibility_output(block, previous_link)

        if previous_block is not None: 
            # normal connection between two blocks with named signals
            
            # Here we have to make sure that, if the blocks defined
            #  signals input/outputs, then the signals given by the user
            #  are coherent.
            
            check_link_compatibility_input(previous_block, previous_link)
    
            # Finally we create the connection
            for s in (previous_link.signals):
                if s.name is None:
                    s.name = "input_%s_for_%s" % (s.local_output, block)

                model.connect(previous_block, s.local_input,
                                     block, s.local_output, s.name)
        else: 
            # this is the first block with previous signals
            # this time we need to be careful, because
            # links can refer to other parts
            for s in previous_link.signals:
                # Cannot use local_input here
                if s.local_input is not None:
                    raise SemanticError('Link %s cannot use local input ' 
                                        ' without antecedent. ' % s, s)
                # Check if it is using an explicit block name
                if s.block_name is not None:
                    if not s.block_name in model.name2block:
                        raise SemanticError(
                        'Link %s refers to unknown block %r; we know %s.' % 
                        (s, s.block_name, aslist(model.name2block.keys())), s)
                        
                    input_block = model.name2block[s.block_name]
                    if not input_block.is_valid_output_name(s.name):
                        # TODO: make other friendly messages like this
                        msg = ("A link refers to an unknown output %r.\n" % 
                               s.name)
                        msg += ("The known outputs are: %s.\n" % 
                                input_block.get_output_signals_names()) 
                        msg += "  link: %s \n" % s
                        msg += " block: %s \n" % input_block  
                        raise SemanticError(msg, element=s)
                    s.local_input = input_block.canonicalize_output(s.name)
                else:
                    if not s.name in model.name2block_connection:
                        msg = 'Link %s refers to unknown signal %r. ' \
                              ' We know %s.' % (s, s.name,
                                    aslist(model.name2block_connection.keys()))
                        raise SemanticError(msg, element=s)
                    defined_signal = model.name2block_connection[s.name]
                    input_block = defined_signal.block1
                    s.local_input = defined_signal.block1_signal
                    
                # make up a name    
                name = "input_%s_for_%s" % (s.local_output, block)
                model.connect(input_block, s.local_input,
                                     block, s.local_output, name)


def fill_anonymous_link(previous_block):
    # --> [local_input] name [local_output] -->
    names = previous_block.get_output_signals_names()
    signals = []
    for name in names:
        signal = ParsedSignal(name=None, block_name=None,
                              local_input=name,
                              local_output=None)
        signals.append(signal)
    return ParsedSignalList(signals)
