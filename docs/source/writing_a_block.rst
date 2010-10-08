.. _`creating_new_blocks`:

Blocks
============




Creating blocks
=================

There are three ways to create new Procgraph blocks:

1. For using simple Python functions as stateless blocks,
   just register them 
   using the function :py:func:`register_simple_block`.

   This is explained in :ref:`simple_blocks`.

2. To create a stateful block in Python, subclass the class ``Block``.

   This is explained in :ref:`normal_blocks`.

   A normal block updates its output only when it has new input.
   A block that produces output even without a new input is called a "Generator"
   and it is treated differently by Procgraph.

   This is explained in :ref:`creating_generators`.


3. Every model created using Procgraph's language can be used as a block.

   The syntax is explained in :ref:`creating_models`
 


.. _simple_blocks:

Turning simple instantaneous functions into blocks 
--------------------------------------------------

**To write.***


.. _normal_blocks:


More complicated blocks
------------------------

To create a stateful block, subclass the class ``Block`` and use the class methods
to define input, output and configuration.

The following is a minimal example of a block. It has one input and one output. 
The output is the 

    class Expectation(Block):
        ''' Computes the sample expectation of a signal. '''
        Block.alias('expectation')
        
        Block.input('x', 'Any numpy array.')
        Block.output('Ex', 'Expectation of input.')
        
        def init(self): 
            self.state.num_samples = 0
        
        def update(self):
            N = self.state.num_samples
            
            if N == 0:
                self.state.Ex = self.input.x.copy()
            else:
                self.state.Ex = (self.state.Ex * N + self.input.x) / float(N + 1);
        
            self.state.num_samples += 1
            self.output.Ex = self.state.Ex 






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
