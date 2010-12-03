import os

def make_sure_dir_exists(file):
    ''' Makes sure that the path to file exists, but creating directories. '''
    dir = os.path.dirname(file)
    # dir == '' for current dir
    if dir != '' and not os.path.exists(dir):
        os.makedirs(dir) 


def expand(filename):
    ''' Expands environment variables in the filename. '''
    filename = os.path.expandvars(filename)
    filename = os.path.expanduser(filename)
    return filename


    
