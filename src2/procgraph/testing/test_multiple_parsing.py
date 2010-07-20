
import unittest
import traceback
from pyparsing import ParseException
from procgraph.core.model import create_from_parsing_results
import procgraph.components.basic 
import procgraph.components.debug_components 
from procgraph.core.parsing import parse_model

good_examples = \
[
"""--- model ciao
y = 2
""",
"""------ model ciao
y = 2
""",
"""
--- model ciao
y = 2
--- model belle
y = 2
""",

"""

--- model ciao

y = 2

--- model belle
y = 2


""",
"""
# comments at the beginning should not start a model
--- model belle
e = 2
""",
"""
# spacing 
---   model   belle
e = 2
"""

]

bad_examples = \
[

"""
# Mixing

y = 2

--- model belle
y = 2
""",
"""
# Empty
--- model belle

--- model belle
y = 2
""",

"""
# incomplete
--- model belle
e = 2
--- model belle

""",

"""
# bad name
--- model 1belle
e = 2
""",
"""
# bad syntax
-- model 1belle
e = 2
""",

"""
# should be on the same line 
---   model  
belle
e = 2
"""

]
          
 



class SyntaxTestMultiple(unittest.TestCase):
    
    def testBadExamples(self):
        for example in bad_examples:
            failed = False
            try:
                parsed = parse_model(example)
                print 'Oops, I parsed "%s" into "%s".' % (example, parsed)
            except: 
                failed = True
                
            if not failed:
                self.assertTrue(False)
            
            
    def testExamples(self):
        failed = None
        for example in good_examples:
            
            try:
                res = parse_model(example)
                #print list(res)
                print "v   '''%s'''" % example
#                print "      %s" % res.__repr__()
            except Exception as e:
                print "X   %s" % example
                print "Error: %s " % e
                traceback.print_exc()
                failed = example
                
        if failed is not None:
            raise Exception('Failed "%s".' % failed)
            
