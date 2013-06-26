from procgraph import Generator
from abc import abstractmethod
from contracts import describe_value, contract
from types import GeneratorType

__all__ = ['IteratorGenerator']

class IteratorGenerator(Generator):
    ''' 

    '''
    
    @abstractmethod
    @contract(returns=GeneratorType)
    def init_iterator(self):
        """ Must return an iterator yielding signal, timestamp, value """
        raise NotImplemented
    
    def init(self):
        self.iterator = self.init_iterator()
        if self.iterator is None:
            msg = 'must return an iterator, got %s' % describe_value(self.iterator)
            raise ValueError(msg)
        self._load_next()

    def _load_next(self):
        try:
            signal, timestamp, value = self.iterator.next()
            if not isinstance(signal, (str, int)):
                msg = ('Expected a string or number for the signal, got %s' % 
                       describe_value(signal))
                raise ValueError(msg)
            if not isinstance(timestamp, float):
                msg = ('Expected a number for the timestamp, got %s' % 
                       describe_value(timestamp))
                raise ValueError(msg)
            
            self.next_signal = signal
            self.next_timestamp = timestamp
            self.next_value = value
            self.has_next = True
        except StopIteration:
            self.has_next = False

    def next_data_status(self):
        if self.has_next:
            return (True, self.next_timestamp)
        else:
            return (False, None)

    def update(self):
        if not self.has_next:
            return  # XXX: error here?

        self.set_output(self.next_signal,
                        value=self.next_value, timestamp=self.next_timestamp)

        self._load_next() 
