from procgraph import Block

from cv2 import cv  # @UnresolvedImport
import numpy as np
import warnings
from procgraph_cv.conversions import numpy_to_cv


class Display(Block):
    nimages = 0 
    
    Block.config('name', default=None)
    Block.config('position', default=None)
    
    Block.alias('cv_display')
    Block.input('rgb')
    
    def init(self):
        name = self.config.name
        if name is None:
            name = 'display%d' % Display.nimages
        self.name = name
            
        Display.nimages += 1
        
        cv.NamedWindow(self.name, 1)
    
        if self.config.position is not None:
            x, y = self.config.position
        else:
            cols = 4
            w, h = 320, 320
            u = Display.nimages % cols
            v = int(np.floor(Display.nimages / cols))
            x = u * w
            y = v * h
        
        cv.MoveWindow(self.name, x, y)
        
    def update(self):
        rgb = self.input.rgb
        img = numpy_to_cv(rgb)
        cv.ShowImage(self.name, img)
    
    def finish(self):    
        warnings.warn('to fix')
        cv.DestroyAllWindows()
    
        
