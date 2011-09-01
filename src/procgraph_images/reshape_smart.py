import numpy as np
from procgraph import simple_block


# TODO: case width = None -> sqrt
# TODO: resize 2D
@simple_block
def reshape2d(x, width=None, height=None, fill_value=np.NaN):
    ''' Reshapes x into (?, width) if x is 1D.
        If width is not given, it is set to be the sqrt(size).
    
        If x is 2D, it is left alone.
    '''
    x = np.array(x)
    if x.ndim == 2:
        return x
    
    if width is not None and height is not None:
        pass
    elif width is None and height is not None:
        width = np.ceil(x.size * 1.0 / height)
    elif width is not None and height is None:
        height = np.ceil(x.size * 1.0 / width)
    elif width is None and height is None:
        width = int(np.sqrt(x.size))
        height = np.ceil(x.size * 1.0 / width)
        
    assert width is not None 
    assert height is not None
    assert width * height >= x.size
    
    y = np.zeros(shape=(height, width), dtype=x.dtype)
    y.fill(fill_value)
    y.flat[0:x.size] = x
    
    return y 