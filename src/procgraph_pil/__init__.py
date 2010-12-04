''' Blocks for image operations based on the PIL library '''

    
procgraph_info = { 
    'requires':  ['PIL']
} 

# Smart dependencies initialization
from procgraph import import_magic, import_succesful
Image = import_magic(__name__, 'PIL.Image')
ImageFont = import_magic(__name__, 'PIL.ImageFont')
ImageDraw = import_magic(__name__, 'PIL.ImageDraw')



import pil_operations
import pil_conversions
import text
import imread
