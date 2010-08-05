from procgraph.core.model_loader import add_models_to_library
from procgraph.core.registrar import default_library
from procgraph.core.block import Block
from procgraph.core.exceptions import BadInput

from snp_geometry.pose import Pose


class Pose2velocity(Block):
    def init(self):
        self.define_input_signals(['q12', 't12'])
        self.define_output_signals(['commands'])
        
    def update(self):
        q = self.get_input('q12')
        t = self.get_input('t12')
        if not (len(q) == 2 and len(t) == 2):
            raise BadInput('Bad input received.', self)
         
        pose1 = Pose.from_xytheta(q[0])
        pose2 = Pose.from_xytheta(q[1])
        delta = t[1] - t[0]
        
        if not delta > 0:
            raise BadInput('Bad timestamp sequence %s' % t, self, 't')

        diff = Pose.pose_diff(pose2, pose1)
        velocity = diff.logarithm()
        # scale velocity
        velocity.linear = velocity.linear / delta
        velocity.angular = velocity.angular / delta
        
        #print velocity.linear, velocity.angular
        
        # This is 2D motion (== is too strong)
        # assert velocity.linear[2] == 0
        # assert velocity.angular[0] == 0
        # assert velocity.angular[1] == 0
        
        commands = [float(velocity.linear[0]),
                    float(velocity.linear[1]),
                    float(velocity.angular[2])]
        
        self.set_output('commands', commands, timestamp=t[0])

default_library.register('pose2vel_', Pose2velocity)

# Computes the variance
model_spec = """
--- model pose2commands
 
|input name=pose| --> |last_n_samples n=2| --> |pose2vel_| --> commands 

    commands          -->          |output name=commands|
    commands --> |extract index=0| --> |output name=vx|
    commands --> |extract index=1| --> |output name=vy|
    commands --> |extract index=2| --> |output name=omega|
    
"""
add_models_to_library(default_library, model_spec)

    
