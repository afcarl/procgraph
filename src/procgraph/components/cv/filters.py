from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic
from procgraph.components.cv.opencv_utils import gradient, smooth

def rgb2grayscale(rgb):    
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
    
    
