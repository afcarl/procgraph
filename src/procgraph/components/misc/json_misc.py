import simplejson as json

from procgraph import Block, block_alias, block_input_is_variable, block_output 

class AsJSON(Block):
    ''' Converts the input into a JSON string. 
    
        TODO: add example
    '''

    block_alias('as_json')
    block_input_is_variable('Inputs to transcribe as JSON.')
    block_output('json', 'JSON string.')
        
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
         
