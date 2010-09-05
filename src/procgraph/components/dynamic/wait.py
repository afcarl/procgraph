from procgraph import Block 
        
class Wait(Block):
    ''' 
    This block waits a given number of updates before transmitting the 
    output.

    ''' 
    Block.alias('wait')
    
    Block.config('n', 'Number of updates to wait at the beginning.')
    
    Block.input_is_variable('Arbitrary signals.')
    Block.output_is_variable('Arbitrary signals, minus the first ``n`` updates.')
    
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        # output signals get the same name as the inputs
        self.define_output_signals(self.get_input_signals_names())
        
        self.state.count = 0

    def update(self):
        count = self.state.count
        count += 1
        self.set_state('count', count)
        #print 'Counting %s' %count
        # make something happen after we have waited enough
        if count >= self.config.n: 
            # Just copy the input to the output
            for i in range(self.num_input_signals()):
                self.set_output(i, self.get_input(i), self.get_input_timestamp(i))
 
