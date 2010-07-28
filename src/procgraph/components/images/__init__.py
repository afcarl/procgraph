'''
.. _`library:images`:

``images`` block library
==========================

The ``images`` library contains blocks that perform basic operations
on images.

This library is autoloaded. 

See also:

* :ref:`library:cv`
* :ref:`library:pil`

**Software dependencies**

None

**Example**

Convert a RGB image to grayscale, and back to a RGB image::


    |input| -> |rgb2gray| -> |gray2rgb| -> |output| 

Block list
----------

.. _`block:rgb2gray`:

Block ``-->|rgb2gray|-->``
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Configuration**

None

**Input**

* A grayscale image.

**Output (2)**

* An RGB image.

**Implementation**

Thin wrapper for :function:gray2rgb.

.. _`block:gray2rgb`:

Block ``-->|gray2rgb|-->``
^^^^^^^^^^^^^^^^^^^^^^^^^^
 
**Configuration**

None

**Input**

* A RGB image.

**Output (2)**

* A grayscale image.

**Implementation**

Thin wrapper for :function:rgb2grayscale.


.. _`block:compose`:

Block ``-->|compose|-->``
^^^^^^^^^^^^^^^^^^^^^^^^^^


.. _`block:grid`:

Block ``-->|grid|-->``
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _`block:posneg`:

Block ``-->|posneg|-->``
^^^^^^^^^^^^^^^^^^^^^^^^^^


.. _`block:scale`:

Block ``-->|scale|-->``
^^^^^^^^^^^^^^^^^^^^^^^^^^


Module documentation
--------------------

.. autofunction:: procgraph.components.images.filters.rgb2grayscale

.. autofunction:: procgraph.components.images.filters.gray2rgb
'''


import filters 
import copied_from_reprep
import compose 
import imggrid

