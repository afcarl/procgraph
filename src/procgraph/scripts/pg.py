import sys 

# XXX: I don't know how to put these

from procgraph.components.rawseeds import *
from procgraph.components.cv import *
from procgraph.core.model_loader import model_from_string
from optparse import OptionParser


def main():
     
    parser = OptionParser()
     
    parser.add_option("--debug", action="store_true",
                      default=False, dest="debug",
                      help="Displays debug information on the model.")
    
    
    (options, args) = parser.parse_args()
    
    
    file = args.pop(0)

    model_spec = open(file).read()
    
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
    
    print 'Configuration: %s' % config
    print """%s""" % model_spec
    model = model_from_string(model_spec, config=config)
    
    if options.debug:
        model.summary()
        sys.exit(0) 
    
    model.reset_execution()
    while model.has_more():
        model.update()
        
        