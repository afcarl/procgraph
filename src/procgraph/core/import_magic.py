import sys
from .visualization import info
from types import ModuleType

# TODO: move somewhere else
sname = 'procgraph_info'  
fname = 'requires'
REQUIRES_PARSED = 'requires_parsed'
    
def import_magic(module_name, required, member=None):
    ''' Equivalent to "from required import member" or "import required". '''
    info_structure = get_module_info(module_name)
    # Check that it was mentioned in the structure
    required_base = required.split('.')[0]
    if not required_base in info_structure[REQUIRES_PARSED]:
        raise Exception('Please specify that you need %r as a dependency '
                        'in the field %r of the %r structure in module %r.' % 
                        (required_base, fname, sname, module_name))
    
    # FIXME: there's a bug in here, should find which base was selected
    if required == required_base:
        options = info_structure[REQUIRES_PARSED][required]
    else:
        options = [required]
    
    for o in options:
        try:
            mod = __import__(o, fromlist=['dummy'])
            if member is not None:
                if not member in mod.__dict__:
                    raise Exception('No member %r in %r' % (member, o))
                return mod.__dict__[member]
            return mod
        except Exception as e:
            # could not load it!
            # TODO: show error
            print e
            pass
        
    # We could not load anything.
    info('Could not load dependency %r for %r. '
          'I will let you continue, but an error might be thrown when the package '
          'actually tries to use it.' % 
          (required, module_name))
    
    msg = 'I tried to let you continue, but it seems that module %r really needs ' \
          '%r to work. Sorry! ' % (module_name, required)
        
    class warn_and_throw:
        def __getattr__(self, method_name): #@UnusedVariable
            raise Exception(msg)
        
    return warn_and_throw()    
    
def get_module_info(module_name):
    # TODO: better Exception?
    if not module_name in sys.modules:
        raise Exception('Please pass the module __name__ (got: %r).' % module_name)

    module = sys.modules[module_name]
    
    if not sname in module.__dict__:
        raise Exception('Please define the structure %r for module %r '
                        'before you call import_magic().' % (sname, module_name)) 

    info = module.__dict__[sname] 
    
    ''' Returns dict   name -> list of possible modules '''
    parsed = {}
    if not fname in info:
        #raise Exception('Please define a field %r in dict %s.%s.' % 
        #                (fname, module_name, sname))
        pass
    else:
        requires = info[fname]
        for r in requires:
            if isinstance(r, str):
                # normal
                parsed[r] = [r]
            else:
                # TODO: check iterable
                name = r[0]
                options = list(r[1])
                # TODO: check options > 0
                parsed[name] = options

    info[REQUIRES_PARSED] = parsed
        
    return info

            
def import_succesful(m):
    return isinstance(m, ModuleType)
            

