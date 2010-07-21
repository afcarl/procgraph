import sys 

# XXX: I don't know how to put these

from procgraph.components.rawseeds import *
from procgraph.components.cv import *
from procgraph.core.model_loader import model_from_string


def main():
    file = sys.argv[1]

    model_spec = open(file).read()
    
    config = {}
    for arg in sys.argv[2:]:
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
    
    model.reset_execution()
    while model.has_more():
        model.update()
        
        