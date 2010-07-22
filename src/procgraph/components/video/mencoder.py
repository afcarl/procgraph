# OS X: install from http://ffmpegx.com/download.html
from procgraph.core.block import Block
import subprocess
from procgraph.core.registrar import default_library
 
class MEncoder(Block):
    ''' Encodes a video stream.
    
    Input: H x W x 3  uint8  numpy array representing RGB image.
    Config: 
        - file 
        - vcodec   mpeg4
        - vbitrate 1000000
    
    Note that allowed codec and bitrate depend on your version of mencoder.
    ''' 
     
    def init(self):
        #self.set_config_default()
        self.process = None
        self.define_input_signals(["image"])
        self.define_output_signals([])
        self.file = self.get_config('file') 
        self.set_config_default('vcodec', 'mpeg4')
        self.set_config_default('vbitrate', 1000000)
        
    def update(self):
        image = self.get_input(0)
        
        if len(image.shape) != 3 or image.shape[2] != 3 or image.dtype != 'uint8':
            raise Exception('Expected uint8 RGB image, got %s %s.' % \
                            (str(image.shape), image.dtype))
        
        h,w,depth=image.shape
        fps=10
        
        if self.process is None:
            vcodec = self.get_config('vcodec')
            vbitrate = self.get_config('vbitrate')
            
            args = ['mencoder', '/dev/stdin', '-demuxer', 'rawvideo',
                    '-rawvideo', 'w=%d:h=%d:fps=%d:format=rgb24' % (w,h,fps),
                    '-ovc','lavc','-lavcopts',
                     'vcodec=%s:vbitrate=%d' %(vcodec, vbitrate),
                     '-o', self.file]
            print 'Command line: \n %s' % " ".join(args)
            self.process = subprocess.Popen(args=args,stdin=subprocess.PIPE,
                                            #stderr=subprocess.PIPE,
                                            #stdout=subprocess.PIPE
                                            )
            
        self.process.stdin.write(image.data)
        self.process.stdin.flush()

default_library.register('mencoder',  MEncoder)
