
from procgraph import Block, block_alias, block_input, block_config

class ToFile(Block):
    ''' Prints the input line by line to a given file.'''
    block_alias('to_file')
    
    block_config('file', 'File to write.')

    block_input('values', 'Anything you wish to print to file.')
    
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
