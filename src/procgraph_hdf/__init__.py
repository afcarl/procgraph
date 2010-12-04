''' This is a set of blocks to read and write logs in HDF5 format.

You need the ``pytables`` package to be installed.

'''


procgraph_info = {
    # List of python packages 
    'requires':  ['tables']
} 


# Smart dependency importing
from procgraph import import_magic
tables = import_magic(__name__, 'tables')


import hdfwrite
import hdfread


from procgraph import pg_add_this_package_models
pg_add_this_package_models(file=__file__, assign_to=__package__)
