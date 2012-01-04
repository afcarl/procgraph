import numpy

from procgraph import simple_block

from . import Image


@simple_block
def imread(filename):
    ''' 
        Reads an image from a file.
        
        :param filename: Image filename.
        :type filename: string
        
        :return: image: The image as a numpy array.
        :rtype: image
    '''
    try:
        im = Image.open(filename)
    except Exception as e:
        raise Exception('Could not open filename "%s": %s' % \
                        (filename, e))

    data = numpy.array(im)

    return data
