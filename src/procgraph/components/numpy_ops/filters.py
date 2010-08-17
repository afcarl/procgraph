import numpy

from procgraph.components.basic import  COMPULSORY, register_simple_block

register_simple_block(lambda x, y: x + y, '+', num_inputs=2)
register_simple_block(lambda x, y: x * y, '*', num_inputs=2)
register_simple_block(lambda x, y: x - y, '-', num_inputs=2)
register_simple_block(lambda x, y: x / y, '/', num_inputs=2)

#default_library.register('+', make_generic(2, 1, lambda x, y: x + y))
#default_library.register('*', make_generic(2, 1, lambda x, y: x * y))
#default_library.register('-', make_generic(2, 1, lambda x, y: x - y))
#default_library.register('/', make_generic(2, 1, lambda x, y: x / y))




def astype(a, dtype):
    return a.astype(dtype)

register_simple_block(astype, params={'dtype': COMPULSORY})

register_simple_block(numpy.square, 'square')
register_simple_block(numpy.log, 'long')
register_simple_block(numpy.abs, 'abs')
register_simple_block(numpy.sign, 'sign')
 
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

register_simple_block(my_take, 'take',
    params={'axis':COMPULSORY, 'indices':COMPULSORY})


from numpy import multiply, array
outer = multiply.outer
        
def my_outer(a, b):
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

