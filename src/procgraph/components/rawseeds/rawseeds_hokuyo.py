import numpy

from procgraph.core.registrar import default_library
from procgraph.components.rawseeds.textlog import TextLog


class RawseedsHokuyo(TextLog):
    ''' This block reads a Hokuyo log in Rawseeds format. 
    
    HOKUYO:
Timestamp [seconds.microseconds]
R1..R681* Ranges [m]
    
    '''
    
    def parse_format(self, line):
        """ returns a tuple (timestamp, array of (name, value) )"""
        elements = map(str.strip, line.split(','))
        timestamp = float(elements.pop(0))
        readings = numpy.array(map(float, elements))
        
        # XXX should be 682 ???
        # if len(elements) != 681:
        #    print elements
        #    raise Exception('Expected 681 readings instead of %s' % len(elements))
            
        return timestamp, [('readings', readings)]


default_library.register('RawseedsHokuyo', RawseedsHokuyo)


