import numpy
from procgraph.core.exceptions import BadInput

def check_2d_array(value, name="?"):
    ''' Checks that we have 2D numpy array '''
    if not isinstance(value, numpy.ndarray):
        raise Exception('Expected 2d array for %s, got %s.' %(name, value.__class__.__name__) )
        
    if len(value.shape) != 2:
        raise Exception('Bad shape for %s, expected 2D array, got %s.' % \
                        (name,str(value.shape)))
   
   
def assert_rgb_image(image, name="?"):
    if not isinstance(image, numpy.ndarray):
        raise Exception('Expected RGB image for %s, got %s.' %( name, image.__class__.__name__) )
        
    if image.dtype != 'uint8':
        raise Exception('Expected RGB image for %s , got an array %s %s.' % \
                            (name, str(image.shape), image.dtype))

    if len(image.shape) != 3 or image.shape[2] != 3:
        raise Exception('Bad shape for %s, expected RGB, got %s.' % \
                        (name,str(image.shape)))

def assert_gray_image(image, name="?"):
    if not isinstance(image, numpy.ndarray):
        raise Exception('Expected a grayscale image for %s, got %s.' %( name, image.__class__.__name__) )

    if image.dtype != 'uint8':
        raise Exception('Expected a grayscale image for %s, got an array %s %s.' % \
                            (name, str(image.shape), image.dtype))
    
    if len(image.shape) != 2:
        raise Exception('Bad shape for %s, expected grayscale, got %s.' % \
                        (name,str(image.shape)))


def check_rgb_or_grayscale(block, input):
    ''' Checks that the selected input is either a grayscale or RGB image.
        That is, a numpy array of uint8 either H x W or H x W x 3. 
        Raises BadInput if it is not. 
    ''' 
    image = block.get_input(input)
    if not isinstance(image, numpy.ndarray):
        raise BadInput('Expected RGB or grayscale, this is not even a '+
            +'numpy array: %s' % image.__class__.__name__, block, input)
    if image.dtype != 'uint8':
        raise BadInput('Expected an image, got an array %s %s.' % \
                            (str(image.shape), image.dtype), block, input)
    shape = image.shape
    if len(shape) == 3:
        if shape[2] != 3:
            raise BadInput('Bad shape for image: %s' % str(shape), block, input)
    elif len(shape) == 2:
        pass
    else:
        raise BadInput('Bad shape for image: %s' % str(shape), block, input)
        