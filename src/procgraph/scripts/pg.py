import sys, os 
from optparse import OptionParser

from ..core.model_loader import model_from_string, pg_look_for_models
from ..core.registrar import default_library, Library
from ..core.exceptions import PGException, SemanticError
from ..core.visualization import error, info
from ..core.constants import PATH_ENV_VAR

usage_short = \
"""Usage:    
        
    pg [options]  <model>.pg   [param=value  param=value ... ]
    
Type "pg --help" for all the options and a few examples.

"""
usage_long = \
"""Usage:    
        
    pg [options]  <model>.pg   [param=value  param=value ... ]
    
Examples:

1) Execute a model that does not need parameters:
    
    $ pg  my_model.pg

2) Execute a model, reading the a directory for additional models:

    $ pg -d my_models/  my_model

   (Note that the current directory is not ready by default).    
   There is also an environment variable that has the same effect:

    $ export {PATH_ENV_VAR}=my_models

3) Execute a model, but first load a module that might contain additional block
   definitions.

    $ pg -m my_blocks  my_model.pg      """.format(PATH_ENV_VAR=PATH_ENV_VAR)
    
    

def main(): 
    parser = OptionParser(usage=usage_long)

    additional_modules = []
    def load_module(option, opt_str, value, parser): #@UnusedVariable
        #info('Importing module %s' % value)
        additional_modules.append(value)
        #__import__(value)
    
    additional_directories = []
    def add_directory(option, opt_str, value, parser): #@UnusedVariable
        additional_directories.append(value)
    
    parser.add_option("-m", dest="module",
                  action="callback", callback=load_module,
                  type="string", help='Loads the specified module')

    parser.add_option("-d", dest='directory', type="string",
                      action="callback", callback=add_directory,
                      help='Additional directory to search for models.')

    parser.add_option("--debug", action="store_true",
                      default=False, dest="debug",
                      help="Displays debug information on the model.")

    parser.add_option("--trace", action="store_true",
                      default=False, dest="trace",
                      help="If true, try to display raw stack trace in case of "
                           " error, instead of the usual friendly message.")
    
    parser.add_option("--stats", action="store_true",
                      default=False, dest="stats",
                    help="Displays execution statistics, including CPU usage.")
    
    parser.add_option("--nocache", action="store_true",
                      default=False, dest="nocache",
                      help="Ignores the parsing cache.")
    
    
    (options, args) = parser.parse_args()
    
    
    if not args:
        print usage_short
        
        #print "Known models: %s" % \
        #    ", ".join(sorted(default_library.get_known_blocks()))
        sys.exit(-1) 
    
    
    filename = args.pop(0)
    
    #if options.debug:
    #    print "Configuration: %s" % config

    if options.trace:
        look_for = RuntimeError
    else:
        look_for = PGException

    try:
        config = parse_cmdline_args(args)
        
        pg(filename, config,
           nocache=options.nocache, debug=options.debug, stats=options.stats,
           additional_directories=additional_directories,
           additional_modules=additional_modules)
        sys.exit(0)
    except look_for as e:
        error(e)
        if not options.trace:
            info('If you run "pg" with the "--trace" option, you can see the '
                 'python details for this error.')
        sys.exit(-2)

def parse_cmdline_args(args):
    ''' Parses the command-line arguments.
        args is returned by optionparser. '''
    config = {}
    for arg in args:
        if '=' in arg:
            key, value_string = arg.split('=')
            try:
                value = int(value_string)
            except:
                try:
                    value = float(value_string)
                except:
                    value = value_string
                
            #value = parse_value(value_string)
            config[key] = value            
        else:
            raise Exception('What should I do with "%s"?' % arg)
    return config

def pg(filename, config,
       debug=False, nocache=False, stats=False,
       additional_directories=[], additional_modules=[]):
    ''' Instantiate and run a model. 
    
    Instantiate a model (filename can be either a file or a known model. '''
    
    for module in additional_modules:
        info('Importing package %r...' % module)
        __import__(module)
    
    library = Library(default_library)
    pg_look_for_models(library, ignore_cache=nocache,
                       additional_paths=additional_directories)
    
    # load standard components
    import procgraph.components #@UnusedImport

    if library.exists(block_type=filename):
#            w = Where('command line', filename, 0)
        model = library.instance(filename, name=None,
                                         config=config)
    else:
        # See if it exists
        if not os.path.exists(filename):
            # Maybe try with extension .pg
            filename_pg = "%s.pg" % filename
            if os.path.exists(filename_pg):
                filename = filename_pg
            else:
                # TODO: add where for command line
                raise SemanticError('Unknown model or file "%s".' % filename)

        # Make sure we use absolute pathnames so that we know the exact directory
        filename = os.path.realpath(filename)
        model_spec = open(filename).read()
        model = model_from_string(model_spec, config=config,
                                  filename=filename, library=library)
    
    if debug:
        model.summary()
        return

    count = 0
    model.reset_execution()
    while model.has_more():       
        model.update()
        
        if stats:
            count += 1
            if count % 500 == 0:
                model.stats.print_info()
    
    # XXX: should it know by itself?
    model.finish()
                
