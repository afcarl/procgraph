from procgraph import Block, block_alias, block_input, block_output


class Expectation(Block):
    ''' Computes the sample expectation of a signal. '''
    block_alias('expectation')
    
    block_input('x', 'Any numpy array.')
    block_output('Ex', 'Expectation of input.')
    
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
