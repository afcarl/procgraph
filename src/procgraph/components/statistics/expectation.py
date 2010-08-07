from procgraph.core.block import Block
from procgraph.core.registrar import default_library


class Expectation(Block):
        
    def init(self):
        self.define_input_signals(['x'])
        self.define_output_signals(['Ex'])
        self.state.Ex = None
        self.state.num_samples = 0
        
    def update(self):
        x = self.input.x
        Ex = self.state.Ex
        num_samples = self.state.num_samples
        
        if num_samples == 0:
            Ex = x.copy()
        else:
            Ex = (Ex * num_samples + x) / float(num_samples + 1);
        
        self.state.Ex = Ex
        self.state.num_samples = num_samples + 1
        
        self.output.Ex = Ex
            
    
default_library.register('expectation', Expectation)
