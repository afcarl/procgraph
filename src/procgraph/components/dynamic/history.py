from procgraph  import Block, block_alias, block_config, block_output
     
class History(Block):
    ''' 
    This block collects the history of a quantity,
    and outputs two signals ``x`` and ``t``. 
    See also :ref:`block:historyt` and :ref:`block:last_n_samples`.
    ''' 
    block_alias('history')
    
    block_config('interval', 'Length of the interval to record.')
    
    block_output('x', 'Sequence of values.')
    block_output('t', 'Sequence of timestamps.')
    
    def init(self):
        self.set_config_default('interval', 10)
        
        self.define_output_signals(['x', 't'])
        self.define_input_signals(['input'])
        
        self.set_state('x', [])
        self.set_state('t', [])
    
    def update(self):
        
        sample = self.get_input(0)
        timestamp = self.get_input_timestamp(0)
         
        x = self.get_state('x')
        t = self.get_state('t')
        
        x.append(sample)
        t.append(timestamp)
        
        interval = self.get_config('interval')
        while abs(t[0] - t[-1]) > interval:
            t.pop(0)
            x.pop(0)
            
        self.set_output('x', x) 
        self.set_output('t', t)
         
class HistoryN(Block):
    ''' 
    This block collects the last N samples of a signals,
    and outputs two signals ``x`` and ``t``. 
    See also :ref:`block:historyt` and :ref:`block:history`.
    ''' 
    block_alias('last_n_samples')
    
    block_config('n', 'Number of samples to retain.')
    
    block_output('x', 'Sequence of values.')
    block_output('t', 'Sequence of timestamps.')
        
    def init(self):
        self.get_config('n')
        
        self.define_output_signals(['x', 't'])
        self.define_input_signals(['input'])
        
        self.set_state('x', [])
        self.set_state('t', [])
    
    def update(self):
        
        sample = self.get_input(0)
        timestamp = self.get_input_timestamp(0)
         
        x = self.get_state('x')
        t = self.get_state('t')
        
        x.append(sample)
        t.append(timestamp)
        
        n = self.get_config('n')
        while len(x) > n:
            t.pop(0)
            x.pop(0)
            
        if len(x) == n:
            self.set_output('x', x) 
            self.set_output('t', t) 
