import unittest
from procgraph.core.model_loader import model_from_string
from procgraph.core.parsing import parse_model
from procgraph.core.exceptions import SemanticError
from procgraph.core.registrar import default_library, Library
import traceback


class PGTestCase(unittest.TestCase):
    
    def check_syntax_ok(self, model_spec):
        ''' Tests that the given string can parse OK. Returns parsed models. '''
        parsed = parse_model(model_spec)

    
    def check_semantic_ok(self, model_spec):
        ''' Tests that the given string can parse OK and we can create a model.
            Note that a syntax error is translated into a test Error, not failure.
            '''
            
        library = Library(parent = default_library)
        
        try:
            model = model_from_string(model_spec, library=library)
            return model
        except SemanticError as e:
            print "Oops, seems like we had an error for '''%s'''" % model_spec
            traceback.print_exc()
            raise e
         
            

    def check_syntax_error(self, model_spec):
        ''' Tests that the given string parsing gives a syntax error. '''
        failed = False
        try:
            parsed = parse_model(model_spec)
            print "OOPS, we could parse '''%s'''" % model_spec
            print parsed
        except SyntaxError as e:
            print "OK, syntax failed with error:  %s" % e
            failed = True
        
        if not failed:
            self.assertTrue(False)

    def check_semantic_error(self, model_spec):
        ''' Tests that the given string parses ok but gives a
            semantic error. '''
        # make sure we can parse it
        parsed = parse_model(model_spec)
        
        failed = False
        try:
            # try again
            library = Library(parent = default_library)
            model = model_from_string(model_spec, library=library)
            print "OOPS, we could interpret '''%s'''" % model_spec
            print parsed 
            model.summary()
        except SemanticError as e:
            failed = True
            print "OK, semantics failed with error:  %s" % e
             
        if not failed:
            self.assertTrue(False)
    