import os, re, sys
from copy import deepcopy
from pyparsing import ParseResults

from procgraph.core.exceptions import SemanticError, \
    x_not_found, aslist
from procgraph.core.block import Block
from procgraph.core.parsing_elements import ParsedSignalList, VariableReference, \
     ParsedBlock, ParsedModel, ParsedSignal
from procgraph.core.registrar import default_library
from procgraph.core.model import Model
from procgraph.core.visualization import semantic_warning

from procgraph.core.visualization import debug as debug_main



def check_link_compatibility_input(previous_block, previous_link):
    assert isinstance(previous_link, ParsedSignalList)
    # If the previous block did not define output signals
    if not previous_block.are_output_signals_defined():
        # We define a bunch of anonymous signals
        n = len(previous_link.signals)
        previous_block.define_output_signals(map(str, range(n)))

    # We check that we have good matches for the previous                    
    for i, s in enumerate(previous_link.signals):
        assert isinstance(s, ParsedSignal)
        if s.block_name is not None:
            raise SemanticError('Could not give a block name between two blocks.')
        if s.local_input is None:
            s.local_input = i
                    
        if not previous_block.is_valid_output_name(s.local_input):
            raise SemanticError('Could not find output name "%s"(%s) in %s' % \
                            (s.local_input, type(s.local_input), previous_block))
            
        s.local_input = previous_block.canonicalize_output(s.local_input)

def check_link_compatibility_output(block, previous_link):
    assert isinstance(previous_link, ParsedSignalList)
    # if the block did not define input signals
    if not block.are_input_signals_defined():
        # We define a bunch of anonymous signals
        n = len(previous_link.signals)
        names = []
        for i in range(n):
            if previous_link.signals[i].local_output is not None:
                name = previous_link.signals[i].local_output
            elif previous_link.signals[i].name is not None:
                name = previous_link.signals[i].name
            else:
                # XXX I'm not sure we should be here, at least name should be 
                # defined
                assert(False)
                #name = str(i)
            names.append(name)
        
        block.define_input_signals(names)
    
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



