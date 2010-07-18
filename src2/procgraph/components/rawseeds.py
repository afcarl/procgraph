from procgraph.core.block import Block
import glob
import os

class RawseedsLogReader(Block):
    
    def init(self, directory, format='png'):
        all_files = glob.glob(os.path.join(directory, '*_*.*.%s' % png))
                              
    def has_more(self):
        pass
             
    def update(self):
        pass
