from procgraph import Block

class History(Block):
    ''' 
    This block collects the history of a quantity,
    and outputs two signals ``x`` and ``t``. 
    See also :ref:`block:historyt` and :ref:`block:last_n_samples`.
    ''' 
    Block.alias('history')
    
    Block.config('interval', 'Length of the interval to record.', default=10)
    
    Block.input('values', 'Any signal.')
    
    Block.output('x', 'Sequence of values.')
    Block.output('t', 'Sequence of timestamps.')
    
    def init(self): 
        self.state.x = []
        self.state.t = []
    
    def update(self):
        
        sample = self.get_input(0)
        timestamp = self.get_input_timestamp(0)
         
        x = self.state.x
        t = self.state.t
        
        x.append(sample)
        t.append(timestamp)
        
        
        while abs(t[0] - t[-1]) > self.config.interval:
            t.pop(0)
            x.pop(0)
            
        self.output.x = x 
        self.output.t = t 
         
