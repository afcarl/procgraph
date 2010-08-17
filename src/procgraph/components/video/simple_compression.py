import numpy
import sys

from procgraph.core.block import Block 
from procgraph.components.checks import check_rgb_or_grayscale
from procgraph.components.basic import register_block
 
 
class SimpleCompression(Block): 
     
    def init(self):
        self.config.compress = True
        self.config.file
        
        self.define_input_signals(["image"])
        self.define_output_signals([])

        self.state.dtype = None
        
        self.file = open(self.config.file, 'w')
        
    def update(self):
        check_rgb_or_grayscale(self, 0)
        
        image = self.input.image        
#        h, w = image.shape[0:2]

        if self.state.dtype is None:
            self.state.dtype = numpy.dtype(
                    [('timestamp', 'float64'),
                     ('difference', 'int', image.shape)])
            
            self.state.delta = numpy.ndarray(shape=(), dtype=self.state.dtype) 
            self.state.current = numpy.zeros(dtype='int8', shape=image.shape)
            
        
        difference = image - self.state.current 
        
        if self.config.compress:
            difference = difference - difference % 4
        
        num = numpy.sum(numpy.abs(difference)) * 1.0 / (image.shape[0] * image.shape[1] * 3)
        print "n: %f" % num
        
        # TODO: truncate difference
        self.state.delta['difference'] = difference
        self.state.delta['timestamp'] = self.get_input_timestamp(0)
        self.state.current = self.state.current + difference 
        
        sys.stderr.write('.')
        numpy.save(self.file, self.state.delta)


register_block(SimpleCompression)
