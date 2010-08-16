import subprocess
import os
import numpy

from PIL import ImageDraw, ImageFont

from procgraph.core.block import Block
from procgraph.core.registrar import default_library
from procgraph.components.pil.pil_conversions import Image_from_array


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
        
        out = im.convert("RGB")
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
    return lines.split('\n')[0]

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
    
    
