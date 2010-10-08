from pylab import ion, draw, imshow

if False:
    
    from procgraph import Block 
    
    class ImagePlot(Block):
        ''' Plots an image (anything you can pass to imshow() ) '''
    
        Block.alias('imshow')
        
        Block.input('to_plot', 'Image to plot.')
        
        def init(self):  
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
         

