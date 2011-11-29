''' Blocks for image operations based on the PIL library '''

    
procgraph_info = { 
    'requires':  ['PIL']
} 

# Smart dependencies initialization
from procgraph import import_magic, import_succesful
Image = import_magic(__name__, 'PIL.Image')
ImageFont = import_magic(__name__, 'PIL.ImageFont')
ImageDraw = import_magic(__name__, 'PIL.ImageDraw')



from . import pil_operations
from . import pil_conversions
from . import text
from . import imread
from . import imwrite
