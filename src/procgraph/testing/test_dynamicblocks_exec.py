from procgraph.core.block import Block
from procgraph.core.registrar import default_library
from procgraph.testing.utils import PGTestCase
from procgraph.core.exceptions import SemanticError
 
good_examples = [
"""
type = generic

|$type in=0 out=1| --> X
""",
"""
type = gen

|"${type}eric" in=0 out=1| --> X
"""

            
]
     
     
bad_examples = [

"""

|"${type}" in=0 out=1| --> X
"""
                
]   
    

class DynamicBlocksTest(PGTestCase):
    
    def testGoodExamples(self):
        for example in good_examples:
            self.check_semantic_ok(example)
                        
    def testBadExamples(self):
        for example in bad_examples:
            self.check_semantic_error(example)
