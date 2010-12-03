import pickle
from tempfile import NamedTemporaryFile

from .utils import PGTestCase
from procgraph import Block
from procgraph.core.model_loader import model_from_string

class HasState(Block):
    ''' A simple block for debugging purposes 
       that puts the config "x" + 1 in the state "x". '''
       
    Block.alias('has_state')
    
    Block.config('x', default=42)
    
    Block.output('x')
    
    def init(self):
        
        self.state.x = self.config.x 

    def update(self):
        self.set_output(0, self.state.x + 1, timestamp=1)




class TestSaving(PGTestCase):
    
    def test_saving(self):
        
        # generate temporary file
        file1 = NamedTemporaryFile(suffix='file1.pickle')
        file2 = NamedTemporaryFile(suffix='file2.pickle')
        file3 = NamedTemporaryFile(suffix='file3.pickle')
        
        model_spec = '''
        --- model testing_saving
        config file1
        config file2
        config file3
        
        |has_state x=1| --> Y
        
        on init:   load has_state.x from $file1 as pickle 
        on finish: save has_state.x  to  $file2 as pickle
        on finish: save Y  to  $file3 as pickle
        
        '''
        value = 43
        pickle.dump(value, file1)
        file1.flush()
        
        config = {'file1': file1.name, 'file2': file2.name, 'file3': file3.name}
        model = model_from_string(model_spec, config=config)
        
        
        model.reset_execution()
        while model.has_more():       
            model.update()
        model.finish()
        
        value2 = pickle.load(open(file2.name))
        self.assertEqual(value, value2)

        value3 = pickle.load(open(file3.name))
        self.assertEqual(value + 1, value3)
        
        
        # should be like this
        if False:
            model.init()
            while model.update() == model.UPDATE_NOT_FINISHED:       
                pass
            model.finish()
            
        
