import unittest
import traceback

from procgraph.core.model_loader import model_from_string
from procgraph.core.parsing import parse_model
from procgraph.core.exceptions import SemanticError, PGSyntaxError
from procgraph.core.registrar import default_library, Library

# load standard components
import procgraph.components
from procgraph.core.block import Block
from procgraph.core.block_meta import block_alias, block_output_is_variable, \
    block_input_is_variable

# a couple of blocks for testing
#
#
#class DoesNotDefineInput(Block):
#    ''' This (erroneous) block does not register inputs '''
#    
#    def init(self):
#        self.define_output_signals([])
#    
#
#
#class DoesNotDefineOutput(Block):
#    ''' This (erroneous) block does not register output '''
#    
#    def init(self):
#        self.define_input_signals([])
        


class Generic(Block):
    ''' This is a generic block used mainly for debug.
        It defines inputs and outputs given by the parameters
        "in" and "out". 
        
        Parameters:
        * ``in`` (default: ``0``)
        * ``out`` (default: ``0``)  
        
        For example::
    
            A,B,C -> |generic in=3 out=5| -> a,b,c,d,e
            
            # all by itself
            |generic|
            
    '''
    block_alias('generic')
     
    
    def init(self):
        # use default if not set
        self.set_config_default('in', 0)
        self.set_config_default('out', 0)
        
        nin = self.get_config('in')
        nout = self.get_config('out')
        self.define_input_signals(map(str, range(nin)))
        self.define_output_signals(map(str, range(nout)))




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
    
    def init(self):
        if self.config.x != self.config.y:
            raise SemanticError('Oops: "%s" != "%s".' % \
                                (self.config.x, self.config.y), self)
        self.define_input_signals([])
        self.define_output_signals([]) 
