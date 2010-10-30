from procgraph import Block

class Expectation(Block):
    ''' Computes the sample expectation of a signal. '''
    Block.alias('expectation')
    
    Block.input('x', 'Any numpy array.')
    Block.output('Ex', 'Expectation of input.')
    
    def init(self): 
        self.state.num_samples = 0
        
    def update(self):
        N = self.state.num_samples
        
        if N == 0:
            self.state.Ex = self.input.x.copy()
        else:
            self.state.Ex = (self.state.Ex * N + self.input.x) / float(N + 1);
        
        self.state.num_samples += 1
        self.output.Ex = self.state.Ex 
