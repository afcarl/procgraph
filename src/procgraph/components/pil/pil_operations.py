import numpy

from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic, COMPULSORY
from procgraph.components.pil.pil_conversions import Image_from_array



def pil_resize(value, width, height):
    image = Image_from_array(value)
    image = image.resize((width, height))
    return numpy.asarray(image.convert("RGB"))    
    
default_library.register('resize',
        make_generic(1, 1, pil_resize, width=COMPULSORY, height=COMPULSORY))
