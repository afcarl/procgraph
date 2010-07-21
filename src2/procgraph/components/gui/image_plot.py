from pylab import ion, draw, imshow
from procgraph.core.block import Block
from procgraph.core.registrar import default_library



class ImagePlot(Block):
    ''' Plots an image (anything you can pass to imshow() ) '''

    def init(self): 
        self.define_input_signals(['to_plot'])
        self.define_output_signals([])
        self.image = None
        
    def update(self):
        ion()

        data = self.get_input(0)
        
        if self.image is None:
            self.image = imshow(data);
        else:  
            self.image.set_data( data )
            self.image.changed()
            draw()
        
default_library.register('imshow', ImagePlot)

