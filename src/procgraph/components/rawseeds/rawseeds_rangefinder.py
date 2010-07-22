import numpy
from procgraph.core.registrar import default_library
from procgraph.components.rawseeds.textlog import TextLog


class RawseedsRangeFinder(TextLog):
    ''' This block reads a range-finder log in Rawseeds format. '''
    
    def parse_format(self, line):
        """ returns a tuple (timestamp, array of (name, value) )"""
        elements = line.split(',')
        timestamp = float(elements[0])
        num_readings = int(elements[1]) #@UnusedVariable
        readings = numpy.array(map(float, elements[2:]))
        return timestamp, [('readings', readings)]


default_library.register('RawseedsRF', RawseedsRangeFinder)


