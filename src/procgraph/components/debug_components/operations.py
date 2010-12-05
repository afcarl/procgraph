from ...core.registrar_other import register_simple_block
from ...core.block import Block

class Minus(Block):
    ''' Implements the difference of two signals, taking care of overflows. 
    
        Because that is rarely the semantics you want to give them.
    '''
    
    Block.alias('-')
    Block.input('x', 'First signal')
    Block.input('y', 'Second signal')
    Block.output('x_minus_y', 'Result of x - y')
    Block.config('safe', 'Whether to use safe promotions. '
                 'If not specified, we will do it but warn once.',
                 default=None)

    Block.config('cases', 'Promotion rules', default={'uint8': 'int16',
                                                      'uint16': 'int32',
                                                      'uint32': 'int64' })
    def init(self):
        self.warned = False
        
    def update(self):
        # TODO:  check_array_same_shape(self, 0, 1)
        inputs = [self.get_input(0), self.get_input(1)]
        
        warned_now = False
        for i in [0, 1]:
            dtype_string = str(inputs[i].dtype)
            if dtype_string in self.config.cases:
                next = self.config.cases[dtype_string]
            
                if not self.warned:
                    self.info('Warning: promoting signal %r from %r to %r.' % 
                          (self.canonicalize_input(i),
                           dtype_string, next))
                    warned_now = True
                inputs[i] = inputs[i].astype(next)
            
        self.warned = self.warned or warned_now
        
        result = inputs[0] - inputs[1]
        
        self.set_output(0, result)
  
   
    

register_simple_block(lambda x, y: x + y, '+', num_inputs=2)
register_simple_block(lambda x, y: x * y, '*', num_inputs=2)
#register_simple_block(lambda x, y: x - y, '-', num_inputs=2)
register_simple_block(lambda x, y: x / y, '/', num_inputs=2)
 
