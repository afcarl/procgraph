import pickle, os

from procgraph import Block 


class Pickle(Block):
    ''' Dumps the input as a :py:mod:`pickle` file. '''
    Block.alias('pickle')
    Block.config('file', 'File to write to.')
    Block.input('x', 'Anything pickable.')
     
    def init(self):
        self.define_input_signals(['x'])
        self.define_output_signals([])
        
    def update(self):
        dir = os.path.dirname(self.config.file)
        if not os.path.exists(dir):
            os.makedirs(dir)
        pickle.dump(self.input.x, open(self.config.file, 'wb'))
 
