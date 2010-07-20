import unittest
from procgraph.core.model_loader import model_from_string
from procgraph.core.parsing import parse_model
from procgraph.core.exceptions import SemanticError


class PGTestCase(unittest.TestCase):
    
    def check_syntax_ok(self, model_spec):
        ''' Tests that the given string can parse OK. Returns parsed models. '''
        parsed = parse_model(model_spec)

    
    def check_semantics_ok(self, model_spec):
        ''' Tests that the given string can parse OK and we can create a model.
            Note that a syntax error is translated into a test Error, not failure.
            '''
        model = model_from_string(model_spec)

    def check_syntax_error(self, model_spec):
        ''' Tests that the given string parsing gives a syntax error. '''
        failed = False
        try:
            parsed = parse_model(model_spec)
            print "OOPS, we could parse '''%s'''" % model_spec
            print parsed
        except SyntaxError:
            failed = True
        
        if not failed:
            self.assertTrue(False)

    def check_semantics_error(self, model_spec):
        ''' Tests that the given string parses ok but gives a
            semantic error. '''
        # make sure we can parse it
        parsed = parse_model(model_spec)
        
        failed = False
        try:
            # try again
            model = model_from_string(model_spec)
            print "OOPS, we could interpret '''%s'''" % model_spec
            print parsed 
            model.summary()
        except SemanticError as e:
            failed = True
            print "OK, failed with error %s" % e
             
        if not failed:
            self.assertTrue(False)
    