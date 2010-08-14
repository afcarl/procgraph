import numpy

from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic, COMPULSORY, \
    register_simple_block



default_library.register('double', make_generic(1, 1, lambda x:x * 2))
default_library.register('square', make_generic(1, 1, numpy.square))
default_library.register('log', make_generic(1, 1, numpy.log))
default_library.register('abs', make_generic(1, 1, numpy.abs))
default_library.register('sign', make_generic(1, 1, numpy.sign))

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


register_simple_block(my_outer, 'outer')


def select(x, every=None):
    n = len(x)
    return x[range(0, n, every)]
    

register_simple_block(select)

