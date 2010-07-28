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

Block ``-->|gradient|-->``
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Configuration**

``aperture``
  Aperture parameter (1,**3**,5,7,...).

**Input**

* A 2D numpy array.

**Output (2)**

``gx`` 
  Gradient along x. A 2D numpy float32 array.
  
``gy``
  Gradient along y. A 2D numpy float32 array.  

.. _`block:smooth`:

Block ``-->|smooth|-->``
^^^^^^^^^^^^^^^^^^^^^^^^

**Configuration**

``gaussian_std``
  Standard deviation of gaussian kernel, in pixel.

**Input (1)**

* a 2D numpy array

**Output (1)**

* a 2D numpy float32 array  


Module documentation
--------------------

.. autofunction:: gradient

.. autofunction:: smooth



'''

from opencv_utils import *