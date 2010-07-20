from procgraph.core.model_loader import model_from_string
import unittest
from procgraph.core.parsing import parse_model
import traceback
from procgraph.core.exceptions import SemanticError

good_examples = [
'''
--- model master

|input name=a| -> |slave1| -> |slave2| -> |output name=b| 

--- model slave1

|input name=x| -> |output name=y|

--- model slave2

|input name=x| -> |output name=y|
''' 
]

bad_examples = [
'''
# recursive models
--- model master

|input name=a| -> |slave| -> |output name=b| 

--- model slave

|input name=x| -> |master| -> |output name=y|
'''             ,

'''
# same name should throw an error
--- model master

|input name=a| -> |slave| -> |output name=b| 

--- model slave

|input name=x|   -> |output name=y|

--- model slave

|input name=x|  -> |output name=y|
'''             

                
                
]



class SemanticsTest(unittest.TestCase):
    
    def testExamples(self):
        failed = None
        for example in good_examples:
            
            try:
                model = model_from_string(example)
            except Exception as e:
                print 'Failed  """%s"""\n' % example
                print "Error: %s " % e
                traceback.print_exc()
                failed = example
                raise e
                
        if failed is not None:
            raise Exception('Failed "%s".' % failed)
            
    
    def testBadExamples(self):
        for example in bad_examples:
            # make sure we can parse it
            parsed = parse_model(example)
            
            failed = False
            try:
                # try again
                model = model_from_string(example)
                print "OOPS, we parsed something from:\n'%s'\n" % example
                print parsed 
                model.summary()
            except SemanticError as e:
                failed = True
                print "OK, failed with error %s" % e
                 
            if not failed:
                self.assertTrue(False)
            
                
                