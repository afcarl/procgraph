import sys
from procgraph.core.model import Model, create_from_parsing_results
import os
from procgraph.core.exceptions import UserError
import glob
import fnmatch
from procgraph.core.registrar import register_block_class
from procgraph.core.parsing import parse_model, ParsedAssignment
from copy import deepcopy

PATH_ENV_VAR = 'PROCGRAPH_PATH'

def pg_look_for_models(additional_paths=None):
    ''' Call this function at the beginning of the executions.
    It scans the disk for model definitions, and register
    them as available block types. 
    Other than the paths that are passed by argument,
    it looks into the ones in the PROCGRAPH_PATH environment
    variable (colon separated list of paths)
    '''
    paths = []
    if additional_paths:
        paths.extend(additional_paths)
        
    if PATH_ENV_VAR in os.environ:
        paths.extend( os.environ[PATH_ENV_VAR].split(':'))
        
    # enumerate each sub directory
    all_files = set()
    for path in paths:
        if not os.path.isdir(path):
            raise UserError('Invalid path "%s" to search for models. ' % path) 
        
        for root, dirs, files in os.walk(path):
            for f in files: 
                if fnmatch.fnmatch(f, '*.pg'):
                    all_files.append(os.path.join(root, f))
    for f in all_files:
        print "Loading %s" % f
        base,  = os.path.splitext(os.path.basename(f))
        model_spec = open(f).read()
        pg_add_models_to_library(model_spec)

def pg_add_models_to_library(pgfile, name=None):
    models = parse_model(pgfile)
    if models[0].name is None:
        assert name is not None
        models[0].name = name
        
    for model in models:
        pg_add_parsed_model_to_library(model)
    

def pg_add_parsed_model_to_library(parsed_model):
    assert parsed_model.name is not None
    print "Registering model %s " % parsed_model.name
    register_block_class(parsed_model.name, ModelSpec(parsed_model))
    
class ModelSpec():
    ''' Class used to register as a block type '''
    def __init__(self, parsed_model):
        self.parsed_model = parsed_model
        
    def __call__(self, name, properties):
        
        parsed_model = deepcopy(self.parsed_model)
        
        for key, value in properties.items():
            assignment = ParsedAssignment(key,value)
            parsed_model.elements.append(assignment)
        
        model = create_from_parsing_results(parsed_model)

        return model
               
def model_from_string(model_spec, properties = {}):
    ''' Instances a model from a specification. Optional
        attributes can be passed. Returns a Model object. '''
    assert isinstance(model_spec, str)
    assert isinstance(properties, dict)
    
    parsed_models = parse_model(model_spec)
    
    if len(parsed_models) > 0:            
        for support in parsed_models[1:]:
            pg_add_parsed_model_to_library(support)

    parsed_model = parsed_models[0]
    
    # Add the properties passed by argument to the ones parsed in the spec
    for key, value in properties.items():
        assignment = ParsedAssignment(key,value)
        parsed_model.elements.append(assignment)
    
    model = create_from_parsing_results(parsed_model)
    
    return model
   