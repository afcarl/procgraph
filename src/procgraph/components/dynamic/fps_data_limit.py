from procgraph.core.block import Block
from procgraph.core.registrar import default_library

class FPSDataLimit(Block):
    ''' This block limits the output update to a certain framerate. ''' 
     
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        # output signals get the same name as the inputs
        self.define_output_signals(self.get_input_signals_names())
      
        fps = self.config.fps  #@UnusedVariable
        
        self.state.last_timestamp = None
        
    def update(self):
        should_update = False
        
        last = self.state.last_timestamp
        current = max(self.get_input_signals_timestamps())
        
        if last is None:
            should_update = True
            self.state.last_timestamp = current
        else:
            fps = self.config.fps 
            delta = 1.0 / fps
            difference = current - last
            if difference > delta:
                #print "%s difference: %s ~ %s" % (self, difference, delta)
                #print "%s difference: %dms > %d" % (self, difference * 1000, delta * 1000)
                should_update = True
                self.state.last_timestamp = current

            
        if should_update:
            # Just copy the input to the output
            for i in range(self.num_input_signals()):
                self.set_output(i, self.get_input(i), self.get_input_timestamp(i))

        
default_library.register('fps_data_limit', FPSDataLimit)



