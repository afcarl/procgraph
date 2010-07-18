from procgraph.core.block import Block
from procgraph.parsing.model_parsing import ParsedAssignment, Connection, ParsedBlock,\
    ParsedSignalList, ParsedSignal

from procgraph.components import *
from procgraph.core.registrar import get_block_class


class BlockConnection:
    def __init__(self, block1, block1_signal, block2, block2_signal, public_name=None ):
        assert block1 is not None
        assert block1_signal is not None
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
    
    def __init__(self):
        self.name2block = {}
        self.name2block_connection = {}
        # block -> block unresolved 
        self.unresolved = {}
        
    def summary(self):
        print "--- Model: %d blocks, %d connections" % \
            (len(self.name2block),len(self.name2block_connection))
        for name, block in self.name2block.items():
            print "- %s: %s" % (name, block)
            
        for name, conn in self.name2block_connection.items():
            print "- %s: %s" % (name, conn) 
    
def instance_block(name, operation, config):
    ''' Instances a block '''
    t = get_block_class(operation)
    block = t(name=name, config=config)
    
    return block

def check_link_compatibility_input(previous_block, previous_link):
    assert isinstance(previous_link, ParsedSignalList)
    # if the previous block did not define output signals
    if not previous_block.output_signals_defined():
        # We define a bunch of anonymous signals
        n = len(previous_link.signals)
        previous_block.define_output_signals(map(str, range(n)))

    # We check that we have good matches for the previous                    
    for i, s in enumerate(previous_link.signals):
        assert isinstance(s, ParsedSignal)
        if s.block_name is not None:
            raise Exception('Could not give a block name between two blocks.')
        if s.local_input is None:
            s.local_input = i
                    
        if not previous_block.valid_output(s.local_input):
            raise Exception('Could not find output name "%s"(%s) in %s' % \
                            (s.local_input, type(s.local_input), previous_block))
            
        s.local_input = previous_block.canonicalize_output(s.local_input)

def check_link_compatibility_output(block, previous_link):
    assert isinstance(previous_link, ParsedSignalList)
    # if the block did not define input signals
    if not block.input_signals_defined():
        # We define a bunch of anonymous signals
        n = len(previous_link.signals)
        block.define_input_signals(map(str, range(n)))
    
    # we check that we have good matches for the next    
    for i, s in enumerate(previous_link.signals):
        assert isinstance(s, ParsedSignal)
        
        if s.local_output is  None:
            s.local_output = i
                    
        if not block.valid_input(s.local_output):
            raise Exception('Could not find input name "%s" in %s' % \
                            s.local_output, s.block)
            
        s.local_output = block.canonicalize_input(s.local_output)
 
     
def create_from_parsing_results(parsed_model):
    print "\n\n --- new model ----------------"
    print "Parsed: %s" % parsed_model

    model = Model()
    
    # First we collect all the properties, to use
    # in initialization.
    properties = {}
    for element in parsed_model:
        if isinstance(element, ParsedAssignment):
            # if it is of the form  object.property = value
            if '.' in element.key:
                object, property = element.key.split('.')
                if not object in properties:
                    properties[object] = {}
                properties[object][property] = element.value
            else:
                properties[element.key] = element.value 
            pass  

    # Then we instantiate all the blocks
    connections = [x for x in parsed_model if isinstance(x, Connection)]
    
    # Things for generating names for anonymous blocks
    num_anonymous_blocks = 0
    anonymous_name_pattern = 'block%d'
    
    # Iterate over connections 
    for connection in connections:
        previous_block = None
        previous_link = None
        
        print "Looking at connection %s" % connection.elements
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
                            raise Exception('Terminator connection %s cannot have a local output' %s)  
                        
                        BC = BlockConnection(block1=previous_block, block1_signal=s.local_input,
                                             block2=None, block2_signal=None, public_name=s.name)
                        
                        if s.name in model.name2block_connection:
                            raise Exception('Signal "%s" already defined. ' % s.name)
                        model.name2block_connection[s.name] = BC
             
                
            if isinstance(element, ParsedBlock):
                
                # give a name if anonymous
                if element.name is None:
                    element.name = anonymous_name_pattern % num_anonymous_blocks
                    num_anonymous_blocks += 1
                
                # update the configuration if given
                if element.name in properties:
                    element.config.update(properties[element.name])
                    # delete so we can keep track of unused properties
                    del properties[element.name]
                
                block = instance_block(element.name, element.operation, \
                                       element.config)
                
                block.init()
                
                model.name2block[element.name] = block
                
                print "Defined block %s = %s " % (element.name , block)
                
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
                        BC = BlockConnection(previous_block, s.local_input,
                                             block, s.local_output, s.name)
                        
                        if s.name in model.name2block_connection:
                            raise Exception('Signal "%s" already defined. ' % s.name)
                        model.name2block_connection[s.name] = BC
                
                elif previous_block is not None and previous_link is None:
                    # anonymous connection between two blocks
                    # if the previous block has already defined the output
                    # AND we didn't define the input, then we copy that
                    if previous_block.output_signals_defined() \
                        and not block.input_signals_defined():
                        block.define_input_signals()
                    # If both have defined, we check they have the same
                    # number of signals
                    elif  previous_block.output_signals_defined() \
                        and block.input_signals_defined():
                        # check that they have the same number of signals
                        num_out = len(previous_block.output_signals)
                        num_in = len(block.input_signals) 
                        if num_out != num_in:
                            raise Exception('Tried to connect two blocks (%s \
and %s) with incompatible signals; you must do this expliciyl.' % (previous_block, block))
                        if num_out == 0:
                            raise Exception('Tried to connect two blocks (%s, %s) w/no signals.'\
                                            % (previous_block, block))
                            
                        # just create default connections
                        for i in range(num_out):
                            name = 'link_%s_to_%s_%d' % \
                                (previous_block.name, block.name, i)
                            BC = BlockConnection(previous_block, i,
                                             block, i, name)
                            model.name2block_connection[name] = BC
                
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
                            raise Exception('Link %s cannot use local input without antecedent. ' %\
                                            s)
                        # Check if it is using an explicit block name
                        if s.block_name is not None:
                            if not s.block_name in model.name2block:
                                raise Exception('Link %s refers to unknown block "%s". We know %s.' % 
                                                (s, s.block_name, model.name2block.keys()))
                            input_block = model.name2block[s.block_name]
                            if not input_block.valid_output(s.name):
                                raise Exception('Link %s refers to unknown output %s in block %s. ' % 
                                                (s, s.name, input_block))
                            s.local_input = input_block.canonicalize_output(s.name)
                        else:
                            if not s.name in model.name2block_connection:
                                raise Exception('Link %s refers to unknown signal "%s". We know %s.' % \
                                                (s, s.name, model.name2block_connection.keys()))
                            defined_signal = model.name2block_connection[s.name]
                            input_block = defined_signal.block1
                            s.local_input = defined_signal.block1_signal
                            
                        # make up a name    
                        name = "input_%s_for_%s" % (s.local_output, block)
                        BC = BlockConnection(input_block, s.local_input,
                                             block, s.local_output, name)
                        model.name2block_connection[name] = BC
                
                elif previous_block is None and previous_link is None:
                    # make sure it's a generator?
                    if (not block.input_signals_defined()) or len(block.input_signals) > 0:
                        raise Exception('The generator block %s should have defined 0 inputs.' % 
                                        block) 
                
                previous_link = None                    
                previous_block = block
            # end if 
     
    print "--------- end model ----------------\n"           
    return model
                
                 


