''' Blocks for basic operations on images.

The  module contains blocks that perform basic operations
on images. The library is autoloaded and has no software dependency. 

For more complex operations see also:

* :ref:`module:procgraph.components.cv`
* :ref:`module:procgraph.components.pil`


**Example**

Convert a RGB image to grayscale, and back to a RGB image:::


    |input| -> |rgb2gray| -> |gray2rgb| -> |output| 

'''
 

#'''
#
#Block list
#---------- 
#
#.. _`block:rgb2gray`:
#
#rgb2gray
#^^^^^^^^^
#
#
#.. container:: configuration
#
#  None
#
#.. container:: input
#
#  A grayscale image.
#
#.. container:: output
#
#  An RGB image.
#
#.. container:: implementation
#
#  Thin wrapper for :function:gray2rgb.
#
#.. _`block:gray2rgb`:
#
#gray2rgb
#^^^^^^^^^^^^^^^^^^^^^^^^^^
# 
#.. container:: configuration
#
#  None
#
#.. container:: input
#
#  A RGB image.
#
#.. container:: output
#
#  A grayscale image.
#
#.. container:: implementation
#
#  Thin wrapper for :function:rgb2grayscale.
#
#
#.. _`block:compose`:
#
#compose
#^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#|towrite|
#
#
#.. _`block:grid`:
#
#grid
#^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#.. _`block:posneg`:
#
#|towrite|
#
#posneg
#^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#|towrite|
#
#
#.. _`block:scale`:
#
#scale
#^^^^^^^^^^^^^^^^^^^^^^^^^^
#
#
#|towrite|
#
#
#Module documentation
#--------------------
#
#.. autofunction:: procgraph.components.images.filters.rgb2grayscale
#
#.. autofunction:: procgraph.components.images.filters.gray2rgb
#'''


import filters 
import copied_from_reprep
import compose 
import imggrid

