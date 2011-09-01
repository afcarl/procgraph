from procgraph import Block, Generator

class BagRead(Generator):
    ''' 
        This block reads a bag file (ROS logging format).
    '''
    Block.alias('bagread')
    Block.output_is_defined_at_runtime('The signals read from the log.')
    Block.config('file', 'Bag file to read')
    Block.config('topics', 'Which signals to output (and in what order). '
                 'Should be a comma-separated list. If you do not specify it '
                 '(or if empty) it will be all signals.',
                 default=None)

# TODO: allow setting signals names ('/rousout:debug')
#   TODO: add advancement display
#    Block.config('quiet', 'If true, disables advancements status messages.',
#                 default=False)
#                 
    def get_output_signals(self):
        from ros import rosbag #@UnresolvedImport
        self.bag = rosbag.Bag(self.config.file)
        
        if self.config.topics is not None:
            given_topics = self.config.topics.strip()
        else:
            given_topics = None
        
        #self.info('Given: %s' % given_topics)    
        if given_topics:
            topics = given_topics.split(',')
        else:
            topics = sorted(set([c.topic for c in self.bag._get_connections()]))
        
        # self.info('Tppics: %s' % topics)    
            
        self.topic2signal = {}
        for t in topics:
            # TODO: what if two topics with same name
            signal = t.split('/')[-1]
            self.topic2signal[t] = signal

        topics = self.topic2signal.keys()
        signals = self.topic2signal.values()
        
        self.info(self.topic2signal)
        
        self.iterator = self.bag.read_messages(topics=topics)

        return signals
        
    def init(self):
        self._load_next()
        
    def _load_next(self):
        try:
            topic, msg, timestamp = self.iterator.next()
            self.next_timestamp = timestamp.to_sec()
            self.next_value = msg
            self.next_topic = topic
            self.next_signal = self.topic2signal[topic]
            self.has_next = True
        except StopIteration:
            self.has_next = False
        
    def next_data_status(self): 
        if self.has_next:
            return (self.next_signal, self.next_timestamp)
        else:
            return (False, None)

    def update(self):
        if not self.has_next:
            return # XXX: error here?
            
        self.set_output(self.next_signal,
                        value=self.next_value,
                        timestamp=self.next_timestamp)
    
        self._load_next()
        

#        # write status message if not quiet
#        if next_signal == self.signals[0] and not self.config.quiet:
#            self.write_update_message(index, len(table), next_signal)
        
#    def write_update_message(self, index, T, signal, nintervals=10):
#        interval = int(numpy.floor(T * 1.0 / nintervals))
#        if (index > 0 and 
#            index != interval * (nintervals) and 
#            index % interval == 0): 
#            percentage = index * 100.0 / T
#            T = str(T)
#            index = str(index).rjust(len(T))
#            self.debug('%s read %.0f%% (%s/%s) (tracking signal %r).' % 
#                        (self.config.file, percentage, index, T, signal))
#         
    def finish(self):
        self.bag.close()
         
        
