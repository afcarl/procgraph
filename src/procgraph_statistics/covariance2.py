from procgraph import Block
import os
from astatsa.mean_covariance.mean_cov import MeanCovariance
from compmake.utils.safe_pickle import safe_pickle_load, safe_pickle_dump



class CovarianceRemember(Block):
    """ Quick hack to remember covariance across executions """
    Block.alias('covariance_rem')
    
    Block.config('filename', default='cov_remember.pickle') 
    Block.input('x')
    Block.output('cov_x')
    
    def init(self):
        filename = self.config.filename
        if os.path.exists(filename):
            self.info('Loading state from filename %r' % filename)
            self.state = safe_pickle_load(filename)
        else:
            self.state = MeanCovariance()
    
    def update(self):
        x = self.input.x.astype('float32')
        self.state.update(x)
        
        self.output.cov_x = self.state.get_covariance()
        safe_pickle_dump(self.state, self.config.filename)  # @UndefinedVariable
