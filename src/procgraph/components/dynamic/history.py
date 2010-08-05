from procgraph.core.registrar import default_library
from procgraph.core.block import Block

    
class History(Block):
    ''' 
    This block collects the history of a quantity,
    and outputs (x, t).
    
    Arguments:
    - interval (seconds)  interval to record
    
    Output:
    - x
    - t
    ''' 
        
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
        
default_library.register('history', History)


class HistoryN(Block):
    ''' 
    This block collects the last n samples of a quantity,
    and outputs (x, timestamp).
    
    Arguments:
    - n, number of samples
    
    Output:
    - x
    - t
    ''' 
        
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
        
default_library.register('last_n_samples', HistoryN)

        

