from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic
from procgraph.components.cv.opencv_utils import gradient, smooth
import numpy

def assert_rgb_image(image, name="?"):
    if not isinstance(image, numpy.ndarray):
        raise Exception('Expected RGB image for %s, got %s.' %( name, image.__class__.__name__) )
        
    if image.dtype != 'uint8':
        raise Exception('Expected an image, got an array %s %s.' % \
                            (str(image.shape), image.dtype))

    if len(image.shape) != 3 or image.shape[2] != 3:
        raise Exception('Bad shape for %s, expected RGB, got %s.' % \
                        (name,str(image.shape)))

def assert_gray_image(image, name="?"):
    if not isinstance(image, numpy.ndarray):
        raise Exception('Expected RGB image for %s, got %s.' %( name, image.__class__.__name__) )

    if image.dtype != 'uint8':
        raise Exception('Expected an image, got an array %s %s.' % \
                            (str(image.shape), image.dtype))
    
    if len(image.shape) != 2:
        raise Exception('Bad shape for %s, expected grayscale, got %s.' % \
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

def gray2rgb(gray):
    ''' Converts a H x W grayscale into a H x W x 3 RGB by replicating channel. '''  
    assert_gray_image(gray, 'input to rgb2grayscale')
      
    rgb = numpy.zeros((gray.shape[0],gray.shape[1],3), dtype='uint8')
    for i in range(3):
        rgb[:,:,i] = gray
    return rgb

default_library.register('grayscale', make_generic(1,1,rgb2grayscale)) 
default_library.register('rgb2gray', make_generic(1,1,rgb2grayscale)) 
default_library.register('gray2rgb', make_generic(1,1,gray2rgb))
default_library.register('gradient', make_generic(1,2,gradient,aperture_size=3))
default_library.register('smooth', make_generic(1,1,smooth,gaussian_std=5.0))
    
    





