from geometry import SE2
from itertools import tee, izip
from procgraph import Block


class se2_from_SE2_seq(Block):
    ''' Block used by :ref:`block:pose2commands`. '''
    Block.alias('se2_from_SE2_seq')

    Block.input('pose', 'Pose as an element of SE2')
    Block.output('velocity', 'Velocity as an element of se(2).')

    def init(self):
        self.state.prev = None
    
    def update(self):
        q2 = self.get_input(0)
        t2 = self.get_input_timestamp(0)
        
        if self.state.prev is not None:
            t1, q1 = self.state.prev
            vel = velocity_from_poses(t1, q1, t2, q2)
            self.set_output(0, vel, timestamp=t2)
            
        self.state.prev = t2, q2
        


def pose_difference(poses, S=SE2):
    """ poses: sequence of (timestamp, pose) """ 
    
    for p1, p2 in pairwise(poses):
        t1, q1 = p1
        t2, q2 = p2
        v = velocity_from_poses(t1, q1, t2, q2, S=S)
        yield v

def velocity_from_poses(t1, q1, t2, q2, S=SE2):
    delta = t2 - t1
    if not delta > 0:
        raise ValueError('invalid sequence')

    x = S.multiply(S.inverse(q1), q2)
    xt = S.algebra_from_group(x)
    v = xt / delta
    return v

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

# 
# class MyInput(object):
#     def __init__(self, block):
#         self.block = block
#         
#         
# class SimpleSequenceBlock(IteratorGenerator):
# 
#     def init_iterator(self):
#         my_input = MyInput(self)
#         myit = self.get_iterator(my_input)
#         
#         def add_signal_name(it):
#             for timestamp, value in it:
#                 yield timestamp, 0, value
#         
#         return add_signal_name(myit)
# 
#     @abstractmethod
#     @contract(returns=GeneratorType)
#     def get_iterator(self, input_sequence):
#         pass
# 
#     def init(self):
#         self.iterator = self.init_iterator()
#         if self.iterator is None:
#             msg = 'must return an iterator, got %s' % describe_value(self.iterator)
#             raise ValueError(msg)
#         self._load_next()
# 
#     def _load_next(self):
#         try:
#             signal, timestamp, value = self.iterator.next()
#             if not isinstance(signal, (str, int)):
#                 msg = ('Expected a string or number for the signal, got %s' % 
#                        describe_value(signal))
#                 raise ValueError(msg)
#             if not isinstance(timestamp, float):
#                 msg = ('Expected a number for the timestamp, got %s' % 
#                        describe_value(timestamp))
#                 raise ValueError(msg)
#             
#             self.next_signal = signal
#             self.next_timestamp = timestamp
#             self.next_value = value
#             self.has_next = True
#         except StopIteration:
#             self.has_next = False
# 
#     def next_data_status(self):
#         if self.has_next:
#             return (True, self.next_timestamp)
#         else:
#             return (False, None)
# 
#     def update(self):
#         if not self.has_next:
#             return  # XXX: error here?
# 
#         self.set_output(self.next_signal,
#                         value=self.next_value, timestamp=self.next_timestamp)
# 
#         self._load_next() 
#         
#         
# class VelocityFromPoses(SimpleSequenceBlock):
#     
#     Block.input('pose', 'Pose as an element of SE2')
#     
#     def get_iterator(self, input_sequence):
#         for t, x in pose_difference(input_sequence):
#             yield t, x
#     
#          
