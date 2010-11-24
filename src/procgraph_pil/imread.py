from PIL import Image
import numpy
from procgraph.components.basic import register_simple_block

def imread(filename):
    try:
        im = Image.open(filename)
    except Exception as e:
        raise Exception('Could not open filename "%s": %s' % \
                        (filename, e))
    
    data = numpy.array(im)

    return data

register_simple_block(imread)
