import sys, os, traceback 
from optparse import OptionParser

from procgraph.core.model_loader import model_from_string, pg_look_for_models
from procgraph.core.registrar import default_library
from procgraph.core.exceptions import SemanticError, PGSyntaxError 
from procgraph.core.parsing_elements import Where


def main():
    try:
        pg_look_for_models(default_library)
         
        parser = OptionParser()
         
        parser.add_option("--debug", action="store_true",
                          default=False, dest="debug",
                          help="Displays debug information on the model.")
        
        
        (options, args) = parser.parse_args()
        
        if not args:
            print "Usage:    pg  <model>.pg   [param=value  param=value ... ]"
            
            print "Known models: %s" % \
                ", ".join(sorted(default_library.get_known_blocks()))
            sys.exit(-1) 
        
        # load standard components
        import procgraph.components #@UnusedImport

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

        
        if default_library.exists(block_type=filename):
            w = Where('command line', filename, 0)
            model = default_library.instance(filename, name=None,
                                             config=config, where=w)
        else:
            if not os.path.exists(filename):
                raise Exception('Uknown file "%s".' % filename)

            model_spec = open(filename).read()
            model = model_from_string(model_spec, config=config,
                                      filename=filename)
        
        if options.debug:
            model.summary()
            sys.exit(0) 

        count = 0
        model.reset_execution()
        while model.has_more():
            count += 1
            model.update()
            
            if count % 500 == 0:
                model.stats.print_info()
                
    #except ModelExecutionError as e:
    #    print e
    #    traceback.print_exc()    
        
    except SemanticError as e:
        print e
        traceback.print_exc()    
        if e.element is not None:
            where = e.element.where
            if where is None:
                raise Exception("%s does not have where?" % e.element)
            
            where.print_where()
        sys.exit(-2)
    except PGSyntaxError as e:
        print e
        traceback.print_exc()    
        e.where.print_where()
        sys.exit(-2)
            
            
