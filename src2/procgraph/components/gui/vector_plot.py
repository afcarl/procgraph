
from pylab import ion, draw, plot
from procgraph.core.block import Block
from procgraph.core.registrar import register_block_class



class SimplePlot(Block):
    ''' Just plots the vector instantaneously '''

    def init(self):
        #self.set_config_default('gain', 1)
        self.define_input_signals([0])
        self.define_output_signals([])
        self.line = None
        
    def update(self):
        ion()

        x = self.get_input(0) 
        
        if self.line is None:
            self.line, = plot(range(len(x)), x)
        else:
            self.line.set_ydata(x)
            draw()
        


register_block_class('plot', SimplePlot)
