from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic
from procgraph.components.cv.opencv_utils import gradient, smooth
import numpy

def assert_rgb_image(image, name="?"):
    if not isinstance(image, numpy.ndarray):
        raise Exception('Expected RGB image for %s, got %s' %( name, str(image)) )
        
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise Exception('Bad shape for %s, expected RGB, got %s' % \
                        (name,str(image.shape)))

def rgb2grayscale(rgb):  
    assert_rgb_image(rgb, 'input to rgb2grayscale')  
    r = rgb[:, :, 0].squeeze()
    g = rgb[:, :, 1].squeeze()
    b = rgb[:, :, 2].squeeze()
    # note we keep a uint8
    gray = (r/3 + g/3 + b/3)
    # This can be made better
    return gray


default_library.register('grayscale', make_generic(1,1,rgb2grayscale)) 
default_library.register('gradient', make_generic(1,2,gradient,aperture_size=3))
default_library.register('smooth', make_generic(1,1,smooth,gaussian_std=5.0))
    
    
