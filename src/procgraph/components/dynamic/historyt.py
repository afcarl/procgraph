from procgraph.core.block import Block
from procgraph.components.basic import register_block

    
class HistoryT(Block):
    ''' 
    This block collects the history of a quantity,
    and outputs (x, t).
    
    Arguments:
    - interval (seconds)  interval to record
    
    Output:
    - a tuple (x,y)
    ''' 
        
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

        
register_block(HistoryT, 'historyt')


