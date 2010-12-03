try:

    from PIL import Image, ImageDraw, ImageFont #@UnusedImport

except ImportError as e:
    # We believe only nose will import this
    import sys
    sys.stderr.write('procgraph_pil: Could not find the PIL module: %s \n'
                     '  I will let you continue, but probably you will have '
                        'other errors later on.\n' % e)
    def warn():
        raise Exception('The PIL module was not found.')
    
    class warn_and_throw:
        def __getattr__(self, method_name): #@UnusedVariable
            warn()            

    Image = warn_and_throw() 
    ImageDraw = warn_and_throw()
    ImageFont = warn_and_throw()
