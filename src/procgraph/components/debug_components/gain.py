from procgraph import Block

class Gain(Block):
    ''' FIXME: to be replaced by simpler function. '''

    Block.alias('gain')
    
    Block.config('k', 'Multiplicative gain')
    
    Block.input('in')
    Block.output('out')
    
    def update(self):
        self.output[0] = self.input[0] * self.config.k

