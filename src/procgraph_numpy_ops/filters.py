import numpy
from numpy import multiply, array

from procgraph import COMPULSORY, register_simple_block, simple_block

@simple_block
def astype(a, dtype=COMPULSORY):
    ''' 
        Converts an array using the ``astype`` function. 
    
        :param a: Numpy array
        :type a: array
        
        :param dtype: The new dtype.
        :type dtype: string
        
        :return: typed: The Numpy array with the new type. 
        :rtype: array
    '''
    return a.astype(dtype)

@simple_block
def take(a, axis=0, indices=COMPULSORY):
    assert indices != COMPULSORY
    a = numpy.array(a)
    indices = list(indices) # parsingresult bug
    axis = int(axis)
    try:
        return a.take(axis=axis, indices=indices).squeeze()
    except Exception as e:
        raise Exception('take(axis=%s,indices=%s) failed on array '
                        'with shape %s: %s' % (axis, indices, a.shape, e))

        
@simple_block
def outer(a, b):
    ''' 
        Outer product of two vectors.
    
        This is a wrapper around :py:func:`numpy.multiply.outer`.
        
        :param a: First vector.
        :param b: Second vector.
        :return: outer: Outer product of the two vectors. 
    '''
    a = array(a)
    b = array(b)
    res = multiply.outer(a, b)
    return res


@simple_block
def select(x, every=COMPULSORY):
    '''
        Selects some of the elements of ``x``.
        
        :param x: Numpy array that can be flatly addressed.
        :param every: How many to jump (every=2 takes only the even elements).
        :return: decimated: The decimated output.
    '''
    assert every != COMPULSORY
    n = len(x)
    return x[range(0, n, every)]

@simple_block    
def normalize_Linf(x):
    ''' Normalize a vector such that ``|x|_inf = max(abs(x))= 1``. 
    
        :param x: Any numpy array.
        :return: normalized: The same array normalized.
         
    '''
    return x / numpy.abs(x).max()

@simple_block
def minimum(value, threshold=COMPULSORY):
    ''' Limits the numpy array to the given threshold. 
    
        :param value: Any numpy array.
        :return: Array of same shape.
    '''
    assert threshold != COMPULSORY
    return numpy.minimum(value, threshold)

@simple_block
def maximum(value, threshold=COMPULSORY):
    ''' Limits the numpy array to the given threshold. '''
    assert threshold != COMPULSORY
    return numpy.maximum(value, threshold)

@simple_block
def norm(value, ord=2): #@ReservedAssignment
    ''' Returns the norm of the vector. '''
    return numpy.linalg.norm(value, ord)

# XXX: not sure the best thing to do
@simple_block
def array(value):
    ''' Converts the value to a Numpy array. '''
    return numpy.array(value)

register_simple_block(numpy.mean, 'mean', params={'axis':0},
      doc='Wrapper around :np:data:`numpy.mean`.')

register_simple_block(numpy.square, 'square',
      doc='Wrapper around :np:data:`numpy.square`.')

register_simple_block(numpy.log, 'log',
      doc='Wrapper around :np:data:`numpy.log`.')

register_simple_block(numpy.abs, 'abs',
      doc='Wrapper around :np:data:`numpy.absolute`.')

register_simple_block(numpy.sign, 'sign',
      doc='Wrapper around :np:data:`numpy.sign`.')

register_simple_block(numpy.arctan, 'arctan',
      doc='Wrapper around :np:data:`numpy.arctan`.')

register_simple_block(numpy.real, 'real',
      doc='Wrapper around :np:data:`numpy.real`.')


register_simple_block(lambda x, y: numpy.dstack((x, y)), 'dstack', num_inputs=2,
      doc='Wrapper around :np:data:`numpy.ma.dstack`.')

register_simple_block(lambda x, y: numpy.hstack((x, y)), 'hstack', num_inputs=2,
      doc='Wrapper around :np:data:`numpy.ma.hstack`.')

register_simple_block(lambda x, y: numpy.vstack((x, y)), 'vstack', num_inputs=2,
      doc='Wrapper around :np:data:`numpy.ma.vstack`.')

register_simple_block(lambda x: numpy.max(array(x).flat), 'max',
      doc='Maximum over **all** elements. ')

register_simple_block(lambda x: numpy.sum(array(x).flat), 'sum',
      doc='Sum over **all** elements. ')

register_simple_block(numpy.flipud, 'flipud',
     doc='Flips the array up/down (wrapper for :py:func:`numpy.flipud`.)')

register_simple_block(numpy.fliplr, 'fliplr',
     doc='Flips the array left/right (wrapper for :py:func:`numpy.fliplr`.)')
 
register_simple_block(numpy.radians, 'deg2rad',
    doc='Converts degrees to radians (wrapper around :np:data:`numpy.radians`.)')

register_simple_block(numpy.degrees, 'rad2deg',
    doc='Converts radians to degrees (wrapper around :np:data:`numpy.degrees`.)')
 
