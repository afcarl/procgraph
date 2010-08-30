from numpy import array, linspace, asarray, sin, cos, minimum, \
    nonzero, logical_not, maximum
from matplotlib import pylab
from PIL import Image
import tempfile

from procgraph  import Block, block_alias, block_config, block_input, block_output

class LaserDisplay(Block):
    ''' Produces a plot of a range-finder scan. 
    
    
    display_sick.groups = [{ indices: [0,179], theta: [-1.57,+1.57],
             color: 'r', origin: [0,0,0]}]
    
    '''
    
    block_alias('laser_display')
    
    block_config('width', default=320)
    block_config('height', default=320)
    block_config('max_readings', default=30)
    block_config('groups', 'How to group and draw the readings. (see example) ')
    
    block_input('readings')
    block_output('image')
     
    # Exampl
    def init(self):
        self.define_input_signals(['readings'])
        self.define_output_signals(['image'])
        self.config.width = 320
        self.config.height = 320
        self.config.max_readings = 30
        
        self.state.theta = None
        
    def update(self):
        
        readings = array(self.input.readings)
            

        f = pylab.figure(frameon=False,
                        figsize=(self.config.width / 100.0,
                                 self.config.height / 100.0))
            
        # limit the readings
        
        bounds = array([0, 0, 0, 0])
                
        for group in self.config.groups:
            indices = group['indices']
            indices = range(indices[0], indices[-1] + 1)
            theta_spec = group['theta']
            origin = group.get('origin', [0, 0, 0])
            color = group.get('color', 'b.')
            max_readings = group.get('max_readings', self.config.max_readings)
            group_readings = minimum(readings[indices], max_readings)
        
        
            N = len(indices)
            theta = linspace(theta_spec[0], theta_spec[-1], N)
            
            x = cos(theta + origin[2]) * group_readings + origin[0] 
            y = sin(theta + origin[2]) * group_readings + origin[1]
        
            valid_flag = group_readings < max_readings
            valid, = nonzero(valid_flag)
            invalid, = nonzero(logical_not(valid_flag))
            
            pylab.plot(-y[valid], x[valid], color)
            pylab.plot(-y[invalid], x[invalid] , 'r.')
            #pylab.xlabel('<-- y')
            #pylab.ylabel('x')
            
            R = max_readings * 1.1
            x_R = R * cos(theta)
            y_R = R * sin(theta)
            group_bounds = array([min(x_R), max(x_R), min(y_R), max(y_R)])
            for i in [1, 3]:
                bounds[i] = maximum(bounds[i], group_bounds[i])
            for i in [0, 2]:
                bounds[i] = minimum(bounds[i], group_bounds[i])
            
        pylab.axis(bounds)
        
        self.output.image = pylab2rgb()

        pylab.close(f.number)
 

def pylab2rgb():
    ''' Saves and returns the pixels in the current pylab figure. 
    
        Returns a RGB uint8 array.
        Uses PIL to do the job. 
    '''
    
    temp_file = tempfile.NamedTemporaryFile(suffix='.png')
    temp_filename = temp_file.name
    pylab.savefig(temp_filename)
    im = Image.open(temp_filename)
    im = im.convert("RGB")
    rgb = asarray(im)    
    return rgb
        
    
