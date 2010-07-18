
import unittest
from procgraph.parsing.model_parsing import parse_model
import traceback
from pyparsing import ParseException
from procgraph.core.model import create_from_parsing_results
import procgraph.components.Components 

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
"""
]



bad_examples = [
"u = -1a",
"|GENERATOR| --> result resu",
"|GENERATOR GENERATOR| --> result resu",
"result x --> |SINK|",
"u -> |FUNCTION| |FUNCTION| --> result"]



class SyntaxTest(unittest.TestCase):
    
    def testBadExamples(self):
        for example in bad_examples:
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
            


good_examples2 = [
""" |rand| -> [0] res """,

""" # Multiple inputs
|constant value=12| -> a
|constant value=13| -> b
a, b -> |+| -> c  """,

""" # Multiple inputs / anonymous
|constant value=12| -> a -> |gain value=3| -> c
|constant value=13| -> |gain value=-1| -> d
 c, d -> |+| -> result         """,

""" # Referring to outputs using numbers  
|constant value=12| -> [0]a  """, 

""" # Referring to input/outputs using numbers  
|constant value=12| -> [0]a[0] -> |gain|  """ 

]

bad_examples2 = [
""" # Bad number of outputs  
|constant value=12| -> a, b  """, 

""" # Bad output name  
|constant value=12| -> [inexistent]a  """, 

""" # Bad output number  
|constant value=12| -> [1]a  """, 

""" # inexistent input
invalid -> |gain|            """,

""" # input to something with no input
|constant value=12| -> a
a -> |constant value=12|   """,

""" # wrong number of inputs
|constant value=12| -> a
|constant value=12| -> b
a, b -> |gain|              """,

""" # Cannot use output if terminating  
|constant value=12| -> [0]a[0]  """ 


]


class SemanticsTest(unittest.TestCase):
    
    def testBadExamples(self):
        for example in bad_examples2:
            #print 'trying """%s"""' % example
            parsed = parse_model(example)
            failed = False
            try:
                model = create_from_parsing_results(parsed)
                print "OOPS, we parsed something"
                model.summary()
            except:
                failed = True
                
            if not failed:
                self.assertTrue(False)
            
            
    def testExamples(self):
        failed = None
        for example in good_examples2:
            
            try:
                parsed = parse_model(example)
                model = create_from_parsing_results(parsed)
                #model.summary()
                #print "v   %s" % example
#                print "      %s" % res.__repr__()
            except Exception as e:
                print 'Failed  """%s"""\n' % example
                print "Error: %s " % e
                traceback.print_exc()
                failed = example
                raise e
                
        if failed is not None:
            raise Exception('Failed "%s".' % failed)
            
            