from procgraph.core.block import Block
from procgraph.components.basic import register_block


class Sieve(Block):
    ''' 
    This block only transmits every n steps. 
    
    Config:
    - n  

    Input: variable 
    Output: variable (same as input)

    ''' 
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        # output signals get the same name as the inputs
        self.define_output_signals(self.get_input_signals_names())
        
        self.get_config('n')
        self.set_state('count', 0) 

    def update(self):
        count = self.get_state('count')
        n = self.get_config('n')

        # make something happen after we have waited enough
        if 0 == count % n: 
            # Just copy the input to the output
            for i in range(self.num_input_signals()):
                self.set_output(i, self.get_input(i), self.get_input_timestamp(i))

        count += 1
        self.set_state('count', count)
        
register_block(Sieve, 'sieve')

  
