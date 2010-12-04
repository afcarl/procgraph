''' This is a set of blocks to read and write logs in HDF5 format.

You need the ``pytables`` package to be installed.

'''


procgraph_info = {
    # List of python packages 
    'requires':  ['tables']
} 


from procgraph import import_magic

# If cv is installed, it will be a reference to it, otherwise a 
# shadow object which will throw when you actually try to use it.
tables = import_magic(__name__, 'tables')


import hdfwrite
import hdfread


from procgraph import pg_add_this_package_models
pg_add_this_package_models(file=__file__, assign_to=__package__)
