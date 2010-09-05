''' Components used for debugging and unit tests. '''

from procgraph import Block, Generator, block_alias 

import constant, identity, info, printc

import gain

class Clock(Generator):
    block_alias('clock')
    
    def init(self):
        self.define_input_signals([])
        self.define_output_signals(['clock'])
        self.set_config_default('interval', 1)
        self.set_state('clock', 0)
    def update(self):
        clock = self.get_state('clock')
        clock += self.get_config('interval')
        self.set_state('clock', clock)
        self.set_output('clock', clock, timestamp=clock)
    def next_data_status(self):
        return (True, self.get_state('clock') + self.get_config('interval'))
    


