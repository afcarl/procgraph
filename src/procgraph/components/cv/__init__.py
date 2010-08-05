''' 
.. _`library:cv`:

``cv`` block library
====================

The ``cv`` library contains blocks that use OpenCV. 

**Packages dependencies**

* ``opencv`` (or ``cv``)

Block list
---------- 


.. _`block:gradient`:

gradient
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: configuration

  ``aperture``
    Aperture parameter (1,**3**,5,7,...).

.. container:: input

  A 2D numpy array.

.. container:: output

  ``gx`` 
    Gradient along x. A 2D numpy float32 array.
  
  ``gy``
    Gradient along y. A 2D numpy float32 array.  

.. _`block:smooth`:

smooth
^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: configuration

  ``gaussian_std``
    Standard deviation of gaussian kernel, in pixel.

.. container:: input

  A 2D numpy array.

.. container:: output

  A 2D numpy float32 array.  


Module documentation
--------------------

.. autofunction:: gradient

.. autofunction:: smooth



'''

from opencv_utils import *
