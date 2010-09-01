from numpy import array, linspace, sin, cos
from matplotlib import pylab

from procgraph  import Block, block_alias, block_config, block_input, block_output
from procgraph.components.robotics.laser_display import pylab2rgb
import math
from procgraph.components.images.copied_from_reprep import skim_top_and_bottom

class LaserDotDisplay(Block):
    ''' Produces a plot of a range-finder scan variation (derivative). 
    
    It uses the same configuration as :ref:`block:laser_display`.
     
    '''
    
    block_alias('laser_dot_display')
    
    block_config('width', default=320)
    block_config('height', default=320)
    
    block_config('skim', default=5)
    
    block_config('groups', 'How to group and draw the readings. (see example) ')
    
    block_input('readings_dot')
    
    block_output('image')
     
    # Exampl
    def init(self):
        self.define_input_signals(['readings_dot'])
        self.define_output_signals(['image'])
        self.config.width = 320
        self.config.height = 320
        self.config.max_readings = 30
         
        self.config.skim = 10
        self.config.scale = True
        self.config.title = None
        
    def update(self):
        
        y = array(self.input.readings_dot)
         

        f = pylab.figure(frameon=False,
                        figsize=(self.config.width / 100.0,
                                 self.config.height / 100.0))
             
        R0 = 3
        amp = 1
        
        theta = linspace(0, 2 * math.pi, 300)
        pylab.plot(R0 * cos(theta), R0 * sin(theta), 'k--')
        
        for group in self.config.groups:
            indices = group['indices']
            indices = range(indices[0], indices[-1] + 1)
            theta_spec = group['theta']
            origin = group.get('origin', [0, 0, 0])
            color = group.get('color', 'b.')
             
            N = len(indices)
            
            theta = linspace(theta_spec[0], theta_spec[-1], N)
            
            group_y = y[indices]
            
#            if self.config.scale:
#                group_y = skim_top_and_bottom(group_y, self.config.skim)
#            
#                # Normalize y
#                y_max = abs(group_y).max()
#                
#                if y_max > 0:
#                    group_y = group_y / y_max 
#                
#                if indices[0] == 0:    
#                    print group['indices'], y_max
                
            r = R0 + amp * group_y
            
            px = cos(theta + origin[2]) * r  
            py = sin(theta + origin[2]) * r
         
            pylab.plot(-py, px, color) 
            
            
        M = R0 + amp * 1.2
        pylab.axis([-M, M, -M, M])
        
        self.output.image = pylab2rgb()

        pylab.close(f.number)
 
 
