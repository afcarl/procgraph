
import unittest
from procgraph.parsing.model_parsing import parse_model
import traceback
from pyparsing import ParseException
from procgraph.core.model import create_from_parsing_results
import procgraph.components.basic 
import procgraph.components.debug_components 

good_examples = [
"u = -1",
"|GENERATOR| --> result",
"result --> |SINK|",
"u -> |FUNCTION| --> result",
"u ,v -> |FUNCTION| --> result, d",
"u -> |opa:FUNCTION| ->  result",
"u --> |op1:FUNCTION op=tan| -> result",
"u -> |FUNCTION| -> |FUNCTION2| -> result",
"u -> |FUNCTION| -> a -> |FUNCTION2| -> result",
"u -> |FUNCTION| -> a -> |FUNCTION2| -> |FUNCTION2| -> result",
"u -> |FUNCTION| -> a -> |FUNCTION2| ---> a,d --> |FUNCTION2| -> result",
"""  |origin| -> a  -> |block| """,
""" |constant value=12| -> [0] a  -> |block| """,
"u = 1",
"""u = 1
u = 2
u =3 """, """u = 2
x -> |func2| -> res3""",
"""x -> |func2| 
u = 2""",
"""

x -> |func2| 

u = 2

""",
" a -> |block| ",
" a[o] -> |block| ",
" a.s[o] -> |block| ",
" [i]a -> |block| ",
" [i]a[d] -> |block| ",
" [i]a[d], b -> |block| ",
" [i]a[d], b[c] -> |block| ",
" b1.f [input_name] -> |test| -> [t] y [U], z [t] -> |test| -> res",
""" 
b1.f [input_name] -> |test| -> [t] y [U], z [t] -> |test| -> res
""",
"""
# this is a comment
u = 1
""",
" |generic in=0,out=2|  ",
" |generic in=0 out=2|  ",
# assignment with object
""" 
g1.in = 2
""", 

]



bad_examples = [
"u = -1a",
"|GENERATOR| --> result resu",
"|GENERATOR GENERATOR| --> result resu",
"result x --> |SINK|",
"u -> |FUNCTION| |FUNCTION| --> result",
# invalid names
".u = 2",
".u.d = 2",
"1u = 2"

]



class SyntaxTest(unittest.TestCase):
    
    def testBadExamples(self):
        for example in bad_examples:
            print ": %s" % example
            self.assertRaises( ParseException, parse_model, example)
            
            
    def testExamples(self):
        failed = None
        for example in good_examples:
            
            try:
                res = parse_model(example)
                #print list(res)
                #print "v   %s" % example
#                print "      %s" % res.__repr__()
            except Exception as e:
                print "X   %s" % example
                print "Error: %s " % e
                traceback.print_exc()
                failed = example
                
        if failed is not None:
            raise Exception('Failed "%s".' % failed)
            
     