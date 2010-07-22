from procgraph.core.registrar import default_library
from procgraph.core.block import Block

    
class History(Block):
    ''' 
    This block collects the history of a quantity,
    and outputs (x, t).
    
    Arguments:
    - interval (seconds)  interval to record
    
    Output:
    - x
    - t
    ''' 
        
    def init(self):
        self.set_config_default('interval', 10)
        
        self.define_output_signals(['x','t'])
        self.define_input_signals(['input'])
        
        self.set_state('x', [])
        self.set_state('t', [])
    
    def update(self):
        
        sample = self.get_input(0)
        timestamp = self.get_input_timestamp(0)
         
        x = self.get_state('x')
        t = self.get_state('t')
        
        x.append(sample)
        t.append(timestamp)
        
        interval = self.get_config('interval')
        while abs(t[0] - t[-1]) > interval:
            t.pop(0)
            x.pop(0)
            
        self.set_output('x', x) 
        self.set_output('t', t)
        
        
   # def __repr__(self):
   #     return 'History(interval=%s)' % self.get_config('interval')

default_library.register('history', History)


class Wait(Block):
    ''' 
    This block waits a given number of updates before transmitting the 
    output.
    
    Config:
    - n (number of updates) 

    Input: variable 
    Output: variable (same as input)
    

    ''' 
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        # output signals get the same name as the inputs
        self.define_output_signals( self.get_input_signals_names() )
        
        self.set_state('count', 0)
        print 'Initializing'

    def update(self):
        count = self.get_state('count')
        count += 1
        self.set_state('count', count)
        #print 'Counting %s' %count
        # make something happen after we have waited enough
        if count >= self.get_config('n'): 
            # Just copy the input to the output
            for i in range(self.num_input_signals()):
                self.set_output(i, self.get_input(i), self.get_input_timestamp(i))

default_library.register('wait', Wait)



class Sieve(Block):
    ''' 
    This block only transmits every n steps. 
    
    Config:
    - n  

    Input: variable 
    Output: variable (same as input)

    ''' 
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        # output signals get the same name as the inputs
        self.define_output_signals( self.get_input_signals_names() )
        
        self.get_config('n')
        self.set_state('count', 0)
        print 'Initializing'

    def update(self):
        count = self.get_state('count')
        n = self.get_config('n')

        # make something happen after we have waited enough
        if 0 == count % n: 
            # Just copy the input to the output
            for i in range(self.num_input_signals()):
                self.set_output(i, self.get_input(i), self.get_input_timestamp(i))

        count += 1
        self.set_state('count', count)
        
default_library.register('sieve', Sieve)

  
  