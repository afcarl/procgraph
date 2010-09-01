from procgraph import Block, block_alias, block_input_is_variable, block_output

class MakeTuple(Block):
    ''' Creates a tuple out of the input signals values. 
    
        Often used for plotting two signals as (x,y); see :ref:`block:plot`.
    '''
    
    block_alias('make_tuple')
    
    block_input_is_variable('Signals to unite in a tuple.')
    
    block_output('tuple', 'Tuple containing signals.')
    
    def init(self):
        self.define_output_signals(['tuple'])
        
    def update(self):
        values = self.get_input_signals_values()
        self.output.tuple = tuple(values) 
