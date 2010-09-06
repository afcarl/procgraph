import time
import tempfile
import  numpy
from PIL import Image
from matplotlib import pylab

from procgraph import Block

from procgraph.core.exceptions import BadInput, BadConfig

class Plot(Block):
    ''' Plots the inputs using matplotlib. 
    
        This block accepts an arbitrary number of signals. 
        Each signals is treated independently and plot separately. 
        
        Each signal can either be:
        
        1.  A tuple of length 2. It is interpreted as a tuple ``(x,y)``,
            and we plot ``x`` versus ``y`` (see also :ref:`block:make_tuple`).
            
        2.  A list of numbers, or a 1-dimensional numpy array of length N. 
            In this case, it is interpreted as the y values, and we set  ``x = 1:N``. 
        
     '''
     
    Block.alias('plot')
    
    Block.config('width', 'Image dimension', default=320)
    Block.config('height', 'Image dimension', default=240)
    Block.config('xlabel', default=None)
    Block.config('ylabel', default=None)
    Block.config('legend', default=None)
    Block.config('title', default=None)
    Block.config('format', default='-')
    Block.config('symmetric', 'An alternative to y_min, y_max.'
                            ' Makes sure the plot is symmetric for y. ',
                                default=False)
    Block.config('x_min', default=None)
    Block.config('x_max', default=None)
    Block.config('y_min', default=None)
    Block.config('y_max', default=None)
    Block.config('keep', default=False)

    Block.input_is_variable('Data to plot.')
    
    Block.output('rgb', 'Resulting image.')
   

    def init(self): 
        # don't define input signals
        self.define_output_signals(['rgb'])
        self.line = None
 
        # figure gets initialized in update() on the first execution
        self.figure = None
        
    def init_figure(self):
        width = self.config.width
        height = self.config.height
        
        pylab.rc('xtick', labelsize=8) 
        pylab.rc('ytick', labelsize=8) 

        ''' Creates figure object and axes '''
        self.figure = pylab.figure(frameon=False,
                                   figsize=(width / 100.0, height / 100.0))
        # left, bottom, right, top
        borders = [0.15, 0.15, 0.03, 0.05]
        w = 1 - borders[0] - borders[2]
        h = 1 - borders[1] - borders[3]
        #self.axes = pylab.axes([borders[0], borders[1], w, h])
        self.axes = pylab.axes()
        self.figure.add_axes(self.axes)
        
        pylab.draw_if_interactive = lambda: None

        pylab.figure(self.figure.number)
        if self.config.title is not None:
            if self.config.title != "":
                self.axes.set_title(self.config.title, fontsize=10)
        else:
            # We don't have a title ---
            t = ", ".join(self.get_input_signals_names())
            self.axes.set_title(t, fontsize=10)
            
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
            self.lines[id].set_xdata(x)
        
        self.lengths[id] = len(x)
        
        if self.limits is None:
            self.limits = numpy.array([min(x), max(x), min(y), max(y)])
        else:
            self.limits[0] = min(self.limits[0], min(x))
            self.limits[1] = max(self.limits[1], max(x))
            self.limits[2] = min(self.limits[2], min(y))
            self.limits[3] = max(self.limits[3], max(y))
            

        #self.limits = map(float, self.limits)
        
    def update(self):
        self.limits = None
        
        start = time.clock()

        if self.figure is None:
            self.init_figure()    

        pylab.figure(self.figure.number)
        
        for i in range(self.num_input_signals()):
            value = self.input[i]
            if value is None:
                raise BadInput('Input is None (did you forget a |sync|?)', self, i)
            elif isinstance(value, tuple):
                if len(value) != 2:
                    raise BadInput('Expected tuple of length 2 instead of %d.' % 
                                   len(value), self, i)
                
                xo = value[0]
                yo = value[1]
                
                if xo is None or yo is None:
                    raise BadInput('Invalid members of tuple', self, i)
                    
                x = numpy.array(xo)
                y = numpy.array(yo)
                
                # X must be one-dimensional
                if len(x.shape) > 1:
                    raise BadInput('Bad x vector w/shape %s.' % str(x.shape), self, i)
                
                # y should be of dimensions ...?
                if len(y.shape) > 2:
                    raise BadInput('Bad shape for y vector %s.' % str(y.shape), self, i)
                
                if len(x) != y.shape[0]:
                    raise BadInput('Incompatible dimensions x: %s, y: %s' % 
                                   (str(x.shape), str(y.shape)))
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
                    self.plot_one(id, x, yk, self.config.format)
            # TODO: check that if one has time vector, also others have it

        if self.limits is not None:
            
            if self.config.x_min is not None:
                self.limits[0] = self.config.x_min
            if self.config.x_max is not None:
                self.limits[1] = self.config.x_max
            if self.config.y_min is not None:
                self.limits[2] = self.config.y_min
            if self.config.y_max is not None:
                self.limits[3] = self.config.y_max
                
            if self.config.symmetric:
                if self.config.y_min is not None or self.config.y_max is not None:
                    raise BadConfig('Cannot specify symmetric together with'
                                    'y_min or y_max.', self, 'symmetric')
                
                M = max(abs(self.limits[2:4]))
                self.limits[2] = -M
                self.limits[3] = M
            
            # leave some space above and below
            self.limits[2] *= 1.1
            self.limits[3] *= 1.1
                
            self.axes.axis(self.limits)
            
        
        
        if self.legend_handle is None:
            legend = self.config.legend
            if legend:
                self.legend_handle = self.axes.legend(*legend,
                    loc='upper right', handlelength=1.5, markerscale=2,
                    labelspacing=0.03, borderpad=0, handletextpad=0.03,
                    borderaxespad=1)
       
        plotting = time.clock() - start
    
        start = time.clock()
        f = tempfile.NamedTemporaryFile(suffix='.png')
        temp_file = f.name
        
        pylab.savefig(temp_file)
        saving = time.clock() - start
        
        
        start = time.clock()    
        im = Image.open(temp_file)
        im = im.convert("RGB")
        pixel_data = numpy.asarray(im)
        reading = time.clock() - start
       
        if False: 
            print "plotting: %dms  saving: %dms  reading: %dms" % (
                plotting * 1000, saving * 1000, reading * 1000)
        
        self.output.rgb = pixel_data
        
        if not self.config.keep:
            pylab.close(self.figure.number)
            self.figure = None


