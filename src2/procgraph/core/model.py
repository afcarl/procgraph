from procgraph.core.block import Block
from procgraph.core.parsing import ParsedAssignment, Connection, ParsedBlock,\
    ParsedSignalList, ParsedSignal, parse_model, ParsedModel, VariableReference

from procgraph.components import *
from procgraph.core.exceptions import  SemanticError, BlockWriterError,\
    ModelExecutionError


class BlockConnection:
    def __init__(self, block1, block1_signal, block2, block2_signal, public_name=None ):
        assert isinstance( block1, Block)
        assert block1_signal is not None
        assert block2 is None or isinstance( block2, Block)
        
        self.block1 = block1
        self.block1_signal = block1_signal
        self.block2 = block2
        self.block2_signal = block2_signal
        self.public_name = public_name
        
    def __repr__(self):
        s = 'Connection('
        if self.block1:
            s += self.block1.name
            s += '.%s' %self.block1_signal 
        else:
            s += '?.?'
        
        s += ' --> '
        if self.block2:
            s += self.block2.name
            s += '.%s' %self.block2_signal 
        else:
            s += '?.?'
        s+=')'
            
        return s
    
    
class Model(Block):
    ''' A Model is a block. '''
    
    def __init__(self, name, model_name):
        ''' Name is the personal name of this instance.
            model_name is this model's name '''
        if name is None:
            name = 'unnamed-block'
        
        if model_name is None:
            model_name = 'unnamed-model'
        
        self.model_name = model_name
    
        # As a block
        Block.__init__(self, name=name, config={}, library=None)
    
        
        # we start with no input/output signals
        self.define_input_signals([])
        self.define_output_signals([])
            
    
        self.name2block = {}
        self.name2block_connection = {}
        # block -> block unresolved 
        self.unresolved = {}
        
        # list of blocks that act as generators (instance of Generator)
        self.generators = []
        
        self.reset_execution()
        
        # hash signal name -> Block for blocks of type ModelInput
        self.model_input_ports = {} 
        
    def summary(self):
        print "--- Model: %d blocks, %d connections" % \
            (len(self.name2block),len(self.name2block_connection))
        for name, block in self.name2block.items():
            print "- %s: %s" % (name, block)
            
        for name, conn in self.name2block_connection.items():
            print "- %s: %s" % (name, conn) 
 
 
    def add_block(self, name, block):
        '''  init(), and add a block to the model.
            Returns the block instance. '''
        
        res = block.init()
        # add it to the list if initialization is not complete
        if res != Block.INIT_NOT_FINISHED:
            if not self.are_input_signals_defined() or \
                not self.are_output_signals_defined():
                raise BlockWriterError(('Block %s did not define input/output signals' + 
                                ' and did not return INIT_NOT_FINISHED') %
                                block) 
         
        
        
        self.name2block[name] = block
        if isinstance(block, Generator):
            self.generators.append(block)
            
        if isinstance(block, ModelInput):
            self.model_input_ports[block.signal_name] = block
            self.define_input_signals(self.get_input_signals_names() + 
                                      [block.signal_name])
        
        if isinstance(block, ModelOutput):
            # XXX bug: output_signals -> output_signals
            self.define_output_signals(self.get_output_signals_names() + 
                                       [block.signal_name])
        
        return block
    
    def from_outside_set_input(self, num_or_id, value, timestamp):
        Block.from_outside_set_input(self, num_or_id, value, timestamp)
        
        signal_name = self.canonicalize_input(num_or_id)
        input_block = self.model_input_ports[signal_name]
        input_block.set_output(signal_name, value, timestamp)
        self.blocks_to_update.append(input_block)
    
    def connect(self, block1, block1_signal, block2, block2_signal, public_name):
        BC = BlockConnection( block1, block1_signal, block2, block2_signal, public_name=None)
        if public_name in self.name2block_connection:
            raise SemanticError('Signal "%s" already defined. ' % public_name)
        self.name2block_connection[public_name] = BC

    def has_more(self):
        if self.blocks_to_update:
            return True
        
        for generator in self.generators:
            (has_next, timestamp) = generator.next_data_status() #@UnusedVariable
            if has_next:
                return True
            
        return False
    
    def reset_execution(self):
        self.blocks_to_update = []
        # FIXME XXX it's late
        # add all the blocks without input to the update list
        for block in self.name2block.values():
            if not isinstance(block, ModelInput) and \
                block.num_input_signals()==0:
                self.blocks_to_update.append(block)
            if isinstance(block, Model):
                block.reset_execution()
    
    def update(self):
        def debug(s):
            if False:
                print 'Model %s | %s' % (self.model_name, s)
        
        
        # We keep a list of blocks to be updated.
        # If the list is not empty, then pop one and update it.
        if self.blocks_to_update:
            # get one block
            block = self.blocks_to_update.pop(0)
            
            debug('Got block to update %s' % block)
            
        else:
            debug('No blocks to update')
            
            # look if we have any generators
            # list of (generator, timestamp) 
            generators_with_timestamps = [] 
            for generator in self.generators:
                (has_next, timestamp) = generator.next_data_status()
                if has_next:
                    generators_with_timestamps.append((generator, timestamp))
        
            if not generators_with_timestamps:
                raise ModelExecutionError("You asked me to update but nothing's left.")
               
            # now look for the smallest available timestamp
            # (timestamp can be none)
            def cmp(timestamp1, timestamp2):
                if timestamp1 is None:
                    return 1
                elif timestamp2 is None:
                    return -1
                elif timestamp1 < timestamp2:
                    return -1
                elif timestamp2 < timestamp1:
                    return 1
                else:
                    return 0
                
            generators_with_timestamps.sort( key = lambda x:x[1], cmp=cmp)
            
            block =  generators_with_timestamps[0][0]
        
        if block is None:
            # We finished everything
            raise ModelExecutionError("You asked me to update but nothing's left.")
            
        # now we have a block (could be a generator)
        debug('Updating %s (input ts: %s)' % \
              (block, block.get_input_signals_timestamps()))
        result = block.update()
        # if the update is not finished, we put it back in the queue
        if result == block.UPDATE_NOT_FINISHED:
            self.blocks_to_update.insert(0, block)
        else:
            # the block updated, propagate
            
            debug("  processed %s, ts: %s" % (block, block.get_output_signals_timestamps()))
            debug("  its succesors: %s"% list(self.__get_output_connections(block)) )
            # check if the output signals were updated
            for connection in self.__get_output_connections(block):
                other = connection.block2
                if other is None:
                    # XXX don't include dummy connection
                    continue
                other_signal = connection.block2_signal
                old_timestamp = other.get_input_timestamp(other_signal)
                this_signal = connection.block1_signal
                this_timestamp = block.get_output_timestamp(this_signal)
                value  = block.get_output(this_signal)
                
                if value is not None and this_timestamp == 0:
                    raise ModelExecutionError('Strange, value is not none by timestamp is 0'+
                                    ' for signal %s of %s.' % (this_signal, block))
                
                # Two cases:
                # - timestamp is updated
                # NOOOOOOO - this is the first time
                #  WRONG think of the |wait| block
                if this_timestamp > old_timestamp: 
                # or \
                #    other.get_input(other_signal) is None:
                    #print "updating input %s of %s with timestamp %s" % \
                    #    (other_signal, other, this_timestamp)
                    
                    debug('  then waking up %s' % other) 
                    
                    other.from_outside_set_input(other_signal, value, 
                                                 this_timestamp)
                    
                    self.blocks_to_update.append(other)
                    
                    # If this is an output port, update the model
                    if isinstance(other, ModelOutput):
                        #print "Updating output %s" %  other.signal_name
                        self.set_output(other.signal_name, value, this_timestamp)
                else:
                    debug("  Not updated %s because not %s > %s" % \
                           (other, this_timestamp, old_timestamp) )
        
        # now let's see if we have still work to do
        # this step is important when the model is inside another one
        if self.blocks_to_update:
            # XXX should I count the generators here?
            return Block.UPDATE_NOT_FINISHED
        else:
            return True
            
    def __get_output_connections(self, block):
        for block_connection in self.name2block_connection.values():
            if block_connection.block1 == block:
                yield block_connection
    def __get_successors(self, block):
        ''' Returns an iterable of all the blocks connected
            to one of the outputs of the given block. '''
        successors = set()
        for block_connection in self.name2block_connection.values():
            if block_connection.block1 == block:
                successors.add(block_connection.block2)
        return successors
    
    
    def __repr__(self):
        s = 'M:%s:%s(' % (self.model_name,self.name)
        s += self.get_io_repr()
        s+= ')'
        return s
    
    

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
        block.define_input_signals(map(str, range(n)))
    
    # we check that we have good matches for the next    
    for i, s in enumerate(previous_link.signals):
        assert isinstance(s, ParsedSignal)
        
        if s.local_output is  None:
            s.local_output = i
                    
        if not block.is_valid_input_name(s.local_output):
            raise SemanticError('Could not find input name "%s" in %s' % \
                            (s.local_output, block) )
            
        s.local_output = block.canonicalize_input(s.local_output)
 
     
