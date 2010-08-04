from procgraph.core.block import Block
from procgraph.core.registrar import default_library
from procgraph.testing.utils import PGTestCase
from procgraph.core.exceptions import SemanticError

class VerifyBlock(Block):
    ''' 
        This debug block verifies that config.x == config.y 
        and throws an exception if that's not the case.
    '''
        
    def init(self):
        if self.config.x != self.config.y:
            raise SemanticError('Oops: "%s" != "%s".' % \
                                (self.config.x, self.config.y), self)
        self.define_input_signals([])
        self.define_output_signals([])
        
default_library.register('verify',  VerifyBlock)


good_examples = [
'|verify  x="a" y="a"|',
'''
var=value
|verify  x=$var y="value"|''',
'''
var=value
|verify  x="${var}" y="value"|''',
'''
var=value
|verify  x="${var}" y=$var|''',
'''
var1=value
var2=$var1
|verify  x="${var2}" y="value"|''',
'''
var1=value
var2=$var1
|verify  x="1${var2}2" y="1value2"|''',
'''
var1=value
|verify  x={a: $var1} y={a: value}|''',
'''
var1=value
|verify  x=[$var1] y=[value]|''',


            
]
     
     
bad_examples = [
'|verify  x="b" y="a"|',

# Recursive cases
'''
    one = $one
''',
'''
    one = "$one"
''',
'''
    one = $two
    two = $one
''',
'''
    one = "${two}"
    two = $one
''',
'''
    two = $one
    one = "${two}"
''',
'''
    one = "${two}"
    two = "${one}"
''' 
                
]   
    

class SubstitutionTest(PGTestCase):
    
    def testGoodExamples(self):
        for example in good_examples:
            self.check_semantic_ok(example)
                        
    def testBadExamples(self):
        for example in bad_examples:
            self.check_semantic_error(example)
