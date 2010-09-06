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
 
import filters 
import copied_from_reprep
import compose 
import imggrid
import border
import blend

