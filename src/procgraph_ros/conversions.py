#try:
#    from ros import std_msgs
#    from std_msgs.msg import  String
#except ImportError:
#    pass
 

from procgraph import simple_block

@simple_block
def ros2python(msg):
    ''' Converts a ROS message to a Python object. '''
    # FIXME: this is a hack
#    print msg.__class__
#    if isinstance(msg, String):
#        return msg.data
#    else:
#        print('Unknown type: %s' % msg.__class__)
#        return msg
    
    return msg.data
