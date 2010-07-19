import sys
from procgraph.core.model import Model


# XXX: I don't know how to put these

from procgraph.components.rawseeds import *


def main():
    file = sys.argv[1]

    model_spec = open(file).read()
    
    model_spec += '\n'.join(sys.argv[2:])
    
    print """%s""" % model_spec
    model = Model.from_string(model_spec)
    
    
    while model.has_more():
        model.update()