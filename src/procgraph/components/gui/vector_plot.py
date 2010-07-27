
from pylab import ion, draw, plot, axis, figure, axes, ioff
from procgraph.core.block import Block
from procgraph.core.registrar import default_library
import numpy 
import pylab
from PIL import Image


class SimplePlot(Block):
    ''' Just plots the vector instantaneously '''

    def init(self): 
        self.define_input_signals(['to_plot'])
        self.define_output_signals([])
        self.line = None
        self.figure = figure()
        self.set_config_default('format', 'k.')
        
    def update(self):
        ion()

        x = self.get_input(0)

        x = numpy.array(x)
        
        
        format = self.get_config('format')
        
        if self.line is None:
            figure(self.figure.number)
            self.n = len(x)    
            self.line, = plot(range(self.n), x, format)
            self.axes = axes()
            
        else:
            if len(x) != self.n:
                self.axes.lines.remove(self.line)
                self.n = len(x)    
                self.line, = plot(range(self.n), x, format)
            else:
                self.line.set_ydata(x)
        #   a = axis()
        #    axis([ a[0],a[1],min(x),max(x)])
        axis([ 0, self.n, min(x),max(x)])
        
        draw()
        
default_library.register('plot', SimplePlot)



class RGBPlot(Block):
    ''' Just plots the vector instantaneously '''

    def init(self): 
        self.define_input_signals(['to_plot'])
        self.define_output_signals(['rgb'])
        self.line = None

        self.set_config_default('width', 320)
        self.set_config_default('height', 240)
        
        width = self.get_config('width')
        height = self.get_config('height')
        
        pylab.rc('xtick', labelsize=8) 
        pylab.rc('ytick', labelsize=8) 
        self.figure = pylab.figure(frameon=False,figsize=(width / 100.0, height / 100.0))
        # left, bottom, right, top
        borders = [0.15, 0.15, 0.03, 0.05]
        w = 1 - borders[0] - borders[2]
        h = 1 - borders[1] - borders[3]
        self.axes = pylab.axes([borders[0], borders[1], w, h])

        pylab.draw_if_interactive = lambda: None

        self.set_config_default('format', 'k.')
        
    def update(self):
        #ion()

        x = self.get_input(0)
        # TODO: add check_cast_array
        x = numpy.array(x) 
        
        format = self.get_config('format')
        
        if self.line is None: 
            self.n = len(x)    
            self.line, = self.axes.plot(range(self.n), x, format)
        else:
            if len(x) != self.n:
                self.axes.lines.remove(self.line)
                self.n = len(x)    
                self.line, = self.axes.plot(range(self.n), x, format)
            else:
                self.line.set_ydata(x)
        
        axis([ 0, self.n, min(x),max(x)])
        #print "x: %s, %s axis: %s" % (min(x),max(x),axis())
            #draw()
        
        temp_file = 'frame-tmp.png'
        pylab.savefig(temp_file)
        im = Image.open(temp_file)
        #print pixel_data.shape
        im = im.convert("RGB")
        pixel_data = numpy.asarray(im)
        
        self.set_output(0, pixel_data)
        
        # XXX This is inefficient -- we are forced to make a copy
        # because 
        #self.set_output(0, pixel_data[:,:,0:3].squeeze().copy())


default_library.register('rgbplot', RGBPlot)

