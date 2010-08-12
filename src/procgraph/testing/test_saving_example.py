from procgraph.testing.utils import PGTestCase
from tempfile import NamedTemporaryFile
from procgraph.core.block import Block
from procgraph.core.model_loader import model_from_string
import pickle
from procgraph.core.registrar import default_library

class HasState(Block):
    ''' A simple block for debugging purposes 
       that puts the config "x" in the state "x". '''
    def init(self):
        # default value
        self.config.x = 42
        
        self.state.x = self.config.x
        
        self.define_input_signals([])
        self.define_output_signals([])


default_library.register('has_state', HasState)




class TestSaving(PGTestCase):
    
    def test_saving(self):
        
        # generate temporary file
        file1 = NamedTemporaryFile(suffix='file1.pickle')
        file2 = NamedTemporaryFile(suffix='file2.pickle')
        
        model_spec = '''
        --- model testing_saving
        
        |has_state x=1|
        
        on init:   load has_state.x from $file1 as pickle 
        on finish: save has_state.x  to  $file2 as pickle
        
        '''
        value = 43
        pickle.dump(value, file1)
        file1.flush()
        
        config = {'file1': file1.name, 'file2': file2.name}
        model = model_from_string(model_spec, config=config)
        
        
        model.reset_execution()
        while model.has_more():       
            model.update()
        model.finish()
        
        value2 = pickle.load(open(file2.name))
        
        self.assertEqual(value, value2)
        
        
        # should be like this
        if False:
            model.init()
            while model.update() == model.UPDATE_NOT_FINISHED:       
                pass
            model.finish()
            
        
