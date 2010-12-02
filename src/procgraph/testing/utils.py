import unittest
import traceback

from procgraph.core.model_loader import model_from_string
from procgraph.core.parsing import parse_model
from procgraph.core.exceptions import SemanticError, PGSyntaxError
from procgraph.core.registrar import default_library, Library

# load standard components
import procgraph.components #@UnusedImport
from procgraph.core.block import Block 
 

def define_generic(nin, nout):
    class Generic(Block):
        Block.alias('generic_in%d_out%d' % (nin, nout))
        for i in range(nin):
            Block.input(str(i))
        for i in range(nout):
            Block.output(str(i))
         

for nin in range(0, 6):
    for nout in range(0, 6):
        define_generic(nin, nout)



class PGTestCase(unittest.TestCase):
    
    def check_syntax_ok(self, model_spec):
        ''' Tests that the given string can parse OK. Returns parsed models. '''
        try:
            parsed = parse_model(model_spec)
            return parsed
        except Exception as e:
            print "Oops, seems like we had an error for '''%s'''" % model_spec
            traceback.print_exc()
            raise e
        
    def check_semantic_ok(self, model_spec, config={}):
        ''' Tests that the given string can parse OK and we can create a model.
            Note that a syntax error is translated into a test Error, not failure.
            '''
        # Don't pollute the main library with unit tests    
        library = Library(parent=default_library)
        
        try:
            model = model_from_string(model_spec, config=config, library=library)
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
        except PGSyntaxError as e:
            print "OK, syntax failed with error:  %s" % e
            failed = True
        
        if not failed:
            raise Exception('This was assumed to fail: \n"""%s"""' % model_spec)
            self.assertTrue(False)

    def check_semantic_error(self, model_spec, config={}):
        ''' Tests that the given string parses ok but gives a
            semantic error. '''
        # make sure we can parse it
        parsed = parse_model(model_spec)
        
        failed = False
        try:
            # try again
            library = Library(parent=default_library)
            model = model_from_string(model_spec, config=config, library=library)
            print "OOPS, we could interpret '''%s'''" % model_spec
            print parsed 
            model.summary()
        except SemanticError as e:
            failed = True
            print "OK, semantics failed with error:  %s" % e
             
        if not failed:
            self.assertTrue(False)
    

class VerifyBlock(Block):
    ''' 
        This debug block verifies that config.x == config.y 
        and throws an exception if that's not the case.
    '''
    
    Block.alias('verify')
    
    Block.config('x')
    Block.config('y')
    
    def init(self):
        if self.config.x != self.config.y:
            raise SemanticError('Oops: "%s" != "%s".' % \
                                (self.config.x, self.config.y), self)
        
