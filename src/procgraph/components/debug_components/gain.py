from procgraph import Block

class Gain(Block):
    ''' FIXME: to be replaced by simpler function. '''

    Block.alias('gain')
    
    Block.config('k', 'Multiplicative gain')
    
    Block.input('in')
    Block.output('out')
    
    def init(self):
        #self.set_config_default('gain', 1)
        self.define_input_signals(['input'])
        self.define_output_signals(['out'])
    
    def update(self):
        self.output[0] = self.input[0] * self.config.k

