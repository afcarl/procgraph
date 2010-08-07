'''

.. block:: join

  |towrite|
  

'''
from procgraph.core.block import Block 
from procgraph.core.registrar import default_library


# Make it generic?
class Extract(Block):
    ''' 
    This block extracts some of the components 
    
    Arguments:
    
    - index
    
    '''
    def init(self):
        self.define_input_signals(['vector'])
        self.define_output_signals(['part'])
            
        self.get_config('index')
            
    def update(self):
        index = self.get_config('index')
        vector = self.get_input('vector')
        
        part = vector[index]
        
        self.set_output('part', part)
         
        
    
default_library.register('extract', Extract)


