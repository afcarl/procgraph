from procgraph.core.block import Block
from procgraph.core.registrar import register_block_class

class Generic(Block):
    ''' This is a generic block used mainly for debug.
        It defines inputs and outputs given by the parameters
        "in" and "out". 
        
        Parameters:
        * ``in`` (default: ``0``)
        * ``out`` (default: ``0``)  
        
        For example::
    
            A,B,C -> |generic in=3 out=5| -> a,b,c,d,e
            
            # all by itself
            |generic|
            
    '''
    def init(self):
        # use default if not set
        self.set_config_default('in', 0)
        self.set_config_default('out', 0)
        
        nin = self.get_config('in')
        nout =  self.get_config('out')
        self.define_input_signals( map(str, range(nin)) )
        self.define_output_signals( map(str, range(nout)) )


register_block_class('generic', Generic)


class Identity(Block):
    ''' This block outputs the inputs. This is an example 
        of a block whose signal configuration is dynamics:
        init() gets called twice. '''
    
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        # output signals get the same name as the inputs
        self.define_output_signals( self.get_input_signals_names() )
        
    def update(self):
        # Just copy the input to the output
        for i in range(self.num_input_signals()):
            self.set_output(i, self.get_input(i), self.get_input_timestamp(i))
        
        
register_block_class('identity', Identity)
        
          

class DoesNotDefineInput(Block):
    ''' This (erroneous) block does not register inputs '''
    
    def init(self):
        self.define_output_signals([])
    
register_block_class('DoesNotDefineInput', DoesNotDefineInput)


class DoesNotDefineOutput(Block):
    ''' This (erroneous) block does not register output '''
    
    def init(self):
        self.define_input_signals([])
        
register_block_class('DoesNotDefineOutput', DoesNotDefineOutput)

        
    


