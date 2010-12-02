from procgraph import Block, BadInput, register_model_spec


from snp_geometry.pose import Pose #@UnresolvedImport

class Pose2velocity(Block):
    ''' Block used by :ref:`block:pose2commands`. '''
    Block.alias('pose2vel_')
    
    Block.input('q12', 'Last two poses.')
    Block.input('t12', 'Last two timestamps.')
    
    Block.output('commands', 'Estimated commands ``[vx,vy,omega]``.')
        
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
        
        commands = [float(velocity.linear[0]),
                    float(velocity.linear[1]),
                    float(velocity.angular[2])]
        
        self.set_output('commands', commands, timestamp=t[0])
 

register_model_spec("""
--- model pose2commands
''' Computes the velocity commands from the odometry data. '''
input pose "Odometry ``[x,y,theta]``."
output commands "Estimated commands ``[vx,vy,omega]``."
output vx
output vy
output omega 
 
|input name=pose| --> |last_n_samples n=2| --> |pose2vel_| --> commands 

    commands          -->          |output name=commands|
    commands --> |extract index=0| --> |output name=vx|
    commands --> |extract index=1| --> |output name=vy|
    commands --> |extract index=2| --> |output name=omega|
    
""")
    
