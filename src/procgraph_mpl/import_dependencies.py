try:
    # This is the only place in procgraph where we import pylab.
    # This centralized place allows us to decide the backend.
    # In other packages, use:
    #    from procgraph_mpl import pylab
    import matplotlib
    # TODO: warn if we cannot select what we want
    matplotlib.use('Agg')
    from matplotlib import pylab #@UnusedImport

except ImportError as e:
    # We believe only nose will import this
    import sys
    sys.stderr.write('procgraph_mpl: Could not find the "matplotlib" module: %s \n' 
                     '  I will let you continue, but probably you will have '
                       'other errors later on. \n' % e)
    def warn():
        raise Exception('The "matplotlib" module was not found.')
    
    class warn_and_throw:
        def __getattr__(self, method_name):
            warn()            

    pylab = warn_and_throw()
    