import subprocess 

from procgraph import Block
from procgraph.block_utils import make_sure_dir_exists, check_rgb_or_grayscale
 
# TODO: detect an error in Mencoder (perhaps size too large)
# TODO: cleanup processes after finishing

class MEncoder(Block):
    ''' Encodes a video stream using ``mencoder``.
    
    Note that allowed codec and bitrate depend on your version of mencoder.
    ''' 
    Block.alias('mencoder')
    
    Block.input('image', 'Either a HxWx3 uint8 numpy array representing '
                         'an RGB image, or a HxW representing grayscale. ') 
    
    Block.config('file', 'Output file (AVI format.)')
    Block.config('fps', 'Framerate of resulting movie. If not specified, '
                        'it will be guessed from data.', default=None)
    Block.config('fps_safe', 'If the frame autodetect gives strange results, '
                             'we use this safe value instead.', default=10)
                        
    Block.config('vcodec', 'Codec to use.', default='mpeg4')
    Block.config('vbitrate', 'Bitrate -- default is reasonable.',
                             default=2000000)
    Block.config('quiet', "If True, suppress mencoder's messages", default=True)
    Block.config('timestamps', "If True, also writes <file>.timestamps that"
        " includes a line with the timestamp for each frame", default=True)
    
    def init(self): 
        self.process = None 
        self.buffer = []
        
    def update(self):
        check_rgb_or_grayscale(self, 0)
        
        # Put image in a buffer -- we don't use it right away
        image = self.get_input(0)
        timestamp = self.get_input_timestamp(0)
        self.buffer.append((timestamp, image))
            
        if self.process is None:
            self.try_initialization()
            
        if self.process is not None:
            # initialization was succesful
            while self.buffer:
                timestamp, image = self.buffer.pop(0)
                self.write_value(timestamp, image) 
                
            
    def try_initialization(self):
        # If we don't have at least two frames, continue
        if len(self.buffer) < 2:
            return
        
        # Get height and width from first image
        first_image = self.buffer[0][1]
        
        self.shape = first_image.shape
        self.height = self.shape[0]
        self.width = self.shape[1]
        self.ndim = len(self.shape)
        if self.ndim == 2:
            format = 'y8'
        else:
            format = 'rgb24' 
        
        # guess the fps if we are not given the config
        if self.config.fps is None:
            delta = self.buffer[-1][0] - self.buffer[0][0]
            fps = (len(self.buffer) - 1) / delta
            
            
            # Check for very wrong results
            if not (3 < fps < 60):
                self.error('Detected fps is %.2f; this seems strange to me,' 
                           ' so I will use the safe choice fps = %.2f.' % 
                           (fps, self.config.fps_safe))
                fps = self.config.fps_safe
        else:
            fps = self.config.fps
        
        
        vcodec = self.config.vcodec
        vbitrate = self.config.vbitrate
    
        make_sure_dir_exists(self.config.file)
            
        args = ['mencoder', '/dev/stdin', '-demuxer', 'rawvideo',
                '-rawvideo', 'w=%d:h=%d:fps=%f:format=%s' % 
                (self.width, self.height, fps, format),
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

    def write_value(self, timestamp, image):            
        self.process.stdin.write(image.data)
        self.process.stdin.flush()

        if self.config.timestamps:
            self.timestamps_file.write('%s\n' % timestamp)
            self.timestamps_file.flush()
