import re
import os


def expand_environment(s):
    """ Expands a string using environment variables.
    Throws an exception (ValueError) if the variable is not found.
    
    Example: "${HOME}/.zshrc" -> "/home/youruser/.zshrc"
    """
    while True:
        m =  re.match('(.*)\$\{(\w+)\}(.*)', s)
        if not m:
            return s
        before = m.group(1)
        var = m.group(2)
        after = m.group(3)
        if not var in os.environ:
            raise ValueError('Could not find environment variable "%s".' % var)
        sub = os.environ[var]
        s = before+sub+after
        #print 'Expanded to %s' % s