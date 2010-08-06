from math import ceil, sqrt

class Statistics:
    def __init__(self, block):
        self.block = block
        self.num = 0
        self.mean = 0
        self.var = 0
        self.perc_cpu = None
        self.perc_times = None

class ExecutionStats:
    
    def __init__(self):
        self.samples = {}
        
    def add(self, block, duration):
        assert duration >= 0
         
        if duration == 0:
            duration = 0.0001
        
        if not block in self.samples:
            self.samples[block] = Statistics(block)
            
        s = self.samples[block]
        
        s.mean = (s.mean * s.num + duration) / (s.num + 1)
        s.var = (s.var * s.num + (duration - s.mean) ** 2) / (s.num + 1)
        s.num = s.num + 1
        
        assert s.var >= 0
        assert s.mean > 0
        
    def print_info(self):
        # update percentage
        total = sum(map(lambda s: s.mean * s.num, self.samples.values()))
        total_times = sum(map(lambda s:  s.num, self.samples.values()))
        for s in self.samples.values():
            s.perc_cpu = s.mean * s.num / total
            s.perc_times = s.num * 1.0 / total_times
            
            
        # sort by percentage
        all = sorted(self.samples.values(), key=lambda x:-x.perc_cpu)
        min_perc = 3
        print 'Statistics (ignoring < %d):' % min_perc + " " * 30
        for s in all:
            perc = ceil(s.perc_cpu * 100)
            if perc < min_perc:
                continue
            perc_times = ceil(s.perc_times * 100)
            
            jitter = ceil(100 * (sqrt(s.var) * 2 / s.mean))
            print '  - %d%%  t=%dms avg.ex: %d%% (jit=%d%%) %s ' % (
                perc, 1000 * s.mean, perc_times, jitter, s.block) 
            
             
