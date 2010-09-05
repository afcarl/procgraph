from procgraph import Block

class Identity(Block):
    ''' This block outputs the inputs, unchanged. 
    
        This is an example of a block whose signal configuration is dynamics:
        init() gets called twice. '''
    
    Block.alias('identity')
    Block.input_is_variable('Input signals.')
    Block.output_is_variable('Output signals, equal to input.')
    
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        # output signals get the same name as the inputs
        self.define_output_signals(self.get_input_signals_names())
        
    def update(self):
        # Just copy the input to the output
        for i in range(self.num_input_signals()):
            self.set_output(i, self.get_input(i), self.get_input_timestamp(i))
        
