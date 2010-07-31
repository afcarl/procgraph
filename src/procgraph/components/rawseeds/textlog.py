from procgraph.components.rawseeds.file_utils import expand_environment
from procgraph.core.block import Generator
from procgraph.core.exceptions import ModelExecutionError


class TextLog(Generator):
    ''' This represents a generic log reader that reads
        from a file line-by-line. 
        
        Subclasses should overload the parse_format() static method.
    '''
    
    def init(self):
        filename = self.get_config('file')
        filename = expand_environment(filename)
        
        if filename.endswith('bz2'):
            import bz2
            self.stream = bz2.BZ2File(filename)
        else:
            self.stream = open(filename,'r')
            
        self.set_state('line', 0) # line counter
        self.read_next_line()
        
        if self.timestamp is None:
            raise Exception('Empty file %s' % filename)
        
        names = map( lambda x:x[0], self.values )
        self.define_output_signals(names)
        self.define_input_signals([])

    def read_next_line(self):
        line = self.get_state('line')
        next_line = self.stream.readline()
        # check end of file
        if not next_line:
            self.timestamp = None
            self.values = None
            return
        try:
            self.timestamp, self.values = self.parse_format(next_line)
        except Exception as e:
            msg = "While reading line %s of file %s (='%s'): %s" % \
                (line, self.get_config('file'), next_line, e)
            raise ModelExecutionError(msg, self)
        self.set_state('line',line+1)

    def next_data_status(self):
        if self.timestamp is None: # EOF
            return (False, None)
        else:
            return (True, self.timestamp)
                 
    def update(self):
        for signal, value in self.values:
            self.set_output(signal, value, timestamp=self.timestamp)
      
        self.read_next_line()
    
    def parse_format(self, line):
        """ returns a tuple (timestamp, array of (name, value) )"""
        raise ValueError("Implement this.")
