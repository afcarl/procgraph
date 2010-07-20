import sys
from procgraph.core.model import Model
import os
from procgraph.core.exceptions import UserError
import glob
import fnmatch
from procgraph.core.registrar import register_block_class

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
        pg_add_to_library(open(f).read())
        
def pg_add_to_library(model_spec, model_name=None):
    ''' Adds a model, or models to the library.
    model_spec might be either:
    1) the spec for a model, in which case a model_name should be given
    2) the spec for multiple models, in which case a model_name should not be given
    '''
    contains_multiple_models, name2spec = try_parse_multiple_models(model_spec)
    
    if contains_multiple_models and model_name is not None:
        raise UserError('The spec you gave contains multiple models, '+
                        ' name "%s" not necessary ' % model_name)
        
    if not contains_multiple_models and model_name is None:
        raise UserError('I need a name for the model.')
    
    if not contains_multiple_models:
        name2spec = {model_name: model_spec}
        
    for name, spec in name2spec.items():
        register_block_class(name, ModelSpec(spec))

def try_parse_multiple_models(s): 
    """    
    Pass a string to this method and it will look whether it is composed
    by multiple models. Multiple models look like this::
    
        --- model <model name>
        
        model content
        
        --- model <model name>
        
        other 
        
    Returns (boolean, hash) tuple """
    pass

class ModelSpec():
    ''' Class used to register as a block type '''
    def __init__(self, model_spec):
        self.model_spec = model_spec
        
    def __call__(self, name, properties):
        return Model.from_string(self.model_spec, properties)
