from procgraph.core.block import Block
from procgraph.core.registrar import default_library
import numpy



class Identity(Block):
    ''' This block outputs the inputs. This is an example 
        of a block whose signal configuration is dynamics:
        init() gets called twice. '''
    
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        # output signals get the same name as the inputs
        self.define_output_signals( self.get_input_signals_names() )
        
    def update(self):
        # Just copy the input to the output
        for i in range(self.num_input_signals()):
            self.set_output(i, self.get_input(i), self.get_input_timestamp(i))
        
        
default_library.register('identity', Identity)
        
          

class Print(Block):
    ''' Prints the inputs '''
    
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        #print self.get_input_signals_names()
        # output signals get the same name as the inputs
        self.define_output_signals([])
        
    def update(self):
        # Just copy the input to the output
        # print self.get_input_signals_names()
        for i in range(self.num_input_signals()):
            print 'P %s %s %s' % (self.canonicalize_input(i),
                                  self.get_input_timestamp(i),
                                self.get_input(i))



default_library.register('print', Print)
        
class Info(Block):
    ''' Prints the inputs '''
    
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        #print self.get_input_signals_names()
        # output signals get the same name as the inputs
        self.define_output_signals([])
        
    def update(self):
        # Just copy the input to the output
        # print self.get_input_signals_names()
        for i in range(self.num_input_signals()):
            val = self.get_input(i)
            if isinstance(val, numpy.ndarray):
                s = "%s %s" % (str(val.shape), str(val.dtype))
            else:
                s = str(val)
            print 'P %s %s %s' % (self.canonicalize_input(i),
                                  self.get_input_timestamp(i),
                                s)


        
default_library.register('info', Info)
        
          

    


