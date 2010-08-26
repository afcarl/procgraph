from procgraph.core.block import Block
from procgraph.components.basic import register_block

class FPSPrint(Block):
    ''' Prints the fps count for the input. ''' 
     
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        self.define_output_signals([])
      
        self.state.last_timestamp = None
        
    def update(self):
        
        current = max(self.get_input_signals_timestamps())
        last = self.state.last_timestamp
        if last is not None:
        
            difference = current - last
            fps = 1.0 / difference
            
            print "FPS %s %.1f" % (self.canonicalize_input(0), fps)

        self.state.last_timestamp = current
        
        
register_block(FPSPrint, 'fps_print')



