from procgraph.core.block import Block, Generator
import glob
import os
from procgraph.core.registrar import register_block_class
import numpy
from procgraph.components.rawseeds.file_utils import expand_environment


class RawseedsLogReader(Block):
    
    def init(self, directory, format='png'):
        all_files = glob.glob(os.path.join(directory, '*_*.*.%s' % format))
                              
    def has_more(self):
        pass
             
    def update(self):
        pass


class RawseedsRangeFinder(Generator):
    ''' This block reads a range-finder log in Rawseeds format. '''
    
    def init(self):
        filename = self.get_config('file')
        filename = expand_environment(filename)
        self.stream = open(filename,'r')
        self.next_line = self.stream.readline()
        self.define_output_signals(['readings'])
        self.define_input_signals([])
        # self.define_output_signals(['theta'])

    def next_data_status(self):
        if self.next_line == '':
            return (False, None)
        else:
            timestamp, data = RawseedsRangeFinder.parse_format(self.next_line)
            return (True, timestamp)
                 
    def update(self):
        timestamp, readings = RawseedsRangeFinder.parse_format(self.next_line)
        self.set_output('readings', value=readings, timestamp=timestamp)
        self.next_line = self.stream.readline()

    @staticmethod
    def parse_format(line):
        """ returns timestamp, readings """
        elements = line.split(',')
        timestamp = float(elements[0])
        num_readings = int(elements[1])
        readings = numpy.array(map(float, elements[2:]))
        return timestamp, readings


register_block_class('RawseedsRF', RawseedsRangeFinder)

