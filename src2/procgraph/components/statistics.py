from procgraph.core.block import Block
from procgraph.core.registrar import register_block_class


class Expectation(Block):
        
    def init(self):
        self.define_input_signals(['x'])
        self.define_output_signals(['Ex'])
        self.set_state('Ex', None)
        self.set_state('num_samples', 0)
        
    def update(self):
        x = self.get_input('x')
        num_samples = self.get_state('num_samples')
        Ex = self.get_state('Ex')
        
        if num_samples == 0:
            Ex = x.copy()
        else:
            Ex = (Ex * num_samples + x) / float(num_samples+1);
        
        self.set_state('Ex', Ex)
        self.set_state('num_samples', num_samples + 1)
        
        self.set_output('Ex', Ex)
            
    
register_block_class('expectation', Expectation)
