try:
    
    try:
        import cv #@UnresolvedImport @UnusedImport
    except:
        import opencv as cv #@UnresolvedImport @Reimport

except ImportError as e:
    # We believe only nose will import this
    import sys
    sys.stderr.write('procgraph_cv: Could not find the "cv" or "opencv" module: %s \n'
                     '  I will let you continue, but probably you will have '
                        'other errors later on.\n' % e)
    def warn():
        raise Exception('The OpenCV module was not found.')
    
    class warn_and_throw:
        def __getattr__(self, method_name): #@UnusedVariable
            warn()            

    cv = warn_and_throw() 
    
