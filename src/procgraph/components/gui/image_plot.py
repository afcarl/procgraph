from pylab import ion, draw, imshow


from procgraph import Block, block_alias, block_config

class ImagePlot(Block):
    ''' Plots an image (anything you can pass to imshow() ) '''

    block_alias('imshow')
    
    block_input('to_plot', 'Image to plot.')
    
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
            self.image.set_data(data)
            self.image.changed()
            draw()
         

