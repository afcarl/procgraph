from procgraph.core.exceptions import BlockWriterError, ModelWriterError, \
    ModelExecutionError
from procgraph.core.block_sugar import InputProxy, OutputProxy, StateProxy, \
    ConfigProxy

# Timestamp to use for constant times
ETERNITY = 'constant-time'

class Value:
    def __init__(self, value=None, timestamp=None):
        self.value = value
        if timestamp is None:
            timestamp = 0
        self.timestamp = timestamp

class Block(object):

    # Housekeeping
    def __init__(self, name, config, library):
        self.name = name
        self.__config = config
        # this is an array containing the names/ids
        # example: ["y", 1, 2]
        self.__input_signal_names = None
        # example: {"y":0, "1":1, "2":2}
        self.__input_signal_name2id = None
        # this is an array of Values
        self.__input_signals = None
        
        # same as above
        self.__output_signal_names = None
        self.__output_signal_name2id = None
        self.__output_signals = None
        
        # state variables
        self.__states = {}
        
        # instantiation point
        self.where = None
        
        # proxies for accessing input, output, and state
        self.input = InputProxy(self)
        self.output = OutputProxy(self)
        self.state = StateProxy(self)
        self.config = ConfigProxy(self)

    
    INIT_NOT_FINISHED = 'init-not-finished'
    def init(self):
        ''' Initializes the block. Return  '''
        pass
     
    UPDATE_NOT_FINISHED = 'update-not-finished'
    def update(self):
        ''' Performs the block function.
        Use set_state() for temporary storage. '''
        pass
    
    # Used during initialization
    
    def num_input_signals(self):
        assert self.are_input_signals_defined()
        return len(self.__input_signals)
    
    def num_output_signals(self):
        assert self.are_output_signals_defined()
        return len(self.__output_signals)
    
    def get_input_signals_names(self):
        ''' Returns the list of names of currently defined input signals. '''
        assert self.are_input_signals_defined()
        return list(self.__input_signal_names)

    def get_output_signals_names(self):
        ''' Returns the list of names of currently defined output signals. '''
        assert self.are_output_signals_defined()
        return list(self.__output_signal_names)
    
    def are_input_signals_defined(self):
        return self.__input_signals is not None
    
    def are_output_signals_defined(self):
        return self.__output_signals is not None
    
    def define_input_signals(self, signals):
        if not isinstance(signals, list):
            raise BlockWriterError('I expect the parameter to define_input_signals()' + 
                                   ' to be a list, got a %s: %s' % \
                                   (signals.__class__.__name__, signals))

        # reset structures
        self.__input_signal_names = []
        self.__input_signals = []
        self.__input_signal_name2id = {}
        for i, s in enumerate(signals):
            if not isinstance(s, str):
                raise BlockWriterError(('Invalid list of names for input: %s ' + 
                                        'they should be strings') % signals)

            self.__input_signal_names.append(str(s))
            self.__input_signal_name2id[str(s)] = i
            self.__input_signals.append(Value()) 
             
          
    def define_output_signals(self, signals):
        if not isinstance(signals, list):
            raise BlockWriterError('I expect the parameter to define_output_signals()' + 
                                   ' to be a list, got a %s: %s' % \
                                   (signals.__class__.__name__, signals))
        # reset structures
        self.__output_signal_names = []
        self.__output_signals = []
        self.__output_signal_name2id = {}
        for i, s in enumerate(signals):
            if not isinstance(s, str):
                raise BlockWriterError(('Invalid list of names for output: %s ' + 
                                        'they should be strings') % signals)
            
            self.__output_signal_names.append(str(s))
            self.__output_signal_name2id[str(s)] = i
            self.__output_signals.append(Value())
        
    def set_config_default(self, key, value):
        if not key in self.__config:
            self.__config[key] = value
            
    def get_config(self, conf):
        if not conf in self.__config:
            raise ModelExecutionError('For block %s: could not find parameter "%s" in config %s.' % 
                             (self, conf, self.__config), self)
        return self.__config[conf]
        
    def set_state(self, num_or_id, value):
        ''' Can be called during init() and update() '''
        self.__states[num_or_id] = value
        
    def get_state(self, num_or_id):
        ''' Can be called during init() and update() '''
        return self.__states[num_or_id]
    
    # Functions that can be called during runtime
    def set_output(self, num_or_id, value, timestamp=None):
        ''' Sets an output value. If timestamp is omitted, it
            will default to the maximum of the input signals timestamp. '''
        if timestamp is None:
            if len(self.__input_signals) == 0:
                raise Exception('Timestamp not specified and no inputs')
            
            timestamp = max(self.get_input_signals_timestamps())
        
        output_struct = self.__get_output_struct(num_or_id)
        output_struct.value = value
        output_struct.timestamp = timestamp

    def from_outside_set_input(self, num_or_id, value, timestamp):
        ''' Sets an input value. This is used from outside, not 
        from the block. (This is overloaded by Model) '''
        input_struct = self.__get_input_struct(num_or_id)
        input_struct.value = value
        input_struct.timestamp = timestamp

    def get_input(self, num_or_id):
        ''' Gets the value of an input signal. '''
        input_struct = self.__get_input_struct(num_or_id)
        return input_struct.value

    def get_input_timestamp(self, num_or_id):
        ''' Gets the timestamp of an input signal. '''
        input_struct = self.__get_input_struct(num_or_id)
        return input_struct.timestamp

    def get_output_timestamp(self, num_or_id):
        ''' Gets the timestamp of an output signal. '''
        output_struct = self.__get_output_struct(num_or_id)
        return output_struct.timestamp

    def get_output(self, num_or_id):
        ''' Gets the value of an output signal. '''
        output_struct = self.__get_output_struct(num_or_id)
        return output_struct.value
    
    def __get_input_struct(self, num_or_id):
        ''' Returns a reference to the Value structure of the given input signal. '''
        if not self.is_valid_input_name(num_or_id):
            raise ModelWriterError('Unknown output name "%s".' % str(num_or_id), self)
        if isinstance(num_or_id, str):
            # convert from name to number 
            num_or_id = self.__input_signal_name2id[num_or_id]
        return self.__input_signals[num_or_id]
        
    def __get_output_struct(self, num_or_id):
        ''' Returns a reference to the Value structure of the given out signal. '''
        if not self.is_valid_output_name(num_or_id):
            raise ModelWriterError('Unknown input name "%s".' % str(num_or_id), self)
        
        if isinstance(num_or_id, str):
            # convert from name to number
            num_or_id = self.__output_signal_name2id[num_or_id]
        return self.__output_signals[num_or_id]
        
    def is_valid_input_name(self, num_or_id):
        ''' Checks that num_or_id (string or int) is a valid handle
            for one of the signals. ''' 
        if isinstance(num_or_id, str):
            return num_or_id in self.__input_signal_name2id
        if isinstance(num_or_id, type(0)):
            return num_or_id < len(self.__input_signals)
        raise ValueError()
    
    def canonicalize_input(self, num_or_id):
        ''' Converts the signal spec (either string or id) to string
            (useful because more user-friendly). ''' 
        assert self.is_valid_input_name(num_or_id)
        if isinstance(num_or_id, str):
            return num_or_id 
        if isinstance(num_or_id, type(0)):
            return self.__input_signal_names[num_or_id]
        raise ValueError()
        
    def is_valid_output_name(self, num_or_id):
        ''' Checks that num_or_id (string or int) is a valid handle
            for one of the signals. ''' 
        if isinstance(num_or_id, str):
            return num_or_id in self.__output_signal_name2id
        if isinstance(num_or_id, type(0)):
            return num_or_id < len(self.__output_signals)
        raise ValueError()
    
    def canonicalize_output(self, num_or_id):
        ''' Converts the signal spec (either string or id) to string
            (useful because more user-friendly). ''' 
        assert self.is_valid_output_name(num_or_id)
        if isinstance(num_or_id, str):
            return num_or_id 
        if isinstance(num_or_id, type(0)):
            return self.__output_signal_names[num_or_id]
        raise ValueError()
     
    def get_output_signals_timestamps(self):
        ''' Returns a list of the output values timestamps. '''
        return map(lambda x: x.timestamp, self.__output_signals)
    
    def get_input_signals_timestamps(self):
        ''' Returns a list of the input signals timestamps. '''
        return map(lambda x: x.timestamp, self.__input_signals)
    
    def __repr__(self):
        s = 'B:%s:%s(' % (self.__class__.__name__, self.name)
        s += self.get_io_repr()
        s += ')'
        return s
    
        
    def get_io_repr(self):
        ''' Returns a representation of io ports for this block. '''
        s = ""
        if self.are_input_signals_defined():
            if self.__input_signals:
                s += "in:%s" % ",".join(self.__input_signal_names)
            else:
                s += 'in:/'
        else:
            s += "in:?"
        
        s += ';'
        if self.are_output_signals_defined():
            if self.__output_signals:
                s += "out:%s" % ",".join(self.__output_signal_names)
            else:
                s += 'out:/'
        else:
            s += "out:?"
        return s
    
    
class Generator(Block):
    
    def next_data_status(self):
        ''' 
        This is complicated but necessary. Do you have another value?
        - Yes, and it will be of this timestamp. (I can see it from the log)
        - No, this generator has finished.
        - Yes, but this is realtime and it does not depend on me.
          For example, I'm waiting for the next sensor data. 
          Ask me later. 
          
        In those cases, we return 
        
            (yes, timestamp)
            (no, None)
            (yes, None)
          
        '''
        raise ValueError('Did not implement this')
    
    

