import numpy

from procgraph.core.block import Block
from procgraph.core.exceptions import BadInput
from procgraph.components.basic import register_block, register_model_spec

def isiterable(x):
    try:
        iter(x)
        return True
    except TypeError:
        return False


class ForwardDifference(Block):
    ''' Computes ``x[t+1] - x[t-1]`` normalized with timestamp. '''
    def init(self):
        self.define_input_signals(['x123', 't123'])
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
            raise BadInput('Bad timestamp sequence % s' % t, self, 't')

        # if this is a sequence of bytes, let's promove them to floats
        if x[0].dtype == numpy.dtype('uint8'):
            diff = x[2].astype('float32') - x[0].astype('float32')
        else:
            diff = x[2] - x[0]
        time = t[1]
        x_dot = diff / numpy.float32(delta)
        self.set_output('x_dot', x_dot, timestamp=time)  

register_block(ForwardDifference, 'forward_difference')

register_model_spec("""
--- model derivative 
|input name=x| --> |last_n_samples n=3| --> x,t

   x, t --> |forward_difference| --> |output name=x_dot|
    
""")

