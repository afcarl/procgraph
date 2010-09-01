from numpy import array, linspace, sin, cos
from matplotlib import pylab

from procgraph  import Block, block_alias, block_config, block_input, block_output
from procgraph.components.robotics.laser_display import pylab2rgb
import math
from procgraph.components.images.copied_from_reprep import skim_top_and_bottom
from procgraph.core.exceptions import BadInput

class LaserDotDisplay(Block):
    ''' Produces a plot of a range-finder scan variation (derivative). 
    
    It uses the same configuration as :ref:`block:laser_display`.
     
    '''
    
    block_alias('laser_dot_display')
    
    block_config('width', default=320)
    block_config('height', default=320)
    
    block_config('skim', default=5)
    
    block_config('groups', 'How to group and draw the readings. (see example) ')
    Block.config('title', 'By default it displays the signal name.'
                        ' Set the empty string to disable.', default=None)
    
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
         
        if max(abs(y)) > 1:
            raise BadInput('I expect an input normalized in the [-1,1] range.',
                           self, 'readings_dot')

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
                
            r = R0 + amp * group_y
            
            px = cos(theta + origin[2]) * r  
            py = sin(theta + origin[2]) * r
         
            pylab.plot(-py, px, color) 
            
            
        M = R0 + amp * 1.2
        pylab.axis([-M, M, -M, M])
        
        # turn off ticks labels, they don't have meaning
        pylab.setp(f.axes[0].get_xticklabels(), visible=False)
        pylab.setp(f.axes[0].get_yticklabels(), visible=False)
        
        
        if self.config.title is not None:
            if self.config.title != "":
                pylab.title(self.config.title, fontsize=10)
        else:
            # We don't have a title ---
            t = self.get_input_signals_names()[0]
            pylab.title(t, fontsize=10)

        
        self.output.image = pylab2rgb()

        pylab.close(f.number)
 
 
