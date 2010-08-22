import os, fnmatch
import cPickle as pickle

from procgraph.core.model_instantiation import create_from_parsing_results
from procgraph.core.visualization import warning, debug
create_from_parsing_results
from procgraph.core.parsing import parse_model, ParsedModel
from procgraph.core.exceptions import SemanticError
from procgraph.core.registrar import default_library, Library

PATH_ENV_VAR = 'PROCGRAPH_PATH'

class ModelSpec(object):
    ''' Class used to register as a block type '''
    def __init__(self, parsed_model):
        self.parsed_model = parsed_model
        # the module to which this model is associated
        self.defined_in = None
        
    def __call__(self, name, config, library):
        parsed_model = self.parsed_model 
            
        parent = self
        # We create a mock library that forbids that this
        # model is created again. This prevents recursion.
        class ForbidRecursion(Library):
            def __init__(self, parent, forbid):
                Library.__init__(self, parent)
                self.forbid = forbid
                
            def instance(self, block_type, name, config, parent_library=None, where=None):
                if block_type == self.forbid:
                    raise SemanticError('Recursion error for model "%s".' % self.forbid,
                                        parent.parsed_model)
                else:
                    #print "Instancing %s (forbid %s)" % (block_type, self.forbid)
                    return Library.instance(self, block_type, name,
                                            config, parent_library, where)
        sandbox = ForbidRecursion(library, parsed_model.name)     
        model = create_from_parsing_results(parsed_model, name, config, library=sandbox)

        return model


def pg_look_for_models(library, additional_paths=None, ignore_env=False, ignore_cache=False,
                       assign_to_module=None):
    ''' Call this function at the beginning of the executions.
    It scans the disk for model definitions, and register
    them as available block types. 
    Other than the paths that are passed by argument,
    it looks into the ones in the PROCGRAPH_PATH environment
    variable (colon separated list of paths), unless ignore_env is True.
    
    assign_to_module is a string that gives the nominal module the model
    is associated to -- this is only used for the documentation generation. 
    '''
    
    paths = []
    if additional_paths:
        paths.extend(additional_paths)
    
    if not ignore_env:
        if PATH_ENV_VAR in os.environ:
            paths.extend(os.environ[PATH_ENV_VAR].split(':'))
        
    if not paths:
        warning("No paths given and environment var %s not defined." % PATH_ENV_VAR) 
        
    # enumerate each sub directory
    all_files = set()
    for path in paths:
        if not os.path.isdir(path):
            raise Exception('Invalid path "%s" to search for models. ' % path) 
        
        for root, dirs, files in os.walk(path): #@UnusedVariable
            for f in files: 
                if fnmatch.fnmatch(f, '*.pg'):
                    all_files.add(os.path.join(root, f))
                    
        #print "Scanning %s " % path
            
    for f in all_files:
        split = os.path.splitext(os.path.basename(f))
        base = split[0]
        
        cache = os.path.splitext(f)[0] + '.pgc'
        if not ignore_cache and \
            os.path.exists(cache) and \
            os.path.getmtime(cache) > os.path.getmtime(f):
            try:
                models = pickle.load(open(cache))
            except Exception as e:
                raise Exception('Cannot unpickle file %s: %s.' % (cache, e))
            #print "Using cache %s" % cache
        else:
            debug("Parsing %s" % os.path.relpath(f))
            model_spec = open(f).read()
            models = parse_model(model_spec, filename=f)
            pickle.dump(models, open(cache, 'w'))
        
        if models[0].name is None:
            models[0].name = base
    
        for parsed_model in models:
            if library.exists(parsed_model.name):
                prev = library.name2block[parsed_model.name].parsed_model.where
                raise SemanticError('Found model "%s" in %s, already in  %s. ' % \
                            (parsed_model.name, f, prev.filename))
            model_spec = ModelSpec(parsed_model)
            model_spec.defined_in = assign_to_module
            library.register(parsed_model.name, model_spec)

  
def pg_add_parsed_model_to_library(parsed_model, library, defined_in=None):
    assert parsed_model.name is not None
    if library.exists(parsed_model.name):
        prev = library.name2block[parsed_model.name].parsed_model.where
        raise SemanticError('I already have registered "%s" from %s. ' % \
                            (parsed_model.name, prev.filename))
    # print "Registering model '%s' " % parsed_model.name

    model_spec = ModelSpec(parsed_model)
    model_spec.defined_in = defined_in    
    assert defined_in is not None
    library.register(parsed_model.name, model_spec)


def add_models_to_library(library, string, name=None, filename=None, defined_in=None):
    '''
    defined_in: module to display in documentation
    '''
    if filename is None and defined_in is not None:
        filename = defined_in.__file__
    
    models = parse_model(string, filename=filename)
    if models[0].name is None:
        assert name is not None
        models[0].name = name
        
    for model in models:
        pg_add_parsed_model_to_library(parsed_model=model, library=library,
                                       defined_in=defined_in)
        
               
def model_from_string(model_spec, name=None, config=None, library=None, filename=None):
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
   
