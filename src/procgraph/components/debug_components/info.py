import numpy

from procgraph import Block, block_alias, block_input_is_variable


class Info(Block):
    ''' Prints more compact information about the inputs than :ref:`block:print`.
    
        For numpy arrays it prints their shape and dtype instead of their values. 
        
    '''
    block_alias('info')
    block_input_is_variable('Signals to describe.')
    
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED 
        
        # output signals get the same name as the inputs
        self.define_output_signals([])
        
    def update(self):
        # Just copy the input to the output 
        for i in range(self.num_input_signals()):
            val = self.get_input(i)
            if isinstance(val, numpy.ndarray):
                s = "%s %s" % (str(val.shape), str(val.dtype))
            else:
                s = str(val)
            print 'P %s %s %s' % (self.canonicalize_input(i),
                                  self.get_input_timestamp(i),
                                s)

 
