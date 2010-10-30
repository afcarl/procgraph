from procgraph import Block
import numpy
from procgraph.components.checks import check_rgb

class Border(Block):
    ''' Adds a block around the input image. '''
    Block.alias('border')
    
    Block.input('rgb', 'Input image.')
    Block.output('rgb', 'Image with borders added around.')
    Block.config('color', 'border color', default=[1, 1, 1])
    Block.config('left', 'pixel length for left border', default=0)
    Block.config('right', 'pixel length for right border', default=0)
    Block.config('top', 'pixel length for top border', default=0)
    Block.config('bottom', 'pixel length for bottom border', default=0)
 
    def update(self):
        check_rgb(self, 'rgb')
        
        # TODO: check
        rgb = self.input.rgb 
        
        if self.config.left > 0:
            height = rgb.shape[0]
            pad = self.pad(height, self.config.left)
            rgb = numpy.hstack((pad, rgb))
        if self.config.right > 0:
            height = rgb.shape[0]
            pad = self.pad(height, self.config.right)
            rgb = numpy.hstack((rgb, pad))
        if self.config.top > 0:
            width = rgb.shape[1]
            pad = self.pad(self.config.top, width)
            rgb = numpy.vstack((pad, rgb))
        if self.config.bottom > 0:
            width = rgb.shape[1]
            pad = self.pad(self.config.bottom, width)
            rgb = numpy.vstack((rgb, pad))
            
        self.output.rgb = rgb
        
    def pad(self, height, width):
        pad = numpy.zeros((height, width, 3), dtype='uint8')
        for i in range(3):
            pad[:, :, i] = self.config.color[i]
        return pad
    
        
