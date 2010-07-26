# OS X: install from http://ffmpegx.com/download.html
import subprocess
import numpy
from procgraph.core.block import Block
from procgraph.core.registrar import default_library
from procgraph.core.exceptions import BadInput
 
def check_rgb_or_grayscale(block, input):
    ''' Checks that the selected input is either a grayscale or RGB image.
        That is, a numpy array of uint8 either H x W or H x W x 3. 
        Raises BadInput if it is not. 
    ''' 
    image = block.get_input(input)
    if not isinstance(image, numpy.ndarray):
        raise BadInput('Expected RGB or grayscale, this is not even a '+
            +'numpy array: %s' % image.__class__.__name__, block, input)
    if image.dtype != 'uint8':
        raise BadInput('Expected an image, got an array %s %s.' % \
                            (str(image.shape), image.dtype), block, input)
    shape = image.shape
    if len(shape) == 3:
        if shape[2] != 3:
            raise BadInput('Bad shape for image: %s' % str(shape))
    elif len(shape) == 2:
        pass
    else:
        raise BadInput('Bad shape for image: %s' % str(shape))
        
 
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
        self.set_config_default('fps', 10) 
        self.set_config_default('vcodec', 'mpeg4')
        self.set_config_default('vbitrate', 1000000)
        
    def update(self):
        check_rgb_or_grayscale(self, 0)
        
        image = self.get_input(0)        
        h, w = image.shape[0:2]
        fps = self.get_config('fps')
        
        if self.process is None:
            vcodec = self.get_config('vcodec')
            vbitrate = self.get_config('vbitrate')
            
            format = {2: 'y8', 3: 'rgb24'}[len(image.shape)]
            
            args = ['mencoder', '/dev/stdin', '-demuxer', 'rawvideo',
                    '-rawvideo', 'w=%d:h=%d:fps=%d:format=%s' % (w,h,fps,format),
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
