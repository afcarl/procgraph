import time

from procgraph import Block 


class FPSLimit(Block):
    ''' This block limits the output update to a certain *realtime* framerate.
    
    Note that this uses realtime wall clock time -- not the data time!
    This is mean for real-time applications, such as visualization.''' 
     
    Block.alias('fps_limit')
    
    Block.config('fps', 'Realtime fps limit.')
    
    Block.input_is_variable('Arbitrary signals.')
    Block.output_is_variable('Arbitrary signals with limited framerate.')
    
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        # output signals get the same name as the inputs
        self.define_output_signals(self.get_input_signals_names())
       
        
        self.state.last_timestamp = None
        
    def update(self):
        should_update = False
        
        last = self.state.last_timestamp
        current = time.time()
        
        if last is None:
            should_update = True
            self.state.last_timestamp = current
        else:
            fps = self.config.fps 
            delta = 1.0 / fps
            difference = current - last
            #print "difference: %s ~ %s" % (difference, delta)
            if difference > delta:
                should_update = True
                self.state.last_timestamp = current

            
        if should_update:
            # Just copy the input to the output
            for i in range(self.num_input_signals()):
                self.set_output(i, self.get_input(i), self.get_input_timestamp(i))
 
