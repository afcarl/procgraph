import subprocess
import yaml
import rosbag
   

def rosbag_info(bag):
    stdout = subprocess.Popen(['rosbag', 'info', '--yaml', bag],
                              stdout=subprocess.PIPE).communicate()[0]
    info_dict = yaml.load(stdout)
    return info_dict
# Example output:
# path: /home/andrea/01-youbot-ros-logs-good/unicornA_base1_2013-04-02-20-37-43.bag
# version: 2.0
# duration: 3499.176103
# start: 1364960263.862855
# end: 1364963763.038959
# size: 997946578
# messages: 2656954
# indexed: True
# compression: bz2
# uncompressed: 1840288997
# compressed: 962203048
# types:
#     - type: array_msgs/FloatArray
#       md5: 788898178a3da2c3718461eecda8f714 
# topics:
#     - topic: /arm_1/arm_controller/position_command
#       type: brics_actuator/JointPositions

from procgraph import logger as pg_logger
from rospy import rostime


def read_bag_stats(bagfile, topics, logger=None):
    """ 
        This yields a dict with: 
        
            topic
            msg
            t
            
            info:
                counter
                messages

                start
                end
                t_percentage
                t_from_start
            
            
    
    """
    if logger is None:
        logger = pg_logger
        
    logger.debug('Reading info for bagfile...')
    bag_info = rosbag_info(bagfile)
    logger.debug('Opening bagfile...')
    bag = rosbag.Bag(bagfile)

    extra = bag_info
    extra['messages'] = bag_info['messages']
    extra['start'] = bag_info['start']
    extra['end'] = bag_info['end']
    extra['duration'] = bag_info['duration']
    t0 = rostime.Time.from_sec(bag_info['start'])
    i = 0
    for topic, msg, t in bag.read_messages(topics=topics):
        if i == 0:
            logger.debug('first message arrived.')
        extra['counter'] = i
        extra['t_from_start'] = (t - t0).to_sec()
        extra['t_percentage'] = 100.0 * (extra['t_from_start'] / extra['duration'])  
        i += 1
        yield topic, msg, t, extra
       
       
