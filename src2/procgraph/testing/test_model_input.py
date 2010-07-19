from procgraph.core.model import Model
from procgraph.components.rawseeds import *
from unittest import TestCase

class PipelineTest(TestCase):
    
    def test1(self):

        model_desc = """
           |input name=x| -> |g1:gain| -> |output name=y|
        """
        gain = 3
        model = Model.from_string(model_desc, {'g1.gain': gain})
        
        model.summary()
        
        for i in range(5):
            value  = i
            timestamp = 4 + i * 0.5 
            model.from_outside_set_input('x', value, timestamp=timestamp)
            
            self.assertTrue(model.has_more())
            while model.has_more():
                print "update %s  y = %s" % (i, model.get_output(0) )
                model.update()

            self.assertEqual(model.get_output(0), gain * value)
            self.assertEqual(model.get_output_timestamp(0), timestamp)