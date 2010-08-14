from procgraph.core.block import Block
import simplejson as json
from procgraph.components.basic import register_block

class AsJSON(Block):
    ''' Converts the input into a JSON string. '''
    
    def init(self):
        # We take any number of output
        self.define_output_signals(['json'])
        
    def update(self):
        data = {}
        data['timestamp'] = max(self.get_input_signals_timestamps())
        for i in range(self.num_input_signals()):
            name = self.canonicalize_input(i)
            value = self.input[name]
            data[name] = value 
            
        self.output.json = json.dumps(data)  
        
register_block(AsJSON, 'as_json')
