from procgraph.core.block import Block, Generator
from collections import namedtuple
from procgraph.core.registrar import default_library

Sample = namedtuple('Sample', 'timestamp value')


class Sync(Generator):
    ''' 
    This block synchronizes a set of N sensor streams.
    
    The first signal is called the "master" signal.
    The other (N-1) are slaves.
    
    We guarantee that:
    - if the slaves are faster than the master,
      then we output exactly the same
      
      
      
    Master  *  *  *   *   *
    Slave   ++++++++++++++++
    
    Master  *  *  *   *   *
    output? v  v  x   v  
    Slave   +    +      +   
    output? v    v      v
    '''
    def init(self):
        # say we are not ready if the inputs were not defined.
        if not self.are_input_signals_defined():
            return Block.INIT_NOT_FINISHED
        
        
        # output signals get the same name as the inputs
        names = self.get_input_signals_names()
        if len(names) == 1:
            raise Exception('I need at least two ')
        
        self.define_output_signals(names)
        
        # create a state for each signal: it is an array
        # of tuples (timestamp, tuple)
        queues = {}
        for signal in names:
            queues[signal] = []
            
        # note in all queues, 
        # [(t0,...), (t1,...), ... , (tn,...) ]
        # and we have t0 > tn
        # The chronologically first (oldest) is queue[-1]
        # You get one out using queue.pop()
        # You insert one with queue.insert(0,...)
            
        
        self.set_state('queues', queues)
        
        self.set_state('master', names[0])
        self.set_state('slaves', names[1:])
        
        # The output is an array of tuple (timestamp, values)
        # [
        #    (timestamp1, [value1,value2,value3,...]),
        #    (timestamp1, [value1,value2,value3,...])
        # ]#
        self.set_state('output', [])
        
    def update(self):
        def debug(s):
            if False:
                print 'sync %s %s' % (self.name, s)
            
        output = self.get_state('output')
        queues = self.get_state('queues')
        names = self.get_input_signals_names()
        # for each input signal, put its value in the queues
        # if it is not already present
        for i, name in enumerate(names):
            current_timestamp = self.get_input_timestamp(i)
            current_value = self.get_input (i)
            if current_timestamp == 0:
                debug('Ignoring %s because timestamp still 0' % name)
                continue
            queue = queues[name]
            # if there is nothing in the queue
            # or this is a new sample
            if not queue or queue[0].timestamp != current_timestamp: # new sample
                queue.insert(0, Sample(timestamp=current_timestamp, value=current_value))
                debug("Inserting %s ts %s (queue %d)" % (name, current_timestamp,
                                                         len(queue)))
                
        master = self.get_state('master')
        master_queue = queues[master]
        slaves = self.get_state('slaves')
        
            
        # if there is more than one value in each slave
        
        # Now check whether all slaves signals are >= the master
        # If so, output a synchronized sample.
        if master_queue:
            all_ready = True
            master_timestamp = master_queue[-1].timestamp
            #print "Master timestamp: %s" % (master_timestamp)
            for slave in slaves:
                slave_queue = queues[slave]
                # remove oldest
                while slave_queue and slave_queue[-1].timestamp < master_timestamp:
                    debug("DROP one from %s" % slave)
                    slave_queue.pop()
                
                if not slave_queue or (master_timestamp > slave_queue[-1].timestamp): 
                    all_ready = False
                    its_ts = map(lambda x:x.timestamp, slave_queue)
                    #print "Slave %s not ready: %s" %(slave, its_ts)
                    break 
            
            if all_ready:
                debug("**** Ready: master timestamp %s " % (master_timestamp))
                master_value = master_queue.pop().value
                output_values = [master_value]
                for slave in slaves:
                    # get the freshest still after the master
                    slave_queue = queues[slave]
                    slave_timestamp, slave_value = slave_queue.pop()
                    assert slave_timestamp >= master_timestamp
                    difference = slave_timestamp - master_timestamp
                    debug(" - %s timestamp %s diff %s" % (slave, slave_timestamp, difference))
                    output_values.append(slave_value)
                output.insert(0, (master_timestamp, output_values))

    # XXX XXX not really sure here
        # if master has more than one sample, then drop the first one
#        if len(master_queue)>1:
 #           val = master_queue.pop()
  #          debug('DROPPING master (%s) ts =%s' % (master, val.timestamp))

        # if we have something to output, do it 
        if output:
            timestamp, values = output.pop()
            assert timestamp > 0
            debug("---------------- @ %s" % timestamp)
            for i in range(self.num_output_signals()):
                self.set_output(i, values[i], timestamp) 
            
        
        
    def next_data_status(self):
        output = self.get_state('output')
        if not output: # no output ready
            return (False, None)
        else:
            timestamp = self.output[-1][0]
            return (True, timestamp)
        
        
    
default_library.register('sync', Sync)


