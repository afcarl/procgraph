import sys, os, traceback 
from optparse import OptionParser

from procgraph.core.model_loader import model_from_string, pg_look_for_models
from procgraph.core.registrar import default_library, Library
from procgraph.core.exceptions import SemanticError, PGSyntaxError 
from procgraph.core.parsing_elements import Where
from procgraph.core.visualization import error



def main(): 
    parser = OptionParser()

    def load_module(option, opt_str, value, parser):
        print 'Importing module %s' % value
        __import__(value)
     
    parser.add_option("-m", "--import", dest='module',
                  action="callback", callback=load_module,
                  type="string", help='Loads the specified module')

    parser.add_option("--debug", action="store_true",
                      default=False, dest="debug",
                      help="Displays debug information on the model.")
    
    parser.add_option("--stats", action="store_true",
                      default=False, dest="stats",
                      help="Displays execution statistics, including CPU usage.")
    
    parser.add_option("--nocache", action="store_true",
                      default=False, dest="nocache",
                      help="Ignores the parsing cache.")
    
    
    (options, args) = parser.parse_args()
    
    
    if not args:
        print "Usage:    pg  <model>.pg   [param=value  param=value ... ]"
        
        #print "Known models: %s" % \
        #    ", ".join(sorted(default_library.get_known_blocks()))
        sys.exit(-1) 
    
    
    filename = args.pop(0)
        
    config = {}
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=')
            try:
                value = float(value)
            except:
                try: 
                    value = int(value)
                except:
                    pass
            config[key] = value            
        else:
            raise Exception('What should I do with "%s"?' % arg)
    
    if options.debug:
        print "Configuration: %s" % config

    pg(filename, config,
       nocache=options.nocache, debug=options.debug, stats=options.stats)
            

def pg(filename, config, debug=False, nocache=False, stats=False):
    ''' Instantiate and run a model. 
    
    Instantiate a model (filename can be either a file or a known model. '''
    
    try:
        library = Library(default_library)
        pg_look_for_models(library, ignore_cache=nocache)
        
        # load standard components
        import procgraph.components #@UnusedImport

        if library.exists(block_type=filename):
            w = Where('command line', filename, 0)
            model = library.instance(filename, name=None,
                                             config=config, where=w)
        else:
            if not os.path.exists(filename):
                raise Exception('Uknown model or file "%s".' % filename)

            model_spec = open(filename).read()
            model = model_from_string(model_spec, config=config,
                                      filename=filename)
        
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
        
        # XXX: it should know by itself
        model.finish()
                
    #except ModelExecutionError as e:
    #    print e
    #    traceback.print_exc()    
        
    except SemanticError as e:
        #traceback.print_exc()    
        error(e)
        if e.element is not None:
            where = e.element.where
            if where is None:
                raise Exception("%s does not have where?" % e.element)
            
            s = str(where)
            error(s)
            
        raise Exception('Semantic error')
    except PGSyntaxError as e:
        #traceback.print_exc()    
        error(e)
        error(str(e.where))
        raise Exception('Syntax error')
            
    #return model
