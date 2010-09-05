from procgraph.core.block import ETERNITY

from procgraph import Block, block_alias, block_config          

class Constant(Block):
    ''' Output a numerical constant that never changes.
    
        Example: ::
    
            |constant value=42 name=meaning| -> ...
            
        Two parameters:
        
        * ``value``, necessary
        * ``name``, optional signal name (default: const)
    ''' 
    
    block_alias('constant')
    
    block_config('value', 'Constant value to output.') 
        
    def init(self):
        # XXX FIXME this will not be supported
        #self.set_config_default('name', 'const')
        
        #self.signal_name = self.get_config('name')
        #self.value = self.get_config('value')
        self.define_output_signals(['constant'])
        self.define_input_signals([])
        
    def update(self):
        self.set_output(0, self.config.value, timestamp=ETERNITY)
        
    def __repr__(self):
        return 'Constant(%s)' % self.get_config('value')

