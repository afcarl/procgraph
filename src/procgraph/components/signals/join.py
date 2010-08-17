'''

.. block:: join

  |towrite|
  

'''
import numpy

from procgraph.core.block import Block  
from procgraph.components.basic import register_block

class Join(Block):
    ''' 
    This block joins multiple signals into one.
    '''
    def init(self): 
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        self.define_output_signals(['joined'])
        
        sizes = {}
        names = self.get_input_signals_names()
        for signal in names:
            sizes[signal] = None 
            
        self.set_state('sizes', sizes)
            
    def update(self):
        sizes = self.get_state('sizes')
        result = []
        for name in self.get_input_signals_names():
            value = self.get_input(name)
            size = len(value)
            if value is None:
                return
            if sizes[name] is None:
                sizes[name] = size
            else:
                if size != sizes[name]:
                    raise Exception('Signal %s changed size from %s to %s.' % \
                                    (name, sizes[name], size))
            
            result.extend(value)
        
        self.set_output(0, numpy.array(result))
         
        
register_block(Join, 'join')


