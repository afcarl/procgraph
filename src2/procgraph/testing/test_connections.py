
import unittest
import traceback
from pyparsing import ParseException
from procgraph.core.model import create_from_parsing_results, Model
import procgraph.components.basic 
import procgraph.components.debug_components 
from procgraph.core.parsing import parse_model
from procgraph.core.model_loader import model_from_string


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
|constant value=12| -> [0]a[0] -> |gain|  """,

""" # A block by itself should be fine  
|generic in=0 out=0|  
|generic in=0 out=2|  """,
 
""" # Trying some named connections (1)  
|generic out=1| -> |generic in=1|  """,

""" # Trying some named connections (1)
# Should be the same  
|generic out=1| -> x
x -> |generic in=1|  """,

"""# Should be the same  as well
|c1:constant value=1| -> |g1:generic in=1 out=1|
g1.0 -> |g2:generic in=1|  """,

"""# Should be the same  as well
|g1:generic out=1|
g1.0 -> |g2:generic in=1|  """,

"""# Checking if the parameters are parsed ok.
# without it would be illegal   
|constant value=1| -> |g1:generic|
g1.in = 1
"""

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
|constant value=12| -> [0]a[0]  """,

""" # Incompatible signals (anonymous) 
|constant value=12| -> |generic in=2 out=1| -> y """,

""" # We don't want to connect blocks with no signals  
|generic in=0 out=0| -> |generic in=0 out=2|  """,
 
""" # It cannot be without input if one is needed   
|generic in=1 out=0|  """,
 
""" # Double definition   
|generic out=1| -> a  
|generic out=1| -> a""",


""" # Oops, definition is left dangling...   
|generic out=1| -> a  
|generic out=1| -> a
g1.in = 2
""",

]


class SemanticsTest(unittest.TestCase):
    
    def testBadExamples(self):
        for example in bad_examples2:
            #print 'trying """%s"""' % example
            parsed = parse_model(example)
            failed = False
            self.assertTrue( len(parsed) == 1)
            try:
                model = create_from_parsing_results(parsed[0])
                print "OOPS, we parsed something from:\n'%s'\n" % example
                print parsed 
                model.summary()
            except:
                failed = True
                
            if not failed:
                self.assertTrue(False)
            
            
    def testExamples(self):
        failed = None
        for example in good_examples2:
            
            # print "E   '''%s'''" % example
            
            try:
                parsed = parse_model(example)
                self.assertTrue( len(parsed) == 1)
                model = create_from_parsing_results(parsed[0])
                #model.summary()
                
#                print "      %s" % res.__repr__()
            except Exception as e:
                print 'Failed  """%s"""\n' % example
                print "Error: %s " % e
                traceback.print_exc()
                failed = example
                raise e
                
        if failed is not None:
            raise Exception('Failed "%s".' % failed)
            
    def test_from_string_params(self):
        spec = '|constant value=1| -> |g1:generic|'
        # this should not work
        self.assertRaises(Exception, model_from_string, spec)
        # this should, instead
        model_from_string(spec, {'g1.in': 1})
        
    
    
class ParamsTest(unittest.TestCase):
    
    def test1(self):
        ''' Checking that we signal unused parameters. '''

        model_desc = """
           |input name=x| -> |g1:gain| -> |output name=y|
        """
        # g2.gain is unused
        self.assertRaises(Exception, model_from_string,
                     model_desc, {'g2.gain': 2})
       
    
    