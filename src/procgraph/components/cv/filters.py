from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic
from procgraph.core.block import Block
from procgraph.components.cv.opencv_utils import gradient, smooth

def rgb2grayscale(rgb):    
    r = rgb[:, :, 0].squeeze()
    g = rgb[:, :, 1].squeeze()
    b = rgb[:, :, 2].squeeze()
    gray = (r/3 + g/3 + b/3)
    # This can be made better
    return gray


default_library.register('grayscale', make_generic(1,1,rgb2grayscale))



class Gradient(Block):
    ''' 
    Computes the gradient of a grayscale image.
    Input:
     image: H x W  numpy array
    Output:
     gx, gy: H x W  numpy array
    '''
    
    def init(self):
        self.set_config_default('aperture', 3)
        self.define_input_signals(['image'])
        self.define_output_signals(['gx','gy'])
        
    def update(self):
        image = self.get_input(0)
        aperture = self.get_config('aperture')
        gx, gy = gradient(image, aperture_size=aperture)
        
        self.set_output(0, gx) 
        self.set_output(1, gy)
     
    
    
default_library.register('gradient', Gradient)


default_library.register('smooth', make_generic(1,1,smooth,gaussian_std=5.0))
    
    
    