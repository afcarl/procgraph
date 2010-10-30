from procgraph.core.block import ETERNITY

from procgraph import Block          

class Constant(Block):
    ''' Output a numerical constant that never changes.
    
        Example: ::
    
            |constant value=42 name=meaning| -> ...
            
        Two parameters:
        
        * ``value``, necessary
        * ``name``, optional signal name (default: const)
    ''' 
    
    Block.alias('constant')
    
    Block.config('value', 'Constant value to output.') 
    Block.output('constant')
        
    def update(self):
        self.set_output(0, self.config.value, timestamp=ETERNITY)
        
    def __repr__(self):
        return 'Constant(%s)' % self.config.value

