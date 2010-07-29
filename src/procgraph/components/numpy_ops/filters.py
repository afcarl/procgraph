from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic, COMPULSORY
import numpy


default_library.register('double', make_generic(1,1, lambda x:x*2))
default_library.register('square', make_generic(1,1, numpy.square))
default_library.register('log', make_generic(1,1, numpy.log))
default_library.register('abs', make_generic(1,1, numpy.abs))
default_library.register('sign', make_generic(1,1, numpy.sign))

from numpy import multiply
outer = multiply.outer

default_library.register('outer', make_generic(2,1, numpy.outer))


def select(x, every=None):
    n = len(x)
    return x[range(0,n,every)]
    

default_library.register('select', make_generic(1,1, select, every=COMPULSORY))
