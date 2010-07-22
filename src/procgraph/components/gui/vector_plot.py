
from pylab import ion, draw, plot, axis, figure, axes
from procgraph.core.block import Block
from procgraph.core.registrar import default_library
import numpy 


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
        #print "Received %s @ time %s" % (x, self.get_input_timestamp(0)) 
        x = numpy.array(x)
        
        
        format = self.get_config('format')
        
        if self.line is None:
            figure(self.figure.number)    
            self.line, = plot(range(len(x)), x, format)
            self.axes = axes()
            self.n = len(x)
        else:
            if len(x) != self.n:
                self.axes.lines.remove(self.line)
                self.line, = self.axes.plot(range(len(x)), x, format)
                #raise Exception('First received length %s')
            else:
                self.line.set_ydata(x)
            a = axis()
            axis([ a[0],a[1],min(x),max(x)])
            draw()
        
default_library.register('plot', SimplePlot)

