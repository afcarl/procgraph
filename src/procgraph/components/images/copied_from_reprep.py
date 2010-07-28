import numpy
from numpy import maximum, minimum, zeros
from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic
from procgraph.components import check_2d_array

def posneg(value, max_value=None):
    """ 
    Converts a 2D value to normalized uint8 RGB red=positive, blue=negative 0-255.
    
     
    """
    
    check_2d_array(value, 'input to posneg')
        
    value = value.squeeze()
    
    if len(value.shape) != 2:
        raise Exception('I expected a H x W image, got shape %s.' % str(value.shape))
    
    if max_value is None:
        max_value = numpy.max(abs(value))
        if max_value == 0:
            raise ValueError('You asked to normalize a matrix which is all 0')
    
    value = value / max_value

    positive_part = abs((maximum(value, 0)) * 255).astype('uint8')
    negative_part = abs((minimum(value, 0)) * 255).astype('uint8')
    result = zeros((value.shape[0], value.shape[1], 3), dtype='uint8')
    
    
    anysign = maximum(positive_part, negative_part)
    result[:, :, 0] = 255 - negative_part[:, :]
    result[:, :, 1] = 255 - anysign
    result[:, :, 2] = 255 - positive_part[:, :]
    
    return result


default_library.register('posneg', make_generic(1,1,posneg,max_value=None))  


def scale(value, min_value=None, max_value=None,
                 min_color=[1, 1, 1], max_color=[0, 0, 0]):
    """ Provides a RGB representation of the values by interpolating the range 
        [min(value),max(value)] into the colorspace [min_color, max_color].
    
    Args:
      value:      a numpy array with finite values squeeze()able to (W,H).
      min_value:  If specified, this is taken to be the threshold. Everything
                  below min_value is considered to be equal to min_value.
      max_value:  Optional upper threshold.
      min_color:  color associated to minimum value. Default: [1,1,1] = white.
      max_color:  color associated to maximum value. Default: [0,0,0] = black.
    
    Raises:
      ValueError: if min_value == max_value
    
    Returns:  a (W,H,3) numpy array with dtype uint8 representing a RGB image.
      
    """
    
    check_2d_array(value, 'input to scale()')
    
    #assert_finite(value)
    value = value.squeeze()
    #require_shape((gt(0), gt(0)), value)
    
    min_color = numpy.array(min_color)
    max_color = numpy.array(max_color)
    #require_shape((3,), min_color)
    #require_shape((3,), max_color)
    
    if max_value is None:
        max_value = numpy.max(value)
        
    if min_value is None:
        min_value = numpy.min(value)

    if max_value == min_value:
        raise ValueError('I end up with max_value = %s = %s = min_value.' % \
                         (max_value, min_value))

    value01 = (value - min_value) / (max_value - min_value)
    
    # Cut at the thresholds
    value01 = maximum(value01, 0)
    value01 = minimum(value01, 1)

    result = zeros((value.shape[0], value.shape[1], 3), dtype='uint8')
    
    for u in [0, 1, 2]:
        result[:, :, u] = 255 * ((1 - value01) * min_color[u] \
                                 + (value01) * max_color[u])
    
    return result


default_library.register('scale', 
                         make_generic(1,1,scale,
                                      min_color=[1, 1, 1], max_color=[0, 0, 0],
                                      min_value=None,max_value=None))  
