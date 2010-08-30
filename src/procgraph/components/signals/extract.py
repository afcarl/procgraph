from procgraph  import Block, block_alias, block_config, block_input, \
    block_output


# Make it generic?
class Extract(Block):
    ''' 
    This block extracts some of the components of a vector.
    
    '''
    block_alias('extract')
    block_input('vector')
    block_output('part')
    block_config('index')
    
    def init(self):
        self.define_input_signals(['vector'])
        self.define_output_signals(['part'])
            
        self.get_config('index')
            
    def update(self):
        index = self.get_config('index')
        vector = self.get_input('vector')
        
        part = vector[index]
        
        self.set_output('part', part)
         
