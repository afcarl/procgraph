import numpy

from procgraph.core.block import Block, Generator, ETERNITY
from procgraph.components.basic import register_block


class Identity(Block):
    ''' This block outputs the inputs, unchanged. 
    
        This is an example of a block whose signal configuration is dynamics:
        init() gets called twice. '''
    
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
        
        
register_block(Identity, 'identity') 
          

class Print(Block):
    ''' Print a representation of the input values along with their timestamp. '''
    
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


register_block(Print, 'print')

        
class Info(Block):
    ''' Prints more compact information about the inputs than :ref:`block:print`.
    
        For numpy arrays it prints their shape and dtype instead of their values. 
        
    '''
    
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


register_block(Info, 'info') 
          

class Constant(Block):
    ''' Output a numerical constant that never changes.
    
        Example: ::
    
            |constant value=42 name=meaning| -> ...
            
        Two parameters:
        
        * ``value``, necessary
        * ``name``, optional signal name (default: const)
    ''' 
        
    def init(self):
        self.set_config_default('name', 'const')
        
        self.signal_name = self.get_config('name')
        self.value = self.get_config('value')
        self.define_output_signals([self.signal_name])
        self.define_input_signals([])
        
    def update(self):
        self.set_output(0, self.value, timestamp=ETERNITY)
        
    def __repr__(self):
        return 'Constant(%s)' % self.get_config('value')

register_block(Constant, 'constant')
 

class Gain(Block):
    ''' FIXME: to be replaced by simpler function. '''

    def init(self):
        #self.set_config_default('gain', 1)
        self.define_input_signals(['input'])
        self.define_output_signals(['out'])
    
    def update(self):
        self.set_output(0, self.get_input(0) * self.get_config('gain'))

# TODO: make generic

register_block(Gain, 'gain')
 

class Clock(Generator):
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
    
register_block(Clock, 'clock')


class RandomGenerator(Generator):    
    def init(self):
        self.set_config_default('variance', 1)
        self.define_input_signals([])
        self.define_output_signals(['random'])
    
    def has_more(self):
        return True
    
    def update(self):
        variance = self.get_config('variance')
        self.set_output(0, random.rand(1) * sqrt(variance))
        

register_block(RandomGenerator, 'rand')