def create_from_parsing_results(parsed_model, name=None, config={}, library=None):
    def debug(s):
        if False:
            print 'Creating %s:%s | %s' % (name, parsed_model.name, s)
    
    debug('config: %s' % config)
    
    if library is None:
        library = default_library
    if not isinstance(parsed_model, ParsedModel):
        raise TypeError('I expect a ParsedModel instance, not a "%s".' % 
                        parsed_model.__class__.__name__)
    
    # print "\n\n --- new model ----------------"
    # print "Parsed: %s" % parsed_model
    
    model = Model(name=name, model_name=parsed_model.name)
    
    # First we collect all the properties, to use
    # in initialization.
    all_config = [] # tuple (key, value)
    # First put the ones in the model (act as default)
    for element in parsed_model.elements:
        if isinstance(element, ParsedAssignment):
            all_config.append((element.key, element.value))
    # now append the ones passed by configuration
    all_config.extend(config.items())
    
    # Next, define the properties hash, and populate it intelligentily
    # from the tuples in all_config.
    properties = {}
    # We keep track of what properties we use
    used_properties = set() # of strings
 
    def expand_value(value):
        if isinstance(value, VariableReference):
            variable = value.variable
            if not variable in properties:
                raise SemanticError('Could not evaluate %s. I know %s' %\
                                    (value, properties.keys()))
            used_properties.add(variable) 
            return expand_value(properties[variable])
        else:
            return value
        
    for key, value in all_config:
        # if it is of the form  object.property = value
        if '.' in key:
            # TODO: put this in syntax
            object, property = key.split('.', 1)
            if not object in properties:
                properties[object] = {}
            properties[object][property] = value
        else:
            properties[key] = expand_value(value) 
        pass  
    
    
    # Then we instantiate all the blocks
    connections = [x for x in parsed_model.elements if isinstance(x, Connection)]
    
    # Things for generating names for anonymous blocks
    num_anonymous_blocks = 0
    anonymous_name_pattern = 'block%d'
    
    # Iterate over connections 
    for connection in connections:
        previous_block = None
        previous_link = None
        
        # print "Looking at connection %s" % connection.elements
        for i, element in enumerate(connection.elements):
            if isinstance(element, ParsedSignalList):
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
                            raise SemanticError('Terminator connection %s cannot have a local output' %s)  
                        
                        model.connect(block1=previous_block, block1_signal=s.local_input,
                                             block2=None, block2_signal=None, public_name=s.name)
             
                
            if isinstance(element, ParsedBlock):
                
                # give a name if anonymous
                if element.name is None:
                    # give it, if possible the name of its type
                    if not element.operation in model.name2block:
                        element.name = element.operation
                    else:
                        element.name = anonymous_name_pattern % num_anonymous_blocks
                        num_anonymous_blocks += 1
                
                # update the configuration if given
                block_config = {}
                block_config.update(element.config)
                if element.name in properties:
                    block_config.update(properties[element.name])
                    # delete so we can keep track of unused properties
                    used_properties.add(element.name)
                
                for key, value in list(block_config.items()):
                    block_config[key] = expand_value(value)
                    
                
                if not library.exists(element.operation):
                    raise SemanticError('Uknown block type "%s". We know %s' % \
                                        (element.operation, library.get_known_blocks()))
                debug('instancing %s:%s config: %s' % \
                      (element.name,element.operation,block_config) )
                
                block = library.instance(block_type=element.operation, 
                                         name=element.name, config=block_config)
                
                block = model.add_block(name=element.name,block=block)
                
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
and %s) with incompatible signals; you must do this expliciyl.' % (previous_block, block))
                        if num_out == 0:
                            raise SemanticError('Tried to connect two blocks (%s, %s) w/no signals.'\
                                            % (previous_block, block))
                            
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
                            raise SemanticError('Link %s cannot use local input without antecedent. ' %\
                                            s)
                        # Check if it is using an explicit block name
                        if s.block_name is not None:
                            if not s.block_name in model.name2block:
                                raise SemanticError('Link %s refers to unknown block "%s". We know %s.' % 
                                                (s, s.block_name, model.name2block.keys()))
                            input_block = model.name2block[s.block_name]
                            if not input_block.is_valid_output_name(s.name):
                                raise SemanticError('Link %s refers to unknown output %s in block %s. ' % 
                                                (s, s.name, input_block))
                            s.local_input = input_block.canonicalize_output(s.name)
                        else:
                            if not s.name in model.name2block_connection:
                                raise SemanticError('Link %s refers to unknown signal "%s". We know %s.' % \
                                                (s, s.name, model.name2block_connection.keys()))
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
                        raise SemanticError('The block %s did not define signals and it has no input.'%
                                       block) 
                    if block.num_input_signals() > 0:
                        raise SemanticError('The generator block %s should have defined 0 inputs.' % 
                                        block) 
                
                # at this point the input should be defined
                assert block.are_input_signals_defined()
                # if it did not define outputs (init delayed)
                if not block.are_output_signals_defined():
                    # then we call init() again
                    res = block.init()
                    # it cannot return NOT_FINISHED again.
                    if res == Block.INIT_NOT_FINISHED:
                        raise SemanticError('Block %s cannot return NOT_FINISHED '+
                                        'after inputs have been defined. ' % block)
                    # now the outputs should be defined
                    if not block.are_output_signals_defined():
                        raise SemanticError(('Block %s still does not define outputs'+
                                        ' after init() called twice. ') % block)
                
                # at this point input/output should be defined
                assert block.are_input_signals_defined()
                assert block.are_output_signals_defined()

                previous_link = None                    
                previous_block = block
            # end if 
    
    unused_properties = set(properties.keys()).difference(used_properties)
    if unused_properties:
        raise SemanticError('Unused properties: %s -- Used: %s' % \
                            (unused_properties, used_properties))
    
    # print "--------- end model ----------------\n"           
    return model



