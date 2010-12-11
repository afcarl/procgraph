import sys
from os import environ as env

try:
    from termcolor import colored as termcolor_colored #@UnresolvedImport
except:
    sys.stderr.write('procgraph can make use of the package "termcolor". '
                     'Please install it.\n')
    def termcolor_colored(x, color=None, on_color=None, attrs=None): #@UnusedVariable
        ''' emulation of the termcolor interface '''
        return x

def colored(x, color=None, on_color=None, attrs=None):
    colorize = True
    # TODO: no colorize during tests
    if colorize: #@UndefinedVariable
        return termcolor_colored(x, color, on_color, attrs)
    else:
        return x


try:
    from setproctitle import setproctitle #@UnresolvedImport @UnusedImport
except:
    sys.stderr.write('procgraph can make use of the package "setproctitle". '
                     'Please install it.\n')
    def setproctitle(x):
        ''' emulation of the setproctitle interface '''
        pass
    
screen_columns = None
def get_screen_columns():
    module = sys.modules[__name__]
    if  module.screen_columns is None:
        max_x, max_y = getTerminalSize() #@UnusedVariable
        module.screen_columns = max_x
        
    return module.screen_columns

def getTerminalSize():
    '''
    max_x, max_y = getTerminalSize()
    '''
    import os
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return None
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)
    return int(cr[1]), int(cr[0])

#    
#def clean_console_line(stream):
#    s = '\r' + (' ' *  (get_screen_columns() - 2)) + '\r'
#    stream.write(s)
#    pass
    
def warning(string):
    write_message(string, lambda x: 'pg: ' + colored(x, 'magenta'))
    
def error(string):
    write_message(string, lambda x: 'pg: ' + colored(x, 'red'))
    
def user_error(string):
    write_message(string, lambda x: 'pg: ' + colored(x, 'red'))
    
def info(string):
    write_message(string, lambda x: 'pg: ' + colored(x, 'green'))
    
def debug(string):
    write_message(string,
                  lambda x: 'pg: ' + colored(x, 'cyan', attrs=['dark']))
    
def write_message(string, formatting):
    sys.stdout.flush()
    string = str(string)
    
    #clean_console_line(sys.stderr)
    lines = string.split('\n')
    if len(lines) == 1:
        sys.stderr.write(formatting(lines[0]) + '\n')
    else:
        for i, l in enumerate(lines): #@UnusedVariable
            #if i == 1: 
            #    l = '- ' + l
            #else:
            #    l = '  ' + l
            sys.stderr.write(formatting(l) + '\n')    
    
    sys.stderr.flush() 

    
def semantic_warning(error, element):
    msg = str(error) + '\n' + str(element.where)
    warning(msg)
