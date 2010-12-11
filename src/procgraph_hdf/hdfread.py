import operator

from procgraph  import Block, Generator, BadConfig

from .tables_cache import tc_open_for_reading, tc_close
from .hdfwrite import PROCGRAPH_LOG_GROUP


# TODO: respect original order

class HDFread(Generator):
    ''' This block reads a log written with HDFwrite.
    
    '''
    
    Block.alias('hdfread')
    Block.output_is_defined_at_runtime('The signals read from the log.')
    Block.config('file', 'HDF file to read')
    Block.config('signals', 'Which signals to output (and in what order). '
                 'Should be a comma-separated list. If you do not specify it '
                 ' will be all signal in the original order',
                 default=None)
    
    def get_output_signals(self):
        self.hf = tc_open_for_reading(self.config.file)
        
        group_name = PROCGRAPH_LOG_GROUP
        if not group_name in self.hf.root:
            raise Exception('File %r does not appear to be a pg log: %r' % 
                            (self.config.file, self.hf))
        
        self.log_group = self.hf.root._f_getChild(group_name)
        # todo: make sure we get the order
        all_signals = list(self.log_group._v_children) 
        
        if self.config.signals is None:
            self.signals = all_signals
        else:
            self.signals = []
            signal_list = filter(lambda x:x, self.config.signals.split(','))
            if not signal_list:
                raise BadConfig('Bad format: %r.' % self.config.signals,
                                self, 'signals')
            for s in signal_list:
                if not s in all_signals:
                    msg = ('Signal %r not present in log (available: %r)' % 
                            (s, all_signals))
                    raise BadConfig(msg, self, 'signals')
                self.signals.append(s)
                
        return self.signals
        
    def init(self):
        # let's do the rest of the initialization
        
        # signal -> table
        self.signal2table = {}
        # signal -> index in the table (or None)
        self.signal2index = {}
        
        for signal in self.signals:
            self.signal2table[signal] = self.log_group._f_getChild(signal) 
            if len(self.signal2table[signal]) > 0:
                self.signal2index[signal] = 0
            else:
                self.signal2index[signal] = None
        
    def _choose_next_signal(self):
        ''' Returns a tuple (name,timestamp) of the signal that produces 
            the next event, or (None,None) if we finished the log. '''
        
        # enumerate timestamps
        status = [] # array of tuples (signal, timestamp)
        for signal in self.signals:
            index = self.signal2index[signal] 
            if index is not None:
                table = self.signal2table[signal]
                timestamp = table[index]['time']
                status.append((signal, timestamp))
        
        if not status:
            return (None, None)
        else:   
            sorted_status = sorted(status, key=operator.itemgetter(1)) 
            return sorted_status[0] 
        
        
    def next_data_status(self):
        ''' 
        This is complicated but necessary. Do you have another value?
        - Yes, and it will be of this timestamp. (I can see it from the log)
        - No, this generator has finished.
        - Yes, but this is realtime and it does not depend on me.
          For example, I'm waiting for the next sensor data. 
          Ask me later. 
          
        In those cases, we return 
        
            (True, timestamp)
            (False, None)
            (True, None)
          
        '''
        
        next_signal, next_timestamp = self._choose_next_signal()
        if next_signal is None:
            return (False, None)
        else:
            return (True, next_timestamp)
        

    def update(self):
        next_signal, next_timestamp = self._choose_next_signal()
        
        # get value
        table = self.signal2table[next_signal]
        index = self.signal2index[next_signal]
        assert next_timestamp == table[index]['time']
        value = table[index]['value']
        
        self.set_output(next_signal, value=value, timestamp=next_timestamp)
        
        # update index
        if index + 1 == len(table):
            # finished
            self.signal2index[next_signal] = None
        else:
            self.signal2index[next_signal] = index + 1
         
        
    def finish(self):
        tc_close(self.hf)
        
         
        
