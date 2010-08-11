from procgraph.core.block import Block, Generator, ETERNITY
from math import sqrt
from numpy import random 
from procgraph.core.registrar import default_library
from procgraph.core.exceptions import ModelExecutionError
 

COMPULSORY = 'compulsory-param'

def make_generic(num_inputs, num_outputs, operation, **parameters):
    # make a copy
    parameters = dict(parameters)
    
    class GenericOperation(Block):
            
        def init(self):
            for key, value in parameters.items():
                if value != COMPULSORY:
                    self.set_config_default(key, value)
            self.define_input_signals(map(str, range(num_inputs)))
            self.define_output_signals(map(str, range(num_outputs)))
   
        def update(self):
            args = []
            for i in range(num_inputs):
                args.append(self.get_input(i))
                
            params = {}
            for key in parameters.keys():
                params[key] = self.get_config(key)
                
            try:
                result = operation(*args, **params)
            except Exception as e:
                raise ModelExecutionError("While executing %s: %s" % \
                                          (operation, e), block=self)
        
            
            if num_outputs == 1:
                self.set_output(0, result)
            else:
                for i in range(num_outputs):
                    self.set_output(i, result[i])
        
    return GenericOperation

default_library.register('+', make_generic(2, 1, lambda x, y: x + y))
default_library.register('*', make_generic(2, 1, lambda x, y: x * y))
default_library.register('-', make_generic(2, 1, lambda x, y: x - y))
default_library.register('/', make_generic(2, 1, lambda x, y: x / y))

    
def define_simple_block(function, name=None, num_inputs=1, num_outputs=1, params={}):
    if name is None:
        name = function.__name__
    
    block = make_generic(num_inputs, num_outputs, function, **params)
    
    default_library.register(name, block)

    
class Constant(Block):
    ''' Creates a numerical constant that never changes.::
    
            |constant value=42 name=meaning| -> ...
            
        Two parameters
        * value, necessary
        * name, optional signal name (default: const)
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

default_library.register('constant', Constant)


class Gain(Block):

    def init(self):
        #self.set_config_default('gain', 1)
        self.define_input_signals(['input'])
        self.define_output_signals(['out'])
    
    def update(self):
        self.set_output(0, self.get_input(0) * self.get_config('gain'))

# TODO: make generic
default_library.register('gain', Gain) 

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
    
default_library.register('clock', Clock)


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
        
default_library.register('rand', RandomGenerator)
        
        
