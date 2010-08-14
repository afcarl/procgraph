from procgraph.core.block import Block
from procgraph.components.basic import register_block

class ToFile(Block):
    ''' Prints the input line by line to a given file.'''
    
    def init(self):
        # We take any number of output
        self.define_output_signals(['values'])
        self.define_output_signals([])
        
        self.file = open(self.config.file, 'w')
        
    def update(self):
        s = str(self.input[0])
        self.file.write(s)
        self.file.write('\n')
        self.file.flush()
        
register_block(ToFile, 'to_file')
