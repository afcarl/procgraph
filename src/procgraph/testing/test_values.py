from procgraph.testing.utils import PGTestCase
from procgraph.core.parsing import parse_value


examples = { \
            '[]': [],
            '[1]': [1],
            '[1,2]': [1, 2],
            '[1,[2]]': [1, [2]],
            '[[]]': [[]],
            '[{}]': [{}],
            '{}': {},
            '[{a:0}]': [{'a':0}],
            # XXX 
            #'{a:[]}': {"a":[]},
            '{a:0}': {'a':0},
            '{a:0,b:1}': {'a':0, 'b':1},
            '{a:b}': {'a':'b'},
            '{a:{b:c}}': {'a':{'b':'c'}},
}



class SyntaxTest2(PGTestCase):
                        
    def testExamples(self):
        for example, expected in examples.items():
            print "Trying '%s'" % example
            found = parse_value(example)
            
            ok = (found == expected) or (str(found) == str(expected))
            
            if not ok:
                raise Exception('From "%s" got %s instead of %s.' % \
                                (example, found, expected))
            
