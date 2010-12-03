from .utils import PGTestCase


good_examples = [
'''
--- model test

|g1:generic|

on init: load g1 from "g1.mat"  
on finish: save g1 to "g1.mat"
init: load g1 from "g1.mat"  
finish: save g1 to "g1.mat"
init: load g1  "g1.mat"  
finish: save g1  "g1.mat"
finish: save g1  "g1.mat" as matlab
''',
'''
--- model test

|g1:generic|

on init: load g1 from "g1" as matlab
on init: load g1 from "g1" as numpy
on init: load g1 from "g1" as pickle
on init: load g1 from "g1" as numpy_raw
on init: load g1.x from "g1" as numpy_raw

on init: load g1 from $file1

'''
]


bad_examples = [
'''
--- model test

|g1:generic|

on init: load g1 from "g1" as 
'''
]



class SyntaxTest(PGTestCase):
    
    def testBadExamples(self):
        for example in bad_examples:
            self.check_syntax_error(example)
                        
    def testExamples(self):
        for example in good_examples:
            self.check_syntax_ok(example)