def create_from_parsing_results(parsed_model, name=None, config={}, library=None,
                                STRICT=False):
    
    def debug(s):
        if False:
            debug_main('Creating %s:%s | %s' % (name, parsed_model.name, s))

    
    #debug_main('config: %s' % config)
    
    if library is None:
        library = default_library
    if not isinstance(parsed_model, ParsedModel):
        raise TypeError('I expect a ParsedModel instance, not a "%s".' % 
                        parsed_model.__class__.__name__)
        
    model = Model(name=name, model_name=parsed_model.name, config=config)
    
    # First we get the names of the config variables.
    # In the mean time we check that we don't have doubles.
    config_variables = set()
    config_variables_required = set()
    for config_statement in parsed_model.config:
        variable = config_statement.variable
        if variable in config_variables:
            raise SemanticError(
            'Config variable "%s" already defined.' % variable, config_statement)
        config_variables.add(variable)
        if not config_statement.has_default:
            config_variables_required.add(variable)
            
    # We start by checking that we got passed the correct configuration.
    # First we check that we were only passed config formally defined. 
    #  (This is only a warning if we are not in strict mode.)
    # Also note that we treat the "block.variable" refs in another way.
    passed_variables = set([x for x in config.keys() if not '.' in x])
    passed_not_defined = passed_variables.difference(config_variables) 
    if passed_not_defined:
        msg = ('We were passed config (%s) which was not defined formally ' + \
        'as a config variable. The defined ones are %s.') % (\
                aslist(passed_not_defined), aslist(config_variables))
        if STRICT:
            raise SemanticError(msg, parsed_model)
        else:
            semantic_warning(msg, parsed_model)
         
    # Then we check that we passed all variables that we needed to pass
    required_not_passed = config_variables_required.difference(passed_variables)
    if required_not_passed:
        msg = ('Some required config (%s) was not passed.' % \
               aslist(required_not_passed))
        raise SemanticError(msg, parsed_model)
    
    
    # We collect here all the properties, to use in initialization.
    all_config = [] # tuple (key, value, element)
    
    # 1. We put the configuration defaults
    for c in parsed_model.config:
        if c.has_default:
            all_config.append((c.variable, c.default, c))

    # 2. We put the user-passed values
    for key, value in config.items():
        all_config.append((key, value, None))

    # 3. We process the assignments
    for assignment in parsed_model.assignments:
        # We make sure we are not overwriting configuration    
        if assignment.key in config_variables:
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
 
        
    def expand_value(value, context=None, element=None):
        ''' Function that looks for VariableReference and does the substitution. '''
        if context is None:
            context = []
        # there's no recursion now...
        #    if value in context:
        #        raise SemanticError('Recursion warning: context = %s, value = "%s".' %\
        #                            context, value)
        context.append(value)
        
        if isinstance(value, VariableReference):
            variable = value.variable
            if variable in os.environ:
                return os.environ[variable]
            if not variable in properties:
                raise SemanticError(
                    x_not_found('variable', variable, properties), element)
            used_properties.add(variable) 
            return expand_value(properties[variable], context, element=element)
        
        elif isinstance(value, str):
            return expand_references_in_string(value,
                    lambda s: expand_value(VariableReference(s),
                                           context=context, element=element))
            
        elif isinstance(value, dict):
            h = {}
            for key in value:
                h[key] = expand_value(value[key], context=context, element=element)
            return h 
        
        # XXX: we shouldn't have here ParseResults
        elif isinstance(value, list) or isinstance(value, ParseResults):
            return map(lambda s: expand_value(s, context, element), value)
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
            debug_main("Importing package %s" % package)
            try:
                __import__(package)
            except Exception as e:
                raise SemanticError('Could not import package "%s": %s' % \
                                        (package, e), element=x)
    
    # Extract load and save statements
    for x in parsed_model.load_statements:
        where_from = expand_value(x.where_from, element=element)
        model.add_load_action(what=x.what, where=where_from,
                              format=x.format, element=element)
        
    for x in parsed_model.save_statements:
        where_to = expand_value(x.where_to, element=element)
        model.add_save_action(what=x.what, where=where_to,
                              format=x.format, element=element)
    
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
                    # This is the last one, we should process it with the previous_block
                    previous_link = element
                    check_link_compatibility_input(previous_block, previous_link)

                    for s in (previous_link.signals):
                        # We cannot have a local output
                        if s.local_output is not None:
                            raise SemanticError(('Terminator connection %s ' + 
                                'cannot have a local output') % s, element=previous_link)  
                        
                        model.connect(block1=previous_block, block1_signal=s.local_input,
                                             block2=None, block2_signal=None, public_name=s.name)
             
                
            if isinstance(element, ParsedBlock):
                
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
                    # now, it might be that el
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
                    raise SemanticError(x_not_found('block type', block_type, library.get_known_blocks()),
                                        element=element)
                debug('instancing %s:%s config: %s' % \
                      (element.name, element.operation, block_config))
                
    
                block = library.instance(block_type=block_type,
                                         name=element.name, config=block_config,
                                         where=element.where)
                
                block = model.add_block(name=element.name, block=block)
                
                # print "Defined block %s = %s " % (element.name , block)
                
                if (previous_block is not None) and (previous_link is not None):
                    # normal connection between two blocks with named signals
                    
                    # Here we have to make sure that, if the blocks defined
                    #  signals input/outputs, then the signals given by the user
                    #  are coherent.
                    # If, instead, the blocks did not define signals, then
                    #  we define it later.
                    
                    check_link_compatibility_input(previous_block, previous_link)
                    check_link_compatibility_output(block, previous_link)
            
                    # Finally we create the connection
                    for s in (previous_link.signals):
                        model.connect(previous_block, s.local_input,
                                             block, s.local_output, s.name)
                        
                elif previous_block is not None and previous_link is None:
                    # anonymous connection between two blocks
                    # if the previous block has already defined the output
                    # AND we didn't define the input, then we copy that
                    if previous_block.are_output_signals_defined() \
                        and not block.are_input_signals_defined():
                        names = previous_block.get_output_signals_names()
                        
                        block.define_input_signals(names)
                        # just create default connections
                        for i in range(len(names)):
                            name = 'link_%s_to_%s_%d' % \
                                (previous_block.name, block.name, i)
                            model.connect(previous_block, i,
                                             block, i, name)
                    # If both have defined, we check they have the same
                    # number of signals
                    elif  previous_block.are_output_signals_defined() \
                        and block.are_input_signals_defined():
                        # check that they have the same number of signals
                        num_out = previous_block.num_output_signals()
                        num_in = block.num_input_signals()
                        if num_out != num_in:
                            raise SemanticError('Tried to connect two blocks (%s \
and %s) with incompatible signals; you must do this expliciyl.' % (previous_block, block),
element=block)
                        if num_out == 0:
                            raise SemanticError('Tried to connect two blocks (%s, %s) w/no signals.'\
                                            % (previous_block, block),
                                            element=block)
                            
                        # just create default connections
                        for i in range(num_out):
                            name = 'link_%s_to_%s_%d' % \
                                (previous_block.name, block.name, i)
                            model.connect(previous_block, i,
                                             block, i, name)
                        
                
                    else:
                        # we cannot say anything before updat()ing the blocks
                        # so we remember to do it later
                        model.unresolved[previous_block] = block
                
                elif previous_block is None and previous_link is not None:
                    # this is the first block with previous signals
                    # For the output we can do as before
                    check_link_compatibility_output(block, previous_link)
                    
                    # However, this time we need to be careful, because
                    # links can refer to other parts
                    for s in (previous_link.signals):
                        # Cannot use local_input here
                        if s.local_input is not None:
                            raise SemanticError('Link %s cannot use local input without antecedent. ' % \
                                            s, element=previous_link)
                        # Check if it is using an explicit block name
                        if s.block_name is not None:
                            if not s.block_name in model.name2block:
                                raise SemanticError('Link %s refers to unknown block "%s". We know %s.' % 
                                                (s, s.block_name, ", ".join(model.name2block.keys())),
                                                element=previous_link)
                            input_block = model.name2block[s.block_name]
                            if not input_block.is_valid_output_name(s.name):
                                raise SemanticError('Link %s refers to unknown output %s in block %s. ' % 
                                                (s, s.name, input_block),
                                                element=previous_link)
                            s.local_input = input_block.canonicalize_output(s.name)
                        else:
                            if not s.name in model.name2block_connection:
                                raise SemanticError('Link %s refers to unknown signal "%s". We know %s.' % \
                                                (s, s.name, ", ".join(model.name2block_connection.keys())),
                                                element=previous_link)
                            defined_signal = model.name2block_connection[s.name]
                            input_block = defined_signal.block1
                            s.local_input = defined_signal.block1_signal
                            
                        # make up a name    
                        name = "input_%s_for_%s" % (s.local_output, block)
                        model.connect(input_block, s.local_input,
                                             block, s.local_output, name)
                        
                
                elif previous_block is None and previous_link is None:
                    # make sure it's a generator?
                    if not block.are_input_signals_defined():
                        raise SemanticError('The block %s did not define signals and it has no input.' % 
                                       block, element=block) 
                    if block.num_input_signals() > 0:
                        raise SemanticError('The generator block %s should have defined 0 inputs.' % 
                                        block, element=block) 
                
                # at this point the input should be defined
                assert block.are_input_signals_defined()
                # if it did not define outputs (init delayed)
                if not block.are_output_signals_defined():
                    # then we call init() again
                    res = block.init()
                    # it cannot return NOT_FINISHED again.
                    if res == Block.INIT_NOT_FINISHED:
                        raise SemanticError('Block %s cannot return NOT_FINISHED ' + 
                                        'after inputs have been defined. ' % block,
                                        element=block)
                    # now the outputs should be defined
                    if not block.are_output_signals_defined():
                        raise SemanticError(('Block %s still does not define outputs' + 
                                        ' after init() called twice. ') % block,
                                        element=block)
                
                # at this point input/output should be defined
                assert block.are_input_signals_defined()
                assert block.are_output_signals_defined()

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
