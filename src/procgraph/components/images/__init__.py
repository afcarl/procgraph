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

.. _`block:rgb2gray`: myblock

Block ``-->|rgb2gray|-->``
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. container:: configuration

  None

.. container:: input

  A grayscale image.

.. container:: output

  An RGB image.

.. container:: implementation

  Thin wrapper for :function:gray2rgb.

.. _`block:gray2rgb`:

Block ``-->|gray2rgb|-->``
^^^^^^^^^^^^^^^^^^^^^^^^^^
 
.. container:: configuration

  None

.. container:: input

  A RGB image.

.. container:: output

  A grayscale image.

.. container:: implementation

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

