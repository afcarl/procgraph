''' 
    Blocks using the OpenCV library. 
'''

procgraph_info = {
    # List of python packages 
    'requires': 
    # [('cv', ('cv', 'opencv'))]
     [('cv2', ('cv2',))]
}


from procgraph import import_magic

# If cv is installed, it will be a reference to it, otherwise a 
# shadow object which will throw when you actually try to use it.
# cv = import_magic(__name__, 'cv')
# cv2 = import_magic(__name__, 'cv2')


from .opencv_utils import *
# import opencv_utils
