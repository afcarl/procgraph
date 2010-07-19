from procgraph.core.model import Model
from unittest import TestCase

class DelayedTest(TestCase):
    
    def test_delayed(self):

        model_desc = """
           |generic out=3| -> |identity| -> |identity| -> |block1:identity|
        """
        model = Model.from_string(model_desc)
        
        block1 = model.name2block['block1']
        self.assertTrue(block1.are_output_signals_defined() )
        
        print block1
        
    def test_check_definitions(self):
        
        model_desc = """ 
            |DoesNotDefineOutput|
        """
        
        self.assertRaises(Exception, Model.from_string, model_desc)
        
        
        model_desc = """ 
            |DoesNotDefineInput|
        """
        
        self.assertRaises(Exception, Model.from_string, model_desc)