''' Blocks for encoding/decoding video based on MPlayer. '''

from .mp4conversion import *
from .mencoder import *
from .mplayer import *
from .depth_buffer import *

procgraph_info = {
    # List of python packages 
    'requires': ['qtfaststart']
}



from procgraph import pg_add_this_package_models
pg_add_this_package_models(__file__, __package__)
