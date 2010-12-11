import numpy
 
from procgraph import simple_block
from procgraph.block_utils import assert_rgb_image, assert_gray_image

@simple_block
def rgb2gray(rgb):  
    ''' Converts a HxWx3 RGB image into a HxW grayscale image 
        by computing the luminance. 
        
        :param rgb: RGB image
        :type rgb: HxWx3 uint8
        
        :return: A RGB image in shades of gray.
        :rtype: HxW uint8
    '''  
    assert_rgb_image(rgb, 'input to rgb2grayscale')  
    r = rgb[:, :, 0].squeeze()
    g = rgb[:, :, 1].squeeze()
    b = rgb[:, :, 2].squeeze()
    # note we keep a uint8
    gray = r * 299.0 / 1000 + g * 587.0 / 1000 + b * 114.0 / 1000
    gray = gray.astype('uint8')
    
    return gray

@simple_block
def gray2rgb(gray):
    ''' Converts a H x W grayscale into a H x W x 3 RGB image 
        by replicating the gray channel over R,G,B. 
        
        :param gray: grayscale
        :type  gray: HxW uint8
        
        :return: A RGB image in shades of gray.
        :rtype: HxWx3 uint8
    '''  
    assert_gray_image(gray, 'input to rgb2grayscale')
      
    rgb = numpy.zeros((gray.shape[0], gray.shape[1], 3), dtype='uint8')
    for i in range(3):
        rgb[:, :, i] = gray
    return rgb
 
