''' 
    This is a set of blocks to read and write logs in HDF_ format.
    
    You need the pytables_ package to be installed.
    
    .. _pytables: http://pytables.org
     
    .. _HDF: http://en.wikipedia.org/wiki/Hierarchical_Data_Format

'''

procgraph_info = {
    # List of python packages 
    'requires':  ['tables']
} 


# Smart dependency importing
from procgraph import import_magic
tables = import_magic(__name__, 'tables')


from . import hdfwrite
from . import hdfread
from . import hdfread_many


from procgraph import pg_add_this_package_models
pg_add_this_package_models(file=__file__, assign_to=__package__)
