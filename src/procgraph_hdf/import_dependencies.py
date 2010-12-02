try:

    import tables #@UnusedImport
    
except ImportError as e:
    # We believe only nose will import this
    import sys
    sys.stderr.write('procgraph_hdf: Could not find the "tables" module: %s \n'
                     '  I will let you continue, but probably you will have '
                        'other errors later on.\n' % e)
    def warn():
        raise Exception('The "tables" module was not found.')
    
    class warn_and_throw:
        def __getattr__(self, method_name):
            warn()            

    tables = warn_and_throw() 