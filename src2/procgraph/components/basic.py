from procgraph.core.block import Block, Generator
from math import sqrt
from numpy import random 
from procgraph.core.registrar import register_block_class

class GenericOperation(Block):
        
    def update(self):
        assert self.input_signals is not None
        if len(self.input_signals) < 2:
            raise ValueError('Too few arguments')
        in1 = self.get_input(0)
        in2 = self.get_input(1)
        res = self.f(in1, in2) 
        for s in self.input_signals[2:]:
            res = self.f(res, self.get_input(s))
        self.set_output(0, res)
    
class Plus(GenericOperation):
    def init(self):
        self.f = lambda x,y : x+y
        self.define_output_signals(['result'])
    
register_block_class('+', Plus)
    
class Constant(Block):
    ''' Creates a numerical constant that never changes.::
    
            |constant value=42 name=meaning| -> ...
            
        Two parameters
        * value, necessary
        * name, optional signal name (default: const)
    ''' 
        
    def init(self):
        self.set_config_default('name', 'const')
        
        self.signal_name  = self.get_config('name')
        self.value = self.get_config('value')
        self.define_output_signals([self.signal_name])
        self.define_input_signals([])
        
    def update(self):
        self.set_output(0, self.value)
        
    def __repr__(self):
        return 'Constant(%s)' % self.get_config('value')

register_block_class('constant', Constant)


class Gain(Block):

    def init(self):
        #self.set_config_default('gain', 1)
        self.define_input_signals(['input'])
        self.define_output_signals(['out'])
    
    def update(self):
        self.set_output(0, self.get_input(0) * self.get_config('gain') )

register_block_class('gain', Gain)
        
class Delay(Block):

    def init(self):
        self.set_state(0, None)
        
    def update(self):
        self.set_output(0, self.get_state(0))
        self.set_state(0, self.get_input(0))

    
register_block_class('delay', Delay)
    
class RandomGenerator(Generator):    
    def init(self):
        self.set_config_default('variance', 1)
        self.define_input_signals([])
        self.define_output_signals(['random'])
    
    def has_more(self):
        return True
    
    def update(self):
        variance = self.get_config('variance')
        self.set_output(0, random.rand(1) * sqrt(variance) )
        
register_block_class('rand', RandomGenerator)







        
        
        