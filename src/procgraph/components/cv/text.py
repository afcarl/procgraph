from procgraph.core.block import Block
from PIL import Image,ImageDraw, ImageFont
import subprocess
import os
import numpy
from procgraph.core.registrar import default_library


class Text(Block):
    ''' This blocks provides text overlays over an RGB image. '''
    
    def init(self):
        self.define_input_signals(['rgb'])
        self.define_output_signals(['rgb'])
    
    def update(self):
        
        texts = self.get_config('texts')
        
        
        rgb = self.get_input(0)

        im = Image_from_array(rgb)
        draw = ImageDraw.Draw(im)
        
        # {string: "raw image", position: [10,30], halign: left, 
        # color: black, bg: white  }
        for text in texts:
            process_text(draw, text)
        
        out =  im.convert("RGB")
        pixel_data = numpy.asarray(out)
        
        self.set_output(0, pixel_data)
            
            

default_library.register('text', Text)


# cache of fonts

def find_file(filename):
    a = subprocess.Popen(['locate', filename], stdout=subprocess.PIPE); 
    lines = a.stdout.read();
    if len(lines) == 0:
        print('Cannot find filename "%s" anywhere' % filename)
        return None
    return lines.split()[0]

fonts = {}
def get_font(name, size):
    tuple = (name, size)
    if not fonts.has_key(tuple):
        if not os.path.exists(name):
            print('Could not find file "%s", searching' % name)
            name = find_file(name)
            if name is None:
                print('Could not find file "%s" anywhere, using default font' % name)
                fonts[tuple] = ImageFont.load_default()
            else:
                print('Using file  "%s".' % name)
                fonts[tuple] = ImageFont.truetype(name, size)
        else:
            fonts[tuple] = ImageFont.truetype(name, size)
    
    return fonts[tuple]


def process_text(draw, t):
    position = t['position']
    string = t['string']
    color = t.get('color', '#aaaaaa')
    bg = t.get('bg', None)
    size = t.get('size', 15)
    fontname = t.get('font', 'Arial.ttf')
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
        for a in [ [-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [-1, +1], [1, 1], [1, -1]]:
            draw.text([x + a[0], y + a[1]], string, fill=bg, font=font)
    
    draw.text([x, y], string, fill=color, font=font)
    
    
def Image_from_array(a):
    ''' Converts an image in a numpy array to an Image instance.
        Accepts:  h x w      255  interpreted as grayscale
        Accepts:  h x w x 3  255  rgb  
        Accepts:  h x w x 4  255  rgba '''
        
    #require_array(a)

    if not a.dtype == 'uint8':
        raise ValueError('I expect dtype to be uint8, got "%s".' % a.dtype)
    
    if len(a.shape) == 2:
        height, width = a.shape
        rgba = numpy.zeros((height, width, 4), dtype='uint8')
        rgba[:, :, 0] = a
        rgba[:, :, 1] = a
        rgba[:, :, 2] = a
        rgba[:, :, 3] = 255
    elif len(a.shape) == 3:
        height, width = a.shape[0:2]
        depth = a.shape[2]
        rgba = numpy.zeros((height, width, 4), dtype='uint8')
        if not depth in [3, 4]:
            raise ValueError('Unexpected shape "%s".' % str(a.shape))
        rgba[:, :, 0:depth] = a[:, :, 0:depth]
        if depth == 3:
            rgba[:, :, 3] = 255
    else:
        raise ValueError('Unexpected shape "%s".' % str(a.shape))
    
    #require_shape((gt(0), gt(0), 4), rgba) 
    
    
    im = Image.frombuffer("RGBA", (width, height), rgba.data,
                           "raw", "RGBA", 0, 1)
    return im