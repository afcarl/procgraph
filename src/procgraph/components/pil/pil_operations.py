import numpy

from procgraph.components.basic import  COMPULSORY, register_simple_block
from procgraph.components.pil.pil_conversions import Image_from_array


def pil_resize(value, width, height):
    image = Image_from_array(value)
    image = image.resize((width, height))
    return numpy.asarray(image.convert("RGB"))    
    
    
register_simple_block(pil_resize, name='resize',
                    params={ 'width':COMPULSORY, 'height':COMPULSORY})
