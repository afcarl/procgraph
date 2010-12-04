import cPickle as pickle

from procgraph import Block 
from procgraph.block_utils import make_sure_dir_exists


class Pickle(Block):
    ''' Dumps the input as a :py:mod:`pickle` file. '''
    Block.alias('pickle')
    Block.config('file', 'File to write to.')
    Block.input('x', 'Anything pickable.') 
        
    def write(self, x, filename):
        make_sure_dir_exists(filename)
        with open(filename, 'wb') as f:
            pickle.dump(x, f, protocol=pickle.HIGHEST_PROTOCOL)
 
    def update(self):
        self.write(self.input.x, self.config.file + '.part')
        
    def finish(self):
        self.write(self.input.x, self.config.file)


class PickleGroup(Block):
    ''' Dumps the input as a :py:mod:`pickle` file, in the form
        of a dictionary  signal name -> value.    
    '''
    Block.alias('pickle_group')
    Block.config('file', 'File to write to.')
    Block.input_is_variable() 
        
    def write(self, x, filename):
        make_sure_dir_exists(filename)
        with open(filename, 'wb') as f:
            pickle.dump(x, f, protocol=pickle.HIGHEST_PROTOCOL)
 
    def get_dict(self):
        data = {}
        for signal in self.get_input_signals_names():
            data[signal] = self.get_input(signal)
        return data
    
    def update(self):
        self.write(self.get_dict(), self.config.file + '.part')
        
    def finish(self):
        self.write(self.get_dict(), self.config.file)
