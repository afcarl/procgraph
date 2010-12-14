from procgraph import Block

# We can still use blocks as normal functions
from tutorial9_blocks import choose


class Psychedelic(Block):
    Block.alias('psychedelic')
    
    Block.input('rgb', 'An RGB image.')
    
    Block.output('processed', 'The processed image.')
    
    
    def init(self):
        self.channel = 0
        
    def update(self):
        self.channel = (self.channel + 1) % 3
        self.output.processed = choose(self.input.rgb, self.channel)
    