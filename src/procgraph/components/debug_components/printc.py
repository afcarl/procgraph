from procgraph import Block

class Print(Block):
    ''' Print a representation of the input values along with their timestamp. '''
    
    Block.alias('print')
    
    Block.input_is_variable('Signals to print.')
    
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED 
        
        # output signals get the same name as the inputs
        self.define_output_signals([])
        
    def update(self): 
        for i in range(self.num_input_signals()):
            print 'P %s %s %s' % (self.canonicalize_input(i),
                                  self.get_input_timestamp(i),
                                self.get_input(i))
 
