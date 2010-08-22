.. _`creating_new_blocks`:

Creating new blocks
===================

Turning simple instantaneous functions into blocks 
--------------------------------------------------

**To write.***

More complicated blocks
------------------------


The init() method
^^^^^^^^^^^^^^^^^

Do not use your class's constructor to initialize the block. There are
all sorts of issues with custom constructors that make writing things
such as module serialization hard.

Instead, |procgraph| provides the facilities you need for configuration,
initialization, etc.

The init() method is supposed to set up 
 method: basic usage.


The return value of init() is ignored, except in one special case described in the 
next section.

Advanced init() usage -- partial initialization

Note that there some special cases for which initialization cannot be
completed before until the block is in the model and sigals are connected.
One typical example is when we want to write a block that can operate
on multiple signal, of which we do not know the number. Consider as an example
the case in which we want to write a block performing a "min" operation.::

	# three values
	|constant value=1| -> x 
	|constant value=2| -> y
	|constant value=3| -> z
	
	# take the min
	x,y,z -> |min| -> minimum

When the block min is initialized, it is outside the block


The update() method
^^^^^^^^^^^^^^^^^^^

* If the computation is not finished, return Block.UPDATE_NOT_FINISHED.
  This will tell procgraph to consider the computation still pending,
  and update() will be called again in the future with the same input signals.
  
  All other return values are just ignored by procgraph.
  

Writing generators
------------------

**To write.***
