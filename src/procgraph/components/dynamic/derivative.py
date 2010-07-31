from procgraph.core.model_loader import add_models_to_library
from procgraph.core.registrar import default_library
from procgraph.core.block import Block
from procgraph.core.exceptions import BadInput
import numpy

def isiterable(x):
    try:
        iter(x)
        return True
    except TypeError:
        return False


class ForwardDifference(Block):
    def init(self):
        self.define_input_signals(['x123','t123'])
        self.define_output_signals(['x_dot'])
        
    def update(self):
        x = self.get_input('x123')
        t = self.get_input('t123')
        if not isiterable(x) or len(x) != 3:
            raise BadInput('Expected arrays of 3 elements', self, 'x')
        if not isiterable(t) or len(t) != 3:
            raise BadInput('Expected arrays of 3 elements', self, 't')
       
        delta = t[2] - t[0]
        
        if not delta > 0:
            raise BadInput('Bad timestamp sequence %s' % t, self, 't')

        # if this is a sequence of bytes, let's promove them to floats
        if x[0].dtype == numpy.dtype('uint8'):
            diff = x[2].astype('float32') - x[0].astype('float32')
        else:
            diff = x[2] - x[0]
        time = t[1]
        x_dot = diff / numpy.float32(delta)
        self.set_output('x_dot', x_dot, timestamp=time)  

default_library.register('forward_difference', ForwardDifference)

model_spec = """
--- model derivative 
|input name=x| --> |last_n_samples n=3| --> x,t

   x, t --> |forward_difference| --> |output name=x_dot|
    
"""
add_models_to_library(default_library, model_spec)

