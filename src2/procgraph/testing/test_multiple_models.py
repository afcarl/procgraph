from procgraph.core.model_loader import model_from_string
import unittest
from procgraph.core.parsing import parse_model
import traceback
from procgraph.core.exceptions import SemanticError
from procgraph.testing.utils import PGTestCase

good_examples = [
'''
--- model master

|input name=a| -> |slave1| -> |slave2| -> |output name=b| 

--- model slave1

|input name=x| -> |output name=y|

--- model slave2

|input name=x| -> |output name=y|
''' ,
'''
# recursive models
--- model master

|input name=a| -> |output name=b| 

--- model slave

|input name=x| -> |output name=b|
'''
]

bad_examples = [
                # XXXXXXXXXXXXXXXXX how can it work?
'''
# recursive models
--- model master

|input name=a| -> |slave1| -> |output name=b| 

--- model slave1

|input name=x| -> |slave2| -> |output name=y|

--- model slave2

|input name=x| -> |slave1| -> |output name=y|
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



class SemanticsTest(PGTestCase):
    
    def testExamples(self):
        for example in good_examples:
            model = self.check_semantic_ok(example)
            print model
            
    
    def testBadExamples(self):
        for example in bad_examples:
            self.check_semantic_error(example)
                