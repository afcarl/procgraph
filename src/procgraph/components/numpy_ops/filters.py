from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic
import numpy

default_library.register('double', make_generic(1,1, lambda x:x*2))
default_library.register('square', make_generic(1,1, numpy.square))
default_library.register('log', make_generic(1,1, numpy.log))
default_library.register('abs', make_generic(1,1, numpy.abs))
