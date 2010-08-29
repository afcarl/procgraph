from procgraph  import Block, block_alias, block_config, block_output

    
class HistoryT(Block):
    ''' 
    This block collects the signals samples of a signals,
    and outputs *one* signal containing a tuple  ``(t,x)``. 
    See also :ref:`block:last_n_samples` and :ref:`block:history`.
    ''' 
    block_alias('historyt')
    
    block_config('interval', 'Length of interval (seconds).')
    
    block_output('history', 'Tuple ``(t,x)`` containing two arrays.')
    
    def init(self):
        self.set_config_default('interval', 10)
        
        self.define_output_signals(['history'])
        self.define_input_signals(['input'])
        
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
    
    
        self.output.history = (t, x)
 
