# OS X: install from http://ffmpegx.com/download.html
import subprocess 

from procgraph import Block

from procgraph.components  import check_rgb_or_grayscale
from procgraph.core.model_loadsave import make_sure_dir_exists
 
 
class MEncoder(Block):
    ''' Encodes a video stream using ``mencoder``.
    
    Note that allowed codec and bitrate depend on your version of mencoder.
    ''' 
    Block.alias('mencoder')
    
    Block.input('image', 'H x W x 3  uint8 numpy array representing an RGB image.') 
    
    Block.config('file', 'Output file (AVI format.)')
    Block.config('fps', 'Framerate of resulting movie.', default=10)
    Block.config('vcodec', 'Codec to use.', default='mpeg4')
    Block.config('vbitrate', 'Bitrate -- default is reasonable.', default=2000000)
    Block.config('quiet', "If True, suppress mencoder's messages", default=True)
    Block.config('timestamps', "If True, also writes <file>.timestamps that"
        " includes a line with the timestamp for each frame", default=True)
    
    def init(self): 
        self.process = None
        self.define_input_signals(["image"])
        self.define_output_signals([])
        
        
    def update(self):
        check_rgb_or_grayscale(self, 0)
        
        image = self.input.image        
        h, w = image.shape[0:2]
        fps = self.config.fps
        
        if self.process is None:
            vcodec = self.config.vcodec
            vbitrate = self.config.vbitrate
        
            make_sure_dir_exists(self.config.file)
                
            format = {2: 'y8', 3: 'rgb24'}[len(image.shape)]
            
            args = ['mencoder', '/dev/stdin', '-demuxer', 'rawvideo',
                    '-rawvideo', 'w=%d:h=%d:fps=%d:format=%s' % (w, h, fps, format),
                    '-ovc', 'lavc', '-lavcopts',
                     'vcodec=%s:vbitrate=%d' % (vcodec, vbitrate),
                     '-o', self.config.file]
            self.info('command line: %s' % " ".join(args))
                     
            if self.config.quiet:
                self.process = subprocess.Popen(args,
                    stdin=subprocess.PIPE, stdout=open('/dev/null'),
                                                stderr=open('/dev/null'),)
            else:
                self.process = subprocess.Popen(args=args, stdin=subprocess.PIPE)

            if self.config.timestamps:
                self.timestamps_file = open(self.config.file + '.timestamps', 'w') 

            
        self.process.stdin.write(image.data)
        self.process.stdin.flush()

        if self.config.timestamps:
            self.timestamps_file.write('%s\n' % self.get_input_timestamp(0))
            self.timestamps_file.flush()
