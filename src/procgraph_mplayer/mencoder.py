import numpy
import subprocess

from procgraph import Block
from procgraph.block_utils import make_sure_dir_exists, check_rgb_or_grayscale
import os
from procgraph.block_utils.file_io import expand

# TODO: detect an error in Mencoder (perhaps size too large)
# TODO: cleanup processes after finishing


class MEncoder(Block):
    ''' Encodes a video stream using ``mencoder``.
    
    Note that allowed codec and bitrate depend on your version of mencoder.
    '''
    Block.alias('mencoder')

    Block.input('image', 'Either a HxWx3 uint8 numpy array representing '
                         'an RGB image, or a HxW representing grayscale. ')

    Block.config('file', 'Output file (AVI format)')
    Block.config('fps', 'Framerate of resulting movie. If not specified, '
                        'it will be guessed from data.', default=None)
    Block.config('fps_safe', 'If the frame autodetect gives strange results, '
                             'we use this safe value instead.', default=10)

    Block.config('convert_to_mp4', 'If true, use ffmpeg to convert to '
                 'web-ready mp4.', default=True)

    Block.config('vcodec', 'Codec to use.', default='mpeg4')
    Block.config('vbitrate', 'Bitrate -- default is reasonable.',
                             default=2000000)
    Block.config('quiet', "If True, suppress mencoder's messages",
                 default=True)
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
            format = 'y8' #@ReservedAssignment
        else:
            format = 'rgb24' #@ReservedAssignment

        # guess the fps if we are not given the config
        if self.config.fps is None:
            delta = self.buffer[-1][0] - self.buffer[0][0]

            if delta == 0:
                timestamps = [x[0] for x in self.buffer]
                self.debug('Got 0 delta: timestamps: %s' % timestamps)
                fps = 0
            else:
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

        self.filename = expand(self.config.file)
        self.tmp_filename = self.filename + '.active'

        make_sure_dir_exists(self.filename)

        self.info('Writing %dx%d %s video stream at %.1f fps to %r.' %
                  (self.width, self.height, format, fps, self.filename))

        args = ['mencoder', '/dev/stdin', '-demuxer', 'rawvideo',
                '-rawvideo', 'w=%d:h=%d:fps=%f:format=%s' %
                (self.width, self.height, fps, format),
                '-ovc', 'lavc', '-lavcopts',
                 'vcodec=%s:vbitrate=%d' % (vcodec, vbitrate),
                  # Currently broken :-(
                  #'-of', 'lavf', '-lavfopts', 'format=mp4',
                 '-o', self.tmp_filename]
        self.debug('command line: %s' % " ".join(args))

        if self.config.quiet:
            self.process = subprocess.Popen(args,
                stdin=subprocess.PIPE, stdout=open('/dev/null'),
                                       stderr=open('/dev/null'),)
        else:
            self.process = subprocess.Popen(args=args, stdin=subprocess.PIPE)

        if self.config.timestamps:
            self.timestamps_file = open(self.filename + '.timestamps', 'w')

    def finish(self):
        if self.process is not None:
            if os.path.exists(self.filename):
                os.unlink(self.filename)
            os.rename(self.tmp_filename, self.filename)

        if self.config.convert_to_mp4:
            convert_to_mp4(self.filename)

    def write_value(self, timestamp, image):
        # very important! make sure we are using a reasonable array
        if not image.flags['C_CONTIGUOUS']:
            image = numpy.ascontiguousarray(image)
        self.process.stdin.write(image.data)
        self.process.stdin.flush()

        if self.config.timestamps:
            self.timestamps_file.write('%s\n' % timestamp)
            self.timestamps_file.flush()


def convert_to_mp4(filename):
    """ Creates a web-ready mp4 using ffmpeg """

    basename, ext = os.path.splitext(filename)
    if ext == 'mp4':
        raise Exception('Need a file that does not end in .mp4 (%r)' %
                        filename)
    mp4 = basename + '.mp4'

    # XXX: make random file
    tmp = basename + '.firstpass.mp4'

    if not os.path.exists(filename):
        raise Exception("Filename %s does not exist." % filename)

    if (os.path.exists(mp4) and
        (os.path.getmtime(mp4) > os.path.getmtime(filename))):
        return

    cmds = ['ffmpeg', '-y', '-i', filename,
            '-vcodec', 'libx264', '-vpre', 'slow',
            '-crf', '22', '-threads', '0', tmp]

    print(" ".join(cmds))
    subprocess.check_call(cmds)

    # TODO: check file exists
    try:
        subprocess.check_call(['qt-faststart', tmp, mp4])
        print('Succesfull call of qt-faststart.')
    except Exception as e:
        print("Could not call qt-faststart: %s" % e)

        try:
            # easy_install qtfaststart
            subprocess.check_call(['qtfaststart', tmp, mp4])
            print('Succesfull call of qtfaststart.')
        except Exception as e:
            print("Could not call qtfaststart: %s" % e)

            print("The file will not be ready for streaming.")
            os.rename(tmp, mp4)

    if os.path.exists(tmp):
        os.unlink(tmp)
