''' 

    Some functions specific to robotics applications. 

    Requires: http://github.com/AndreaCensi/snp_geometry
    
'''


procgraph_info = {
    # List of python packages 
    'requires':  ['snp_geometry']
} 

# Smart dependency resolution
from procgraph import import_magic
Pose = import_magic(__name__, 'snp_geometry', 'Pose')


from . import pose2velocity
from . import laser_display
from . import laser_dot_display
from . import organic_scale
from . import misc
