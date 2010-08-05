import pylab, numpy
from procgraph.core.block import Block
from procgraph.core.exceptions import BadInput
from procgraph.core.registrar import default_library
from PIL import Image

class Plot(Block):
    ''' Just plots the vector instantaneously '''

    def init(self): 
        # don't define input signals
        self.define_output_signals(['rgb'])
        self.line = None

        # set config defaults
        self.config.width = 320 
        self.config.height = 240 
        self.config.xlabel = None 
        self.config.ylabel = None
        self.config.legend = None
        self.config.title = None
        self.config.format = '-'
        
        width = self.config.width
        height = self.config.height
        
        pylab.rc('xtick', labelsize=8) 
        pylab.rc('ytick', labelsize=8) 
        self.figure = pylab.figure(frameon=False,
                                   figsize=(width / 100.0, height / 100.0))
        # left, bottom, right, top
        borders = [0.15, 0.15, 0.03, 0.05]
        w = 1 - borders[0] - borders[2]
        h = 1 - borders[1] - borders[3]
        self.axes = pylab.axes([borders[0], borders[1], w, h])
        self.figure.add_axes(self.axes)
        
        pylab.draw_if_interactive = lambda: None

        pylab.figure(self.figure.number)
        if self.config.title:
            self.axes.set_title(self.config.title)
        if self.config.xlabel:
            self.axes.set_xlabel(self.config.xlabel)
        if self.config.ylabel:
            self.axes.set_ylabel(self.config.ylabel)
        
        self.legend_handle = None
        
        self.lines = {}
        self.lengths = {}
        
    def plot_one(self, id, x, y, format):
        assert isinstance(x, numpy.ndarray)
        assert isinstance(y, numpy.ndarray)
        assert len(x.shape) <= 1
        assert len(y.shape) <= 1
        assert len(x) == len(y)
        
        
        if id in self.lengths:
            if self.lengths[id] != len(x):
                redraw = True
                self.axes.lines.remove(self.lines[id])
            else:
                redraw = False
        else:
            redraw = True
            
        if redraw:
            res = self.axes.plot(x, y, format)
            line = res[0]
            
            self.lines[id] = line
        else:
            self.lines[id].set_ydata(y)
        
        self.lengths[id] = len(x)
        
        if self.limits is None:
            self.limits = [min(x), max(x), min(y), max(y)]
        else:
            self.limits[0] = min(self.limits[0], min(x))
            self.limits[1] = max(self.limits[1], max(x))
            self.limits[2] = min(self.limits[2], min(y))
            self.limits[3] = max(self.limits[3], max(y))
            

        self.limits = map(float, self.limits)
        
    def update(self):
        self.limits = None
        
        pylab.figure(self.figure.number)
        
        for i in range(self.num_input_signals()):
            value = self.input[i]
            if isinstance(value, tuple):
                if len(value) != 2:
                    raise BadInput('Expected tuple of length 2 instead of %d.' % 
                                   len(value), self, i)
                x = numpy.array(value[0])
                y = numpy.array(value[1])
                
                if len(x.shape) > 1:
                    raise BadInput('Bad x vector w/shape %s.' % str(x.shape), self, i)
                
                if len(y.shape) > 2:
                    raise BadInput('Bad shape for y vector %s.' % str(y.shape), self, i)
                
                # TODO: check x unidimensional (T)
                # TODO: check y compatible dimensions (T x N) 
                
            else: 
                y = numpy.array(value)
                if len(y.shape) > 2:
                    raise BadInput('Bad shape for y vector %s.' % str(y.shape), self, i)

                if len(y.shape) == 1:
                    x = numpy.array(range(len(y)))     
                else:
                    assert(len(y.shape) == 2)
                    x = numpy.array(range(y.shape[1]))
                    
            if len(x) <= 1: 
                continue

            if len(y.shape) == 2:
                y = y.transpose()


            if len(y.shape) == 1:
                id = self.canonicalize_input(i)
                self.plot_one(id, x, y, self.config.format)
            else:
                assert(len(y.shape) == 2)
                num_lines = y.shape[0]
                for k in range(num_lines):
                    id = "%s-%d" % (self.canonicalize_input(i), k)
                    yk = y[k, :]
                    #print "Slice: %s -> %s (x: %s)" % (y.shape, yk.shape, x.shape)
                    self.plot_one(id, x, yk, self.config.format)
            # TODO: check that if one has time vector, also others have it

        if self.limits:
            self.axes.axis(self.limits)
        
        if self.legend_handle is None:
            legend = self.config.legend
            if legend:
                self.legend_handle = self.axes.legend(*legend,
                    loc='upper right', handlelength=1.5, markerscale=2,
                    labelspacing=0.03, borderpad=0, handletextpad=0.03,
                    borderaxespad=1)
            
        temp_file = 'frame-tmp.png' # TODO use tmpfile
        pylab.savefig(temp_file)
        im = Image.open(temp_file)
        #print pixel_data.shape
        im = im.convert("RGB")
        pixel_data = numpy.asarray(im)
        
        self.set_output(0, pixel_data)

default_library.register('plot', Plot)
