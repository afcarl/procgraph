import debug_components

# Check that the dependendencies are there before importing modules
from collections import namedtuple #@UnresolvedImport
Option = namedtuple('Option', 'module desc requires') #@UndefinedVariable

import procgraph_cv
import procgraph_foo
import procgraph_hdf
import procgraph_images
import procgraph_io_misc
import procgraph_mpl
import procgraph_mplayer
import procgraph_numpy_ops
import procgraph_pil
import procgraph_robotics
import procgraph_signals
import procgraph_statistics

#
## FIXME: there is a redundancy here and in setup.py
# 
#optional_packages = [
#                     
#    Option('procgraph_cv',
#            'Functions to interact with the OpenCV.',
#              ['cv']),
#
#    Option('procgraph_pil',
#            'Functions to interact with the PIL image library.',
#              ['PIL']),
#              
#    Option('procgraph_mpl',
#            'Functions to interact with matplotlib.',
#            ['PIL', 'matplotlib']),
#            
#    Option('procgraph_robotics', # uses procgraph_mpl
#            'Misc. functions for robotics data sources.',
#            ['PIL', 'matplotlib', 'snp_geometry']),
#            
#    Option('procgraph_hdf', # uses procgraph_mpl
#            'Reading and writing HDF logs..',
#            ['tables'])
#]
#
#def is_package_available(p):
#    ''' Checks that a package is available. '''
#    try:
#        __import__(p)
#        return True
#    except ImportError:
#        return False
#
#def get_suitable():
#    ''' returns ok, not_ok '''
#    ok = []
#    not_ok = []
#
#    for op in optional_packages:
#        found = all([is_package_available(m) 
#                 for m in op.requires])
#        if found:
#            ok.append(op)
#        else:
#            not_ok.append(op)
#    return ok, not_ok
#
#
#ok, not_ok = get_suitable()
#for op in ok:
#    __import__(op.module)
    
    
