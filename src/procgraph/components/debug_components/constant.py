
from procgraph import Block, ETERNITY

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
        # FIXME: are you sure we need ETERNITY?
        self.set_output(0, self.config.value, timestamp=ETERNITY)
        
    def __repr__(self):
        return 'Constant(%s)' % self.config.value

