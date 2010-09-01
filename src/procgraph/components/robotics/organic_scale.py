
from procgraph import Block, block_alias, block_config, block_input, block_output
from procgraph.components.images.copied_from_reprep import skim_top_and_bottom, \
    skim_top

from numpy import maximum, minimum
import numpy

class OrganicScale(Block):
    block_alias('organic_scale')
    
    block_input('value')
    block_output('value_scaled')
        
    block_config('skim', default=5)
    block_config('skim_hist', default=5)
    block_config('hist', default=100)
    block_config('tau', default=0.1)

    def init(self):
        ###
        self.define_input_signals(['value'])
        self.define_output_signals(['value_scaled'])
        self.config.skim = 5
        self.config.skim_hist = 5
        self.config.hist = 100
        self.config.tau = 0.1
        ###
        self.state.max = []
        self.state.M = None
        
    def update(self):
        y = numpy.array(self.input.value)
        # first skim it
        y = skim_top_and_bottom(y, self.config.skim)
        # put the max in the history
        self.state.max.insert(0, max(abs(y)))
        # prune the history
        self.state.max = self.state.max[:self.config.hist]
        # get the history percent
        M = max(skim_top(numpy.array(self.state.max), self.config.skim_hist))
        
        if self.state.M is None:
            self.state.M = M
        else:
            self.state.M += self.config.tau * (M - self.state.M)
            
        print self.state.M
        
        y = minimum(y, self.state.M)
        y = maximum(y, -self.state.M)
        
        y = y / self.state.M
        self.output.value_scaled = y
             
            
