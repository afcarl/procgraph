from procgraph import Block

__all__ = ['Retime']

class Retime(Block):
    ''' 
        Multiples timestamps by give factor
    '''
    Block.alias('retime')

    Block.config('factor', 'Factor')

    Block.input('x')
    Block.output('y')

    def init(self):
        pass
    
    def update(self):        
        value = self.get_input(0)
        t = self.get_input_timestamp(0)
        t_ = t * self.config.factor
        self.set_output(0, value, t_)
