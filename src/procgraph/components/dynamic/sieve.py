from procgraph import Block 

class Sieve(Block):
    ''' 
    This block decimates the data in time by transmitting
    only one in ``n`` updates.
    '''
    
    Block.alias('sieve')
    
    Block.config('n', 'Decimation level; ``n = 3`` means transmit one in three.')
    
    Block.input('data', 'Arbitrary input signals.')
    Block.output('decimated', 'Decimated signals.')
     
    def init(self):
        # output signals get the same name as the inputs
        #self.define_output_signals(self.get_input_signals_names())
                
        self.state.count = 0

    def update(self):
        # make something happen after we have waited enough
        if 0 == self.state.count % self.config.n: 
            # Just copy the input to the output
            for i in range(self.num_input_signals()):
                self.set_output(i, self.get_input(i), self.get_input_timestamp(i))

        self.state.count += 1

