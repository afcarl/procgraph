import numpy

from procgraph.core.block import Block 
from procgraph.components  import assert_rgb_image
from procgraph.components.basic import register_block

        
def place_at(canvas, image, xpix, ypix):
    #print canvas.shape, image.shape
    xsize = min(canvas.shape[1] - xpix, image.shape[1])
    ysize = min(canvas.shape[0] - ypix, image.shape[0])
    if len(image.shape) == 2:
        image = image.reshape((image.shape[0], image.shape[1], 1))
    canvas[ypix:(ypix + ysize), xpix:(xpix + xsize), 0:3] = image[0:ysize, 0:xsize, :]


class Compose(Block):
    '''
    Arguments:
    - width, height  pixels
    - positions a string that evals to a structure such as 
    compose.positions = "{'y': [0,0], 'ys': [320,20]}"
    '''
    def init(self):
        self.define_output_signals(['canvas'])
        
        
    def update(self):
        width = self.get_config('width')
        height = self.get_config('height')
        
        canvas = numpy.zeros((height, width, 3), dtype='uint8')
        
        positions = self.get_config('positions')

        if not isinstance(positions, dict):
            raise Exception('I expected a dict, not "%s"' % positions)
        
       
        for signal, position in positions.items():
            if not self.is_valid_input_name(signal):
                raise Exception('Uknown input "%s" in %s.' % (signal, self))
            rgb = self.get_input(signal)
            # TODO check
            if rgb is not None:
                assert_rgb_image(rgb, 'input %s to compose block' % signal)
                
                place_at(canvas, rgb, position[0], position[1])
                #print "Writing image %s" % signal
            else:
                print "Ignoring image %s because not ready.\n" % signal
        
        self.set_output(0, canvas)
       
register_block(Compose, 'compose')

        
        
        
