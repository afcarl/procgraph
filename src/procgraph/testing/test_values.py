from .utils import PGTestCase

from procgraph.core.parsing import parse_value
import unittest

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

        """{ indices: [0,170] }""": { 'indices': [0, 170]},

        """{ indices: [0,170], theta: [-1,+1], color: 'r', \
            origin: [0,0,0],  max_readings: 5}""":
{ 'indices': [0, 170], 'theta': [-1, +1], 'color': 'r',
      'origin': [0, 0, 0], 'max_readings': 5},

#}
#
#examples_known_failing = {
"""[{ indices: [0,170], theta: [-1,+1], color: 'r', \
      origin: [0,0,0],  max_readings: 5}, { indices: [171,341], \
        theta: [+1,+5], color: 'b', origin: [0,0,0], max_readings: 5}]""":
[{ 'indices': [0, 170], 'theta': [-1, +1], 'color': 'r',
      'origin': [0, 0, 0], 'max_readings': 5},
{ 'indices': [171, 341],
        'theta': [+1, +5], 'color': 'b', 'origin': [0, 0, 0], 'max_readings': 5}]

}



class SyntaxTest2(PGTestCase):
                        
    def testExamples(self):
        for example, expected in examples.items():
            print "Trying '%s'" % example
            found = parse_value(example)
            
            ok = (found == expected) or (str(found) == str(expected))
            
            if not ok:
                raise Exception('From:\n%s\ngot:\n%s\ninstead of\n%s' % \
                                (example, found, expected))

#    if 1:
#        #@unittest.expectedFailure
#        def testExamplesKnownToFail(self):
#            for example, expected in examples_known_failing.items():
#                print "Trying '%s'" % example
#                found = parse_value(example)
#                
#                ok = (found == expected) or (str(found) == str(expected))
#                
#                if not ok:
#                    raise Exception('From:\n%s\ngot:\n%s\ninstead of\n%s' % \
#                                    (example, found, expected))
