from math import ceil, sqrt

class Statistics:
    def __init__(self, block):
        self.block = block
        self.num = 0
        self.mean_cpu = 0
        self.var_cpu = 0
        self.mean_wall = 0
        self.var_wall = 0
        self.perc_cpu = None
        self.perc_wall = None
        self.perc_times = None

class ExecutionStats:
    
    
    def __init__(self):
        self.samples = {}
        
    def add(self, block, cpu, wall):
        assert cpu >= 0
        assert wall >= 0
         
        if cpu == 0:
            cpu = 0.0001
        if wall == 0:
            wall = 0.0001
            
        
        if not block in self.samples:
            self.samples[block] = Statistics(block)
            
        s = self.samples[block]
        
        s.mean_cpu = (s.mean_cpu * s.num + cpu) / (s.num + 1)
        s.var_cpu = (s.var_cpu * s.num + (cpu - s.mean_cpu) ** 2) / (s.num + 1)
        s.mean_wall = (s.mean_wall * s.num + wall) / (s.num + 1)
        s.var_wall = (s.var_wall * s.num + (wall - s.mean_wall) ** 2) / (s.num + 1)
        s.num = s.num + 1
        
        WINDOW = 100
        
        if s.num > WINDOW:
            s.num == WINDOW
        
        
    def print_info(self):
        # update percentage
        samples = self.samples.values()
        total_cpu = sum(map(lambda s: s.mean_cpu * s.num, samples))
        total_wall = sum(map(lambda s: s.mean_wall * s.num, samples))
        total_times = sum(map(lambda s:  s.num, samples))
        for s in samples:
            s.perc_cpu = s.mean_cpu * s.num / total_cpu
            s.perc_wall = s.mean_wall * s.num / total_wall
            s.perc_times = s.num * 1.0 / total_times
            
            
        # sort by percentage
        all = sorted(self.samples.values(), key=lambda x:-x.perc_wall)
        min_perc = 3
        print 'Statistics (ignoring < %d):' % min_perc + " " * 30
        for s in all:
            perc_cpu = ceil(s.perc_cpu * 100)
            perc_wall = ceil(s.perc_wall * 100)
            if (perc_cpu < min_perc) and (perc_wall < min_perc):
                continue
            perc_times = ceil(s.perc_times * 100)
            
            jitter_cpu = ceil(100 * (sqrt(s.var_cpu) * 2 / s.mean_cpu))
            jitter_wall = ceil(100 * (sqrt(s.var_wall) * 2 / s.mean_wall))
            
            if s.mean_cpu < 0.7 * s.mean_wall:
                comment = ' IO '
            else:
                comment = '    '
#            print ''.join([
#'- cpu: %dms (+-%d%%) %02d%% of total; ' % (1000 * s.mean_cpu, jitter_cpu, perc_cpu),
#'wall: %dms (+-%d%%) %02d%% of total; ' % (1000 * s.mean_wall, jitter_wall, perc_wall),
#'exec: %02d%% of total' % perc_times])
            print ''.join([
'- cpu: %4dms %2d%%; ' % (1000 * s.mean_cpu, perc_cpu),
'wall: %4dms %2d%%; ' % (1000 * s.mean_wall, perc_wall),
'exec: %2d%%; %s  ' % (perc_times, comment),
str(s.block)])
     
        
