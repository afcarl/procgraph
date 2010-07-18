

class Value:
    def __init__(self, value=None, timestamp=None):
        self.value = value
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
        self.input_signal_name2id = {}
        # this is an array of Values
        self.input_signals = None
        
        # same as above
        self.output_signals_names = None
        self.output_signals_name2id = {}
        self.output_signals = None
    
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
            raise ValueError('Could not find config "%s" in %s.' % 
                             (conf, self.config))
        return self.config[conf]
        
    def set_state(self, num_or_id, value):
        ''' Can be called during init() and update() '''
        pass
    
    # Functions that can be called during runtime
    def set_output(self, num_or_id, value, timestamp=None):
        ''' Sets an output value. If timestamp is omitted, it
            will default to the inherited timestamp. '''
        pass
    
    def get_input(self, num_or_id):
        pass
    
    def valid_input(self, num_or_id):
        if isinstance(num_or_id, str):
            return num_or_id in self.input_signal_name2id
        if isinstance(num_or_id, type(0)):
            return num_or_id < len(self.input_signals)
        raise ValueError()
    
    def canonicalize_input(self, num_or_id):
        assert self.valid_input(num_or_id)
        if isinstance(num_or_id, str):
            return num_or_id 
        if isinstance(num_or_id, type(0)):
            return self.input_signal_names[num_or_id]
        raise ValueError()
        
    def valid_output(self, num_or_id):
        if isinstance(num_or_id, str):
            return num_or_id in self.output_signal_name2id
        if isinstance(num_or_id, type(0)):
            return num_or_id < len(self.output_signals)
        raise ValueError()
    
    def canonicalize_output(self, num_or_id):
        assert self.valid_output(num_or_id)
        if isinstance(num_or_id, str):
            return num_or_id 
        if isinstance(num_or_id, type(0)):
            return self.output_signal_names[num_or_id]
        raise ValueError()
    
    def get_input_timestamp(self, num_or_id):
        ''' Returns the timestamp (double) for the selected input. '''
        pass
    
    def __repr__(self):
        s = 'Block:%s(' % self.__class__.__name__
        if self.input_signals:
            s += "in:%s" % ",".join(self.input_signal_names)
        else:
            s += "in:?"
        
        s+=';'
        if self.output_signals:
            s += "out:%s" % ",".join(self.output_signal_names)
        else:
            s += "out:?"
        s+= ')'
        return s
    
    
class Generator(Block):
    
    def has_more(self):
        raise TypeError()
    
    
    