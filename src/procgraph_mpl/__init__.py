''' 
    Blocks using Matplotlib to display data. 

'''

procgraph_info = { 
    'requires':  ['matplotlib', 'matplotlib.pylab']
} 

# Smart dependencies initialization
from procgraph import import_magic, import_succesful
matplotlib = import_magic(__name__, 'matplotlib')
if import_succesful(matplotlib):
    matplotlib.use('Agg')
    
pylab = import_magic(__name__, 'matplotlib.pylab')

from .pylab_to_image import * 
from .plot import *

