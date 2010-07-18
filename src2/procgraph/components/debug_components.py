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

