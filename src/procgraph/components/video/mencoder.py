# OS X: install from http://ffmpegx.com/download.html
import subprocess 


from procgraph import Block, block_config, block_input 

from procgraph.components  import check_rgb_or_grayscale
from procgraph.core.model_loadsave import make_sure_dir_exists
from procgraph.components.basic import register_block
 
 
class MEncoder(Block):
    ''' Encodes a video stream using ``mencoder``.
    
    Note that allowed codec and bitrate depend on your version of mencoder.
    ''' 
    block_input('image', 'H x W x 3  uint8 numpy array representing an RGB image.') 
    
    block_config('file', 'Output file (AVI format.)')
    block_config('fps', 'Framerate of resulting movie.', default=10)
    block_config('vcodec', 'Codec to use.', default='mpeg4')
    block_config('vbitrate', 'Bitrate -- default is reasonable.', default=1000000)
    block_config('quiet', "If True, suppress mencoder's messages", default=True)
    
    def init(self):
        #self.set_config_default()
        self.process = None
        self.define_input_signals(["image"])
        self.define_output_signals([])
        # XXX: check with the state
        self.file = self.config.file
        self.config.fps = 10 
        self.config.vcodec = 'mpeg4'
        self.config.vbitrate = 1000000
        self.config.quiet = True
        
    def update(self):
        check_rgb_or_grayscale(self, 0)
        
        image = self.input.image        
        h, w = image.shape[0:2]
        fps = self.config.fps
        
        if self.process is None:
            vcodec = self.config.vcodec
            vbitrate = self.config.vbitrate
        
            make_sure_dir_exists(self.file)
                
            format = {2: 'y8', 3: 'rgb24'}[len(image.shape)]
            
            args = ['mencoder', '/dev/stdin', '-demuxer', 'rawvideo',
                    '-rawvideo', 'w=%d:h=%d:fps=%d:format=%s' % (w, h, fps, format),
                    '-ovc', 'lavc', '-lavcopts',
                     'vcodec=%s:vbitrate=%d' % (vcodec, vbitrate),
                     '-o', self.file]
            self.info('command line: %s' % " ".join(args))
                     
            if self.config.quiet:
                self.process = subprocess.Popen(args,
                    stdin=subprocess.PIPE, stdout=open('/dev/null'),
                                                stderr=open('/dev/null'),)
            else:
                self.process = subprocess.Popen(args=args, stdin=subprocess.PIPE)


            
        self.process.stdin.write(image.data)
        self.process.stdin.flush()

register_block(MEncoder, 'mencoder')
