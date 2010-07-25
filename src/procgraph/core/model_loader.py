from procgraph.core.model import  create_from_parsing_results
import os
import fnmatch
from procgraph.core.parsing import parse_model, ParsedModel
from procgraph.core.exceptions import SemanticError
from procgraph.core.registrar import default_library, Library

PATH_ENV_VAR = 'PROCGRAPH_PATH'

class ModelSpec():
    ''' Class used to register as a block type '''
    def __init__(self, parsed_model):
        self.parsed_model = parsed_model
        
    def __call__(self, name, config, library):
        parsed_model = self.parsed_model 
            
        # We create a mock library that forbids that this
        # model is created again. This prevents recursion.
        class ForbidRecursion(Library):
            def __init__(self, parent, forbid):
                Library.__init__(self, parent)
                self.forbid = forbid
                
            def instance(self, block_type, name, config, parent_library=None):
                if block_type == self.forbid:
                    raise SemanticError('Recursion error for model "%s".' % self.forbid)
                else:
                    #print "Instancing %s (forbid %s)" % (block_type, self.forbid)
                    return Library.instance(self, block_type, name, 
                                            config,parent_library)
        sandbox = ForbidRecursion(library, parsed_model.name)     
        model = create_from_parsing_results(parsed_model, name, config, library=sandbox)

        return model

def pg_look_for_models(library, additional_paths=None):
    ''' Call this function at the beginning of the executions.
    It scans the disk for model definitions, and register
    them as available block types. 
    Other than the paths that are passed by argument,
    it looks into the ones in the PROCGRAPH_PATH environment
    variable (colon separated list of paths)
    '''
    def __add_models_to_library(library,pgfile, name=None):
        models = parse_model(pgfile,filename=pgfile)
        if models[0].name is None:
            assert name is not None
            models[0].name = name
            
        for model in models:
            pg_add_parsed_model_to_library(parsed_model=model, library=library)

    
    paths = []
    if additional_paths:
        paths.extend(additional_paths)
        
    if PATH_ENV_VAR in os.environ:
        paths.extend( os.environ[PATH_ENV_VAR].split(':'))
        
    if not paths:
        print "No paths given and environment var %s not defined." % PATH_ENV_VAR 
        
    # enumerate each sub directory
    all_files = set()
    for path in paths:
        if not os.path.isdir(path):
            raise Exception('Invalid path "%s" to search for models. ' % path) 
        
        for root, dirs, files in os.walk(path): #@UnusedVariable
            for f in files: 
                if fnmatch.fnmatch(f, '*.pg'):
                    all_files.add(os.path.join(root, f))
                    
        print "Scanning %s " % path
            
    for f in all_files:
        print "Loading %s" % f
        split = os.path.splitext(os.path.basename(f))
        base = split[0]
        model_spec = open(f).read()
        __add_models_to_library(library, model_spec, base)

  
def pg_add_parsed_model_to_library(parsed_model, library):
    assert parsed_model.name is not None
    if library.exists(parsed_model.name):
        raise SemanticError('I already have registered "%s". '%parsed_model.name)
    # print "Registering model '%s' " % parsed_model.name
    
    library.register(parsed_model.name, ModelSpec(parsed_model))

               
def model_from_string(model_spec, name=None, config = None, library=None, filename=None):
    ''' Instances a model from a specification. Optional
        attributes can be passed. Returns a Model object. '''
    if config is None:
        config = {}
    if library is None:
        library = default_library
    assert isinstance(model_spec, str)
    assert isinstance(config, dict)
    assert name is None or isinstance(name, str)
    
    parsed_models = parse_model(model_spec, filename)

    assert isinstance(parsed_models, list)
    for x in parsed_models:
        assert isinstance(x, ParsedModel)
    
    if len(parsed_models) > 0:            
        for support in parsed_models[1:]:
            pg_add_parsed_model_to_library(support, library)

    parsed_model = parsed_models[0]
    
    model = create_from_parsing_results(parsed_model, name=name, 
                                        config=config, library=library)
    
    return model
   