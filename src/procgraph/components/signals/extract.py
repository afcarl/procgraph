from procgraph.core.block import Block
from procgraph.components.basic import register_block


# Make it generic?
class Extract(Block):
    ''' 
    This block extracts some of the components 
    
    Arguments:
    
    - index
    
    '''
    def init(self):
        self.define_input_signals(['vector'])
        self.define_output_signals(['part'])
            
        self.get_config('index')
            
    def update(self):
        index = self.get_config('index')
        vector = self.get_input('vector')
        
        part = vector[index]
        
        self.set_output('part', part)
         
        
register_block(Extract, 'extract')


