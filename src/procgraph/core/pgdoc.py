import sys, os, traceback 
from optparse import OptionParser

from procgraph.core.model_loader import model_from_string, pg_look_for_models, \
    ModelSpec
from procgraph.core.registrar import default_library, Library
from procgraph.core.exceptions import SemanticError, PGSyntaxError 
from procgraph.core.parsing_elements import Where
from procgraph.core.visualization import error
from collections import namedtuple
from procgraph.core.block import Block


# type = 'model', 'block', 'simple_block'
# implementation: either Class or wrapped function
# 'desc' is the first line of a docstring, 'desc_rest' are the remaining lines
type_block = 'block'
type_model = 'model'
type_simple_block = 'simple_block'

ModelDoc = namedtuple('ModelDoc', 'name source module type implementation input '
                      'output config desc desc_rest')
ModelInput = namedtuple('ModelInput', 'name desc desc_rest')
ModelOutput = namedtuple('ModelOutput', 'name desc desc_rest')
ModelConfig = namedtuple('ModelConfig', 'name default desc desc_rest')

def collect_info(block_type, block_generator):
    
    if isinstance(block_generator, ModelSpec):
        parsed_model = block_generator.parsed_model
        type = type_model
        implementation = None
        module = block_generator.defined_in # XXX
        while  module.__doc__ is None:
                module = module.__package__
        source = parsed_model.where.filename
    elif issubclass(block_generator, Block):
        if block_generator.__name__ == 'GenericOperation':
            func = block_generator.my_operation
            type = type_simple_block
            implementation = func
            source = block_generator.defined_in.__file__ # xxx
            module = block_generator.defined_in
            while  module.__doc__ is None:
                module = module.__package__
            #func.__file__
            #print block_type, 'SIMPLE_BLOCK', func, func.__name__, func.__module__
        else:
            type = type_block
            implementation = block_generator
            
            module = __import__(block_generator.__module__, fromlist=['x'])
            source = module.__file__
            while  module.__doc__ is None:
                module = module.__package__
                #print "changing to %s" % str(module)
    else: 
        assert False

    print block_type
    print " - type\t", type
    print " - implementation\t", implementation
    print " - module\t", module
    print " - source\t", source
     
    
    return None

def get_all_info(library):
    for block_type, generator in library.name2block.items():
        yield collect_info(block_type, generator)

def main(): 
    parser = OptionParser()
     
    parser.add_option("--output", default=None, help="HTML output file.")
    
    (options, args) = parser.parse_args()
    
    import procgraph.components
    import bootstrap_experiments_201008
    
    library = default_library
    pg_look_for_models(library)
    
    infos = list(get_all_info(library))
        
    
