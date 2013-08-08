from procgraph import Block

__all__ = ['AllReady']


class AllReady(Block):
    ''' 
        This block outputs the inputs, unchanged. 
    '''
    
    Block.alias('all_ready')
    
    Block.input_is_variable('Input signals.', min=1)
    Block.output_is_variable('Output signals, equal to input.')

    
    def update(self):
        n = self.num_input_signals()
        ts = [self.get_input_timestamp(i) for i in range(n)]
        self.debug('ts: %s' % ts)
        values = [self.get_input(i) for i in range(n)]
        if None in values:
            self.debug('waiting...')
            return
        
        for i in range(self.num_input_signals()):
            self.set_output(i, self.get_input(i), self.get_input_timestamp(i))

