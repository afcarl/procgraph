from contracts import contract, new_contract

class DrawToken():
    def __init__(self, position, text):
        self.position = position
        self.text = text
    def __repr__(self):
        return "DT([%1.f,%1.f], %r)" % (self.position[0], self.position[1], self.text)
        
new_contract('drawtoken', DrawToken)

def tokenize(s):
    s = s.replace('\n', " ")
    tokens = s.split(" ")
    tokens = [t for t in tokens if t]
    return tokens

@contract(text=str, line_width='>0', line_scale='>1', returns='tuple(list(drawtoken), tuple(float,float))')
def format_paragraph(text, font, line_width, line_scale=1.2):
    """ Returns a list of drawtokens and width/height """
    tokens = tokenize(text)
    
    def width_from_token(token):
        w, _ = font.getsize(token)
        return w
    
    space_width, _ = font.getsize('n')
    _, line_height = font.getsize('l')
    line_height *= line_scale
    
    #print('line width (max): %s' % line_width)
    #print('line height: %s' % line_height)
    #print('space_width: %s' % space_width)
    lines = split_in_lines(tokens, width_from_token, line_width, space_width)
    #print('Obtained %d lines: %s' % (len(lines), lines))
    out = []
    max_w = 0.0
    for i, l in enumerate(lines):
        cur_y = i * line_height
        dts, w = format_line(line=l, width_from_token=width_from_token,
                                 ybase=cur_y, space_width=space_width)
        assert w<=line_width, (w, line_width)
        max_w = max(max_w, w)
        out.extend(dts)
        
    height = len(lines) * line_height
    return out, (height, max_w)
    
@contract(line='list(str)', returns='tuple(list(drawtoken), >=0)')
def format_line(line, width_from_token, ybase, space_width):
    out = []
    cur_x = 0.0
    for token in line:
        #print('cur: %s token: %r w: %r' % (cur_x, token, wt))
        o = DrawToken(position=(ybase, cur_x), text=token)
        out.append(o)
        wt = width_from_token(token)
        cur_x += wt + space_width
        
    if line:
        cur_x -= space_width
    return out, cur_x
        
@contract(returns='list(list(str))')
def split_in_lines(tokens, width_from_token, line_width, space_width):
    lines = []
    cur_line = [] 
    cur_line_width = 0.0 
    for token in tokens:
        token_width = width_from_token(token)
        too_long = cur_line_width + token_width + space_width > line_width
        if too_long:
            lines.append(cur_line)
            cur_line_width = 0.0
            cur_line = []
        cur_line.append(token)
        cur_line_width += token_width + space_width
    if cur_line:
        lines.append(cur_line)
    return lines
            