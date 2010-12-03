from .utils import PGTestCase

good_examples = [
('''
--- model master
config  a      "well documented param"
config  b = 3  "well documented param"

|verify x=$a y=$b|
''', {'a': 3, 'b': 3}),
('''
--- model master
config  a      "well documented param"
config  b = 3  "well documented param"

|verify x=$a y=$b|
''', {'a': 3}) 
]

bad_examples = [
('''
# a is not assigned
--- model master
config  a      "well documented param"
config  b = 3  "well documented param"

|verify x=$a y=$b|
''', { 'b': 3}),
('''
# double description
--- model master
config  a      "well documented param"
config  a      "well documented param"

b=2
''', {}),
('''
# overwriting configuration
--- model master
config  a      "well documented param"

a=2
''', {}) 

]



class SemanticsTest(PGTestCase):
    
    def testExamples(self):
        for example, config in good_examples:
            self.check_semantic_ok(example, config=config)
            
    
    def testBadExamples(self):
        for example, config in bad_examples:
            self.check_semantic_error(example, config=config)
                
