from procgraph.core.block import Block
from procgraph.core.registrar import default_library


class ModelInput(Block):
    ''' This represents one input to the model. '''
    
    Block.alias('input')

    Block.config('name')
    
    Block.output('dummy')
    
    def init(self):
        self.signal_name = self.config.name
        self.define_output_signals([self.signal_name])
        self.define_input_signals([])
        
    def update(self):
        pass
      
      
class ModelOutput(Block):
    ''' This represents one output to the model. '''
    
    Block.alias('output')
    
    Block.config('name')
    
    Block.input('dummy')
    
    def init(self):
        self.signal_name = self.config.name
        self.define_input_signals([self.signal_name])
        self.define_output_signals([])
        
    def update(self):
        pass
    
     

