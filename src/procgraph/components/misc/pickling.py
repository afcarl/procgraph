import pickle, os

from procgraph import Block, block_alias, block_input, block_config 


class Pickle(Block):
    ''' Dumps the input as a :py:mod:`pickle` file. '''
    block_alias('pickle')
    block_config('file', 'File to write.')
    block_input('x', 'Anything pickable.')
     
    def init(self):
        self.define_input_signals(['x'])
        self.define_output_signals([])
        
        file = self.config.file
        
    def update(self):
        dir = os.path.dirname(self.config.file)
        if not os.path.exists(dir):
            os.makedirs(dir)
        pickle.dump(self.input.x, open(self.config.file, 'wb'))
 
