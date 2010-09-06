import numpy

from procgraph.components.basic import  COMPULSORY, register_simple_block

register_simple_block(lambda x, y: x + y, '+', num_inputs=2)
register_simple_block(lambda x, y: x * y, '*', num_inputs=2)
register_simple_block(lambda x, y: x - y, '-', num_inputs=2)
register_simple_block(lambda x, y: x / y, '/', num_inputs=2)
 

def astype(a, dtype):
    return a.astype(dtype)

register_simple_block(astype, params={'dtype': COMPULSORY})

register_simple_block(numpy.square, 'square',
      doc='Wrapper around :py:func:`numpy.core.umath.square`.')

register_simple_block(numpy.log, 'log',
      doc='Wrapper around :py:func:`numpy.core.umath.log`.')

register_simple_block(numpy.abs, 'abs',
      doc='Wrapper around :py:func:`numpy.core.umath.absolute`.')

register_simple_block(numpy.sign, 'sign',
      doc='Wrapper around :py:func:`numpy.core.umath.sign`.')

register_simple_block(lambda x, y: numpy.dstack((x, y)), 'dstack', num_inputs=2,
      doc='Wrapper around :py:func:`numpy.dstack`.')

register_simple_block(lambda x, y: numpy.hstack((x, y)), 'hstack', num_inputs=2,
      doc='Wrapper around :py:func:`numpy.hstack`.')

register_simple_block(lambda x, y: numpy.vstack((x, y)), 'vstack', num_inputs=2,
      doc='Wrapper around :py:func:`numpy.vstack`.')

register_simple_block(lambda x: numpy.max(array(x).flat), 'max',
      doc='Maximum over all elements.')

register_simple_block(lambda x: numpy.sum(array(x).flat), 'sum',
      doc='Sum over all elements.')

register_simple_block(numpy.flipud, 'flipud', doc='Wrapper for :py:func:`numpy.flipud`.')
register_simple_block(numpy.fliplr, 'fliplr', doc='Wrapper for :py:func:`numpy.fliplr`.')
 
 
 
 
def my_take(a, axis, indices):
    a = numpy.array(a)
    indices = list(indices) # parsingresult bug
    axis = int(axis)
    try:
        return a.take(axis=axis, indices=indices).squeeze()
    except Exception as e:
        raise Exception('take(axis=%s,indices=%s) failed on array with shape %s: %s' % \
            (axis, indices, a.shape, e))

#default_library.register('take', make_generic(1,1, numpy.take, 
#                                              axis=COMPULSORY, indices=COMPULSORY))

register_simple_block(my_take, 'take', params={'axis':0, 'indices':COMPULSORY})


from numpy import multiply, array
outer = multiply.outer
        
def my_outer(a, b):
    '''Wrapper around :py:func:`numpy.multiply.outer`.'''
    a = array(a)
    b = array(b)
    res = multiply.outer(a, b)
    #print "outer %s x %s = %s " % (a.shape,b.shape,res.shape)
    return res


register_simple_block(my_outer, 'outer', num_inputs=2)


def select(x, every=None):
    n = len(x)
    return x[range(0, n, every)]
    

register_simple_block(select, params={'every': COMPULSORY})



register_simple_block(lambda x: x / max(abs(x)), 'normalize_Linf',
                      doc='Normalize a vector such that ``|x|_inf = max(abs(x))= 1``')


def my_minimum(value, threshold):
    return numpy.minimum(value, threshold)
def my_maximum(value, threshold):
    return numpy.maximum(value, threshold)

register_simple_block(my_minimum, 'minimum', params={'threshold': COMPULSORY})
register_simple_block(my_maximum, 'maximum', params={'threshold': COMPULSORY})

