

class Value:
    def __init__(self, value=None, timestamp=None):
        self.value = value
        if timestamp is None:
            timestamp = 0
        self.timestamp = timestamp

class Block(object):

    # Housekeeping
    def __init__(self, name, config):
        self.name = name
        self.config = config
        # this is an array containing the names/ids
        # example: ["y", 1, 2]
        self.input_signal_names = None
        # example: {"y":0, "1":1, "2":2}
        self.input_signal_name2id = None
        # this is an array of Values
        self.input_signals = None
        
        # same as above
        self.output_signal_names = None
        self.output_signal_name2id = None
        self.output_signals = None
        
        # state variables
        self.states = {}
    
    def init(self, *args, **kwargs):
        ''' Initializes the block '''
        pass
     
    def update(self):
        ''' Performs the block function.
        Use set_state() for temporary storage. '''
        pass
    
    # Used during initialization
    def input_signals_defined(self):
        return self.input_signals is not None
    
    def output_signals_defined(self):
        return self.output_signals is not None
    
    def define_input_signals(self, signals):
        assert isinstance(signals, list)
        # reset structures
        self.input_signal_names = []
        self.input_signals = []
        self.input_signal_name2id = {}
        for i, s in enumerate(signals):
            self.input_signal_names.append(str(s))
            self.input_signal_name2id[str(s)] = i
            self.input_signals.append( Value()) 
             
          
    def define_output_signals(self, signals):
        assert isinstance(signals, list)
        # reset structures
        self.output_signal_names = []
        self.output_signals = []
        self.output_signal_name2id = {}
        for i, s in enumerate(signals):
            self.output_signal_names.append(str(s))
            self.output_signal_name2id[str(s)] = i
            self.output_signals.append( Value())
        
    def set_config_default(self, key, value):
        if not key in self.config:
            self.config[key] = value
            
    def get_config(self, conf):
        if not conf in self.config:
            raise ValueError('Could not find parameter "%s" in config %s.' % 
                             (conf, self.config))
        return self.config[conf]
        
    def set_state(self, num_or_id, value):
        ''' Can be called during init() and update() '''
        self.states[num_or_id] = value
        
    def get_state(self, num_or_id):
        ''' Can be called during init() and update() '''
        return self.states[num_or_id]
    
    # Functions that can be called during runtime
    def set_output(self, num_or_id, value, timestamp=None):
        ''' Sets an output value. If timestamp is omitted, it
            will default to the maximum of the input signals timestamp. '''
        if timestamp is None:
            if len(self.input_signals) == 0:
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
        if isinstance(num_or_id, str):
            # convert from name to number 
            num_or_id = self.input_signal_name2id[num_or_id]
        return self.input_signals[num_or_id]
        
    def __get_output_struct(self, num_or_id):
        ''' Returns a reference to the Value structure of the given out signal. '''
        if isinstance(num_or_id, str):
            # convert from name to number
            num_or_id = self.output_signal_name2id[num_or_id]
        return self.output_signals[num_or_id]
        
    def valid_input(self, num_or_id):
        ''' Checks that num_or_id (string or int) is a valid handle
            for one of the signals. ''' 
        if isinstance(num_or_id, str):
            return num_or_id in self.input_signal_name2id
        if isinstance(num_or_id, type(0)):
            return num_or_id < len(self.input_signals)
        raise ValueError()
    
    def canonicalize_input(self, num_or_id):
        ''' Converts the signal spec (either string or id) to string
            (useful because more user-friendly). ''' 
        assert self.valid_input(num_or_id)
        if isinstance(num_or_id, str):
            return num_or_id 
        if isinstance(num_or_id, type(0)):
            return self.input_signal_names[num_or_id]
        raise ValueError()
        
    def valid_output(self, num_or_id):
        ''' Checks that num_or_id (string or int) is a valid handle
            for one of the signals. ''' 
        if isinstance(num_or_id, str):
            return num_or_id in self.output_signal_name2id
        if isinstance(num_or_id, type(0)):
            return num_or_id < len(self.output_signals)
        raise ValueError()
    
    def canonicalize_output(self, num_or_id):
        ''' Converts the signal spec (either string or id) to string
            (useful because more user-friendly). ''' 
        assert self.valid_output(num_or_id)
        if isinstance(num_or_id, str):
            return num_or_id 
        if isinstance(num_or_id, type(0)):
            return self.output_signal_names[num_or_id]
        raise ValueError()
    
     
    def get_output_signals_timestamps(self):
        ''' Returns a list of the output values timestamps. '''
        return map( lambda x: x.timestamp, self.output_signals)
    
    def get_input_signals_timestamps(self):
        ''' Returns a list of the input signals timestamps. '''
        return map( lambda x: x.timestamp, self.input_signals)
    
#    def were_output_signals_updated(self, previous_timestamps):
#        ''' Check if any timestamp changed. previous_timestamp
#            is the result of an earlier call to get_output_signals_timestamps() '''
#        for i, t in enumerate(previous_timestamps):
#            # check time does not flow backward
#            if not (t <= self.output_signals[i].timestamp):
#                raise Exception(('It seems we got back in time for signal %s in %s:'
#                                +' from %s to %s.') % \
#                                ( self.output_signal_names[i], self,
#                                  t, self.output_signals[i].timestamp))
#                
#            if t < self.output_signals[i].timestamp:
#                return True
#        return False

    
    def __repr__(self):
        s = 'Block:%s(' % self.__class__.__name__
        if self.input_signals is not None:
            if self.input_signals:
                s += "in:%s" % ",".join(self.input_signal_names)
        else:
            s += "in:?"
        
        s+=';'
        if self.output_signals is not None:
            if self.output_signals:
                s += "out:%s" % ",".join(self.output_signal_names)
        else:
            s += "out:?"
        s+= ')'
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
    
    

