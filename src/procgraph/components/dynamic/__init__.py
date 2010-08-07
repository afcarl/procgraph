'''
.. _`library:dynamic`:

``dynamic`` block library
==========================

This library contains blocks that perform operations with time.


This library is autoloaded. 


**Software dependencies**

None

**Examples** 


Block list
---------- 

.. _`block:wait`:

wait
^^^^

This block ignores the first ``n`` samples from the input, and then acts
as the identity. This is useful if the preceding block has unreliable
input at the beginning.

.. container:: configuration

  ``n`` 
    Number of initial samples to ignore.



.. _`block:sieve`:

sieve
^^^^^

This block only allows 1 / ``n`` th of samples to pass through. Useful to decimate
data.
 
.. container:: configuration

  ``n``
    Fraction of samples to pass through.




.. _`block:sync`:

sync
^^^^

This block synchronizes a group of signals.

**To write long description**

.. container:: input

  Variable number of input.

.. container:: output

  As many as the input.



.. _`block:derivative`:


derivative
^^^^^^^^^^

This block computes the derivative of the input value.
The derivative is computed by convolving the input with the (non causal) filter
``[-1 0 1] / (2*dt)``.

.. container:: input

  A numpy array.

.. container:: output

  The derivative of the array.
   



.. _`block:history`:


history
^^^^^^^^^^

** to write **


.. _`block:historyn`:


historyn
^^^^^^^^^^

** to write **

'''


import derivative
import history
import sync
import sieve
import wait

import historyt
import fps_data_limit

