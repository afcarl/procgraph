import numpy
from procgraph import register_simple_block
from .import_dependencies import Image

def imread(filename):
    try:
        im = Image.open(filename)
    except Exception as e:
        raise Exception('Could not open filename "%s": %s' % \
                        (filename, e))
    
    data = numpy.array(im)

    return data

register_simple_block(imread)
