import subprocess, os, numpy

from procgraph import Block, BadConfig


from procgraph.core.visualization import info  as info_main, error as error_main 

def info(s):
    info_main('procgraph_pil/text: %s' % s)
def error(s):
    error_main('procgraph_pil/text: %s' % s)
    

from . import ImageDraw, ImageFont
from .pil_conversions import Image_from_array


class Text(Block):
    ''' This block provides text overlays over an image. 
    
    You should provide a list of dictionary in the configuration variable 
     ``texts``. Each dictionary in the list describes one piece of text.
     
    An example of valid configuration is the following: ::
    
        text.texts = [{string: "raw image", position: [10,30], halign: left, 
                      color: black, bg: white }]
    
    The meaning of the fields is as follow:
    
    ``string``
      Text to display. See the section below about keyword expansion.
      
    ``position``
      Array of two integers giving the position of the text in the image
      
    ``color``
      Text color. It can be a keyword color or an hexadecimal string 
      (``white`` or ``#ffffff``).
      
    ``bg``
      background color
    
    ``halign``
      Horizontal alignment. 
      Choose between ``left`` (default), ``center``, ``right``.
      
    ``valign``
      Vertical alignment. 
      Choose between ``top`` (default), ``middle``, ``center``.
    
    ``size``
      Font size in pixels
      
    ``font``
      Font family. Must be a ttf file (``Arial.ttf``)

    **Expansion**: Also we expand macros in the text using ``format()``. 
    The available keywords are:
    
    ``frame``
      number of frames since the beginning
       
    ``time``
      seconds since the beginning of the log

    ``timestamp``
      absolute timestamp
    
    '''
    
    Block.alias('text')
    
    Block.config('texts', 'Text specification (see block description).')
    
    Block.input('rgb', 'Input image.')
    Block.output('rgb', 'Output image with overlaid text.')
    
    def init(self): 
        self.state.first_timestamp = None 
    
    def update(self):
        
        # TODO: add check
        if self.state.first_timestamp is None:
            self.state.first_timestamp = self.get_input_timestamp(0)
            self.state.frame = 0
        else:
            self.state.frame += 1
        # Add stats
        macros = {}
        macros['timestamp'] = self.get_input_timestamp(0)
        macros['time'] = \
            self.get_input_timestamp(0) - self.state.first_timestamp
        macros['frame'] = self.state.frame
        
        rgb = self.input.rgb
        im = Image_from_array(rgb)
        draw = ImageDraw.Draw(im)
        
        # {string: "raw image", position: [10,30], halign: left, 
        # color: black, bg: white  }
        if not isinstance(self.config.texts, list):
            raise BadConfig('Expected list', self, 'texts')
        
        for text in self.config.texts:
            text = text.copy()
            if not 'string' in text:
                raise BadConfig('Missing field "string" in text spec %s.' % \
                                text.__repr__(), self, 'texts')
            text['string'] = Text.replace(text['string'], macros)
            p = text['position']
            if p[0] == 'middle':
                p[0] = rgb.shape[1] / 2
            if p[1] == 'middle':
                p[1] = rgb.shape[0] / 2
            if p[0] < 0: 
                p[0] = rgb.shape[1] + p[0]
            if p[1] < 0: 
                p[1] = rgb.shape[0] + p[1]
                
            process_text(draw, text)
        
        out = im.convert("RGB")
        pixel_data = numpy.asarray(out)
        
        self.output.rgb = pixel_data
    
    @staticmethod   
    def replace(s, macros):
        ''' Expand macros in the text. '''
        return s.format(**macros)

# cache of fonts

def find_file(font_name):
    try:
        #pattern = '*%s*.ttf' % font_name
        pattern = '%s.ttf' % font_name
        a = subprocess.Popen(['locate', pattern], stdout=subprocess.PIPE); 
        lines = a.stdout.read();
        if len(lines) == 0:
            error('Cannot find a file matching the pattern %r.' % pattern)
            return None
        options = lines.split('\n')
        guess = options[0]
        info('Found %d matches for %s, using  "%s".' % 
             (len(options), pattern, guess))
        return guess
    except Exception as e:
        error('Cannot run "locate": %s' % e)
        return None 
    
fonts = {}
def get_font(name, size):
    tuple = (name, size)
    if not fonts.has_key(tuple):
        filename = name + '.ttf'
        if not os.path.exists(filename):
            info('Could not find file %r, trying "locate"...' % filename)
            name = find_file(name)
            if name is None:
                error('Could not find %r anywhere, using default font' % name)
                fonts[tuple] = ImageFont.load_default()
            else:
                fonts[tuple] = ImageFont.truetype(name, size)
        else:
            info('Using font in file %s' % filename)
            fonts[tuple] = ImageFont.truetype(filename, size)
    
    return fonts[tuple]


def process_text(draw, t):
    position = t['position']
    string = t['string']
    color = t.get('color', '#aaaaaa')
    bg = t.get('bg', None)
    size = t.get('size', 15)
    fontname = t.get('font', 'Arial')
    font = get_font(fontname, size)
    
    tw, th = font.getsize(string)
    x, y = position[0], position[1]
     
    
    halign = t.get('halign', 'left')
    valign = t.get('valign', 'top')
    
    
    if halign == 'left':
        pass
    elif halign == 'right':
        x -= tw
    elif halign == 'center':
        x -= tw / 2
    else:
        print('Uknown horizontal-align key %s' % halign)

    if valign == 'top':
        pass
    elif valign == 'bottom':
        y -= th
    elif valign == 'middle':
        y -= th / 2
    else:
        print('Uknown vertical-align key %s' % valign)

    if bg:
        for a in [ [-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1],
                   [-1, +1], [1, 1], [1, -1]]:
            draw.text([x + a[0], y + a[1]], string, fill=bg, font=font)
    
    draw.text([x, y], string, fill=color, font=font)
    
    
