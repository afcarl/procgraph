''' This is a set of blocks to read and write logs in HDF5 format.

You need the ``pytables`` package to be installed.

'''

import hdfwrite
import hdfread


# FIXME, make this easier
import os
from procgraph.core.registrar import default_library
from procgraph.core.model_loader import pg_look_for_models
dir = os.path.join(os.path.dirname(__file__), 'models')
pg_look_for_models(default_library, additional_paths=[dir], ignore_env=True,
                   assign_to_module='procgraph_hdf')
