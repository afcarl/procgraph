''' Components used for debugging and unit tests. '''

from procgraph import Block, Generator 

import constant, identity, info, printc

import gain

class Clock(Generator):
    Block.alias('clock')
    Block.config('interval', default=1)
    Block.output('clock')
    
    def init(self): 
        self.state.clock = 0
        
    def update(self):
        self.set_output('clock', self.state.clock, timestamp=self.state.clock)
        self.state.clock += self.config.interval
    
    def next_data_status(self):
        return (True, self.state.clock + self.config.interval)
    


