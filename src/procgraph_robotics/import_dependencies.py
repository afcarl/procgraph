try:

    from snp_geometry.pose import Pose #@UnresolvedImport

except ImportError as e:
    # We believe only nose will import this
    import sys
    sys.stderr.write('procgraph_robotics: Could not find the "snp_geometry" module: %s \n'
                     '  I will let you continue, but probably you will have \n'
                     '  other errors later on.\n' % e)
    sys.stderr.write('  You need to install snp_geometry from '
                       'http://github.com/AndreaCensi/snp_geometry \n')
    def warn():
        raise Exception('The  "snp_geometry" module was not found.')
    
    class warn_and_throw:
        def __getattr__(self, method_name): #@UnusedVariable
            warn()            

    Pose = warn_and_throw() 
    
