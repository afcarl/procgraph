import numpy

from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic
from procgraph.components import assert_rgb_image, assert_gray_image


def rgb2grayscale(rgb):  
    assert_rgb_image(rgb, 'input to rgb2grayscale')  
    r = rgb[:, :, 0].squeeze()
    g = rgb[:, :, 1].squeeze()
    b = rgb[:, :, 2].squeeze()
    # note we keep a uint8
    # gray = (r/3 + g/3 + b/3)
    gray = r * 299.0 / 1000 + g * 587.0 / 1000 + b * 114.0 / 1000
    gray = gray.astype('uint8')
    
    return gray

def gray2rgb(gray):
    ''' Converts a H x W grayscale into a H x W x 3 RGB by replicating channel. '''  
    assert_gray_image(gray, 'input to rgb2grayscale')
      
    rgb = numpy.zeros((gray.shape[0], gray.shape[1], 3), dtype='uint8')
    for i in range(3):
        rgb[:, :, i] = gray
    return rgb

default_library.register('grayscale', make_generic(1, 1, rgb2grayscale)) 
default_library.register('rgb2gray', make_generic(1, 1, rgb2grayscale)) 
default_library.register('gray2rgb', make_generic(1, 1, gray2rgb))
    
    





