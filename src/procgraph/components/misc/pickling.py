import pickle

from procgraph.core.block import Block
from procgraph.components.basic import register_block
import os

class Pickle(Block):
    ''' Dumps the input as a pickle file. ''' 
    def init(self):
        self.define_input_signals(['x'])
        self.define_output_signals([])
        
        file = self.config.file
        
    def update(self):
        dir = os.path.dirname(self.config.file)
        if not os.path.exists(dir):
            os.makedirs(dir)
        pickle.dump(self.input.x, open(self.config.file, 'wb'))

        
register_block(Pickle, 'pickle')
