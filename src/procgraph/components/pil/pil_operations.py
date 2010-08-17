import numpy

from procgraph.components.basic import  register_simple_block
from procgraph.components.pil.pil_conversions import Image_from_array


def pil_resize(value, width=None, height=None):
    image = Image_from_array(value)
    
    if width is None and height is None:
        raise ValueError('You should pass at least one of width and height.')
    
    if width is None and height is not None:
        width = (height * image.size[0]) / image.size[1]
    elif height is None and width is not None:
        height = (width * image.size[1]) / image.size[0]
    
    #    raise Exception('wrong assertion')
        
    image = image.resize((width, height))
    return numpy.asarray(image.convert("RGB"))    
    
    
register_simple_block(pil_resize, name='resize',
                    params={ 'width':None, 'height':None})
