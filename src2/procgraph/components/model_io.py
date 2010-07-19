from procgraph.core.block import Block
from procgraph.core.registrar import register_block_class


class ModelInput(Block):
    ''' This represents one input to the model. '''
    def init(self):
        self.signal_name = self.get_config('name')
        self.define_output_signals([self.signal_name])
        self.define_input_signals([])
        
    def update(self):
        pass
      
      
class ModelOutput(Block):
    ''' This represents one output to the model. '''
    def init(self):
        self.signal_name = self.get_config('name')
        self.define_input_signals([self.signal_name])
        self.define_output_signals([])
        
    def update(self):
        pass
    
    
register_block_class('input', ModelInput)
register_block_class('output', ModelOutput)


