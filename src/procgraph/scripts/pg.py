import sys 

from procgraph.core.model_loader import model_from_string, pg_look_for_models
from optparse import OptionParser
from procgraph.core.registrar import default_library
import traceback
from procgraph.core.exceptions import SemanticError, PGSyntaxError


def main():
    
    pg_look_for_models(default_library)
     
    parser = OptionParser()
     
    parser.add_option("--debug", action="store_true",
                      default=False, dest="debug",
                      help="Displays debug information on the model.")
    
    
    (options, args) = parser.parse_args()
    
    
    filename = args.pop(0)

    model_spec = open(filename).read()
    
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
    
    try:
        # load standard components
        import procgraph.components

        model = model_from_string(model_spec, config=config, filename=filename)
        
        if options.debug:
            model.summary()
            sys.exit(0) 

        model.reset_execution()
        while model.has_more():
            model.update()
    except SemanticError as e:
        print e
        traceback.print_exc()    
        if e.element is not None:
            where = e.element.where
            where.print_where()
        sys.exit(-2)
    except PGSyntaxError as e:
        print e
        traceback.print_exc()    
        e.where.print_where()
        sys.exit(-2)
            
            