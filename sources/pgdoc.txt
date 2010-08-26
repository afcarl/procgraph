.. |towrite| replace:: **to write** 

.. _`pgdoc:procgraph.components`:

Summary 
============================================================


:ref:`module:procgraph.components`

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`Info <block:Info>`                                                                                                                                                                                 Prints more compact information about the inputs than :ref:`block:print`.                                                                                                                               
:ref:`clock <block:clock>`                                                                                                                                                                               None                                                                                                                                                                                                    
:ref:`constant <block:constant>`                                                                                                                                                                         Output a numerical constant that never changes.                                                                                                                                                         
:ref:`gain <block:gain>`                                                                                                                                                                                 FIXME: to be replaced by simpler function.                                                                                                                                                              
:ref:`identity <block:identity>`                                                                                                                                                                         This block outputs the inputs, unchanged.                                                                                                                                                               
:ref:`print <block:print>`                                                                                                                                                                               Print a representation of the input values along with their timestamp.                                                                                                                                  
:ref:`rand <block:rand>`                                                                                                                                                                                 None                                                                                                                                                                                                    
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.dynamic`

Blocks performing operations with a dynamic nature. 

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`derivative <block:derivative>`                                                                                                                                                                     None                                                                                                                                                                                                    
:ref:`derivative2 <block:derivative2>`                                                                                                                                                                   None                                                                                                                                                                                                    
:ref:`forward_difference <block:forward_difference>`                                                                                                                                                     Computes ``x[t+1] - x[t-1]`` normalized with timestamp.                                                                                                                                                 
:ref:`fps_data_limit <block:fps_data_limit>`                                                                                                                                                             This block limits the output update to a certain framerate.                                                                                                                                             
:ref:`fps_print <block:fps_print>`                                                                                                                                                                       Prints the fps count for the input.                                                                                                                                                                     
:ref:`history <block:history>`                                                                                                                                                                           This block collects the history of a quantity, and outputs (x, t).                                                                                                                                      
:ref:`historyt <block:historyt>`                                                                                                                                                                         This block collects the history of a quantity, and outputs (x, t).                                                                                                                                      
:ref:`last_n_samples <block:last_n_samples>`                                                                                                                                                             This block collects the last n samples of a quantity, and outputs (x, timestamp).                                                                                                                       
:ref:`sieve <block:sieve>`                                                                                                                                                                               This block only transmits every n steps.                                                                                                                                                                
:ref:`sync <block:sync>`                                                                                                                                                                                 This block synchronizes a set of streams to the first stream (the master).                                                                                                                              
:ref:`sync2 <block:sync2>`                                                                                                                                                                               This block synchronizes a set of N sensor streams.                                                                                                                                                      
:ref:`two_step_difference <block:two_step_difference>`                                                                                                                                                   Computes ``x[t+1] - x[t]`` normalized with timestamp.                                                                                                                                                   
:ref:`wait <block:wait>`                                                                                                                                                                                 This block waits a given number of updates before transmitting the output.                                                                                                                              
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.gui`

Blocks using Matplotlib to display data.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`fps_limit <block:fps_limit>`                                                                                                                                                                       This block limits the output update to a certain framerate.                                                                                                                                             
:ref:`plot <block:plot>`                                                                                                                                                                                 Just plots the vector instantaneously                                                                                                                                                                   
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.images`

Blocks for basic operations on images. 

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`compose <block:compose>`                                                                                                                                                                           Configuration:                                                                                                                                                                                          
:ref:`gray2rgb <block:gray2rgb>`                                                                                                                                                                         Converts a H x W grayscale into a H x W x 3 RGB by replicating channel.                                                                                                                                 
:ref:`grayscale <block:grayscale>`                                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`grid <block:grid>`                                                                                                                                                                                 A block that creates a larger image by arranging them in a grid.                                                                                                                                        
:ref:`posneg <block:posneg>`                                                                                                                                                                             Converts a 2D value to normalized uint8 RGB red=positive, blue=negative 0-255.                                                                                                                          
:ref:`rgb2gray <block:rgb2gray>`                                                                                                                                                                         None                                                                                                                                                                                                    
:ref:`scale <block:scale>`                                                                                                                                                                               Provides a RGB representation of the values by interpolating the range [min(value),max(value)] into the colorspace [min_color, max_color].                                                              
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.misc`

Miscellaneous functions to be better organized.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`as_json <block:as_json>`                                                                                                                                                                           Converts the input into a JSON string.                                                                                                                                                                  
:ref:`pickle <block:pickle>`                                                                                                                                                                             Dumps the input as a pickle file.                                                                                                                                                                       
:ref:`to_file <block:to_file>`                                                                                                                                                                           Prints the input line by line to a given file.                                                                                                                                                          
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.numpy_ops`

Various operations wrapping numpy functions.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`* <block:*>`                                                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`+ <block:+>`                                                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`- <block:->`                                                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`/ <block:/>`                                                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`abs <block:abs>`                                                                                                                                                                                   Wrapper around :py:func:`numpy.core.umath.absolute`.                                                                                                                                                    
:ref:`astype <block:astype>`                                                                                                                                                                             None                                                                                                                                                                                                    
:ref:`dstack <block:dstack>`                                                                                                                                                                             Wrapper around :py:func:`numpy.dstack`.                                                                                                                                                                 
:ref:`gradient1d <block:gradient1d>`                                                                                                                                                                     None                                                                                                                                                                                                    
:ref:`hstack <block:hstack>`                                                                                                                                                                             Wrapper around :py:func:`numpy.hstack`.                                                                                                                                                                 
:ref:`log <block:log>`                                                                                                                                                                                   Wrapper around :py:func:`numpy.core.umath.log`.                                                                                                                                                         
:ref:`outer <block:outer>`                                                                                                                                                                               Wrapper around :py:func:`numpy.multiply.outer`.                                                                                                                                                         
:ref:`select <block:select>`                                                                                                                                                                             None                                                                                                                                                                                                    
:ref:`sign <block:sign>`                                                                                                                                                                                 Wrapper around :py:func:`numpy.core.umath.sign`.                                                                                                                                                        
:ref:`square <block:square>`                                                                                                                                                                             Wrapper around :py:func:`numpy.core.umath.square`.                                                                                                                                                      
:ref:`take <block:take>`                                                                                                                                                                                 None                                                                                                                                                                                                    
:ref:`vstack <block:vstack>`                                                                                                                                                                             Wrapper around :py:func:`numpy.vstack`.                                                                                                                                                                 
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.robotics`

Routines specific to robotics.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`pose2commands <block:pose2commands>`                                                                                                                                                               None                                                                                                                                                                                                    
:ref:`pose2vel_ <block:pose2vel_>`                                                                                                                                                                       None                                                                                                                                                                                                    
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.signals`

Simple routins for signals extraction, combination.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`extract <block:extract>`                                                                                                                                                                           This block extracts some of the components                                                                                                                                                              
:ref:`join <block:join>`                                                                                                                                                                                 This block joins multiple signals into one.                                                                                                                                                             
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.statistics`

Blocks for common statistical operations.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`cov2corr <block:cov2corr>`                                                                                                                                                                         Compute the correlation matrix from the covariance matrix. If zero_diagonal = True, the diagonal is set to 0 instead of 1.                                                                              
:ref:`covariance <block:covariance>`                                                                                                                                                                     None                                                                                                                                                                                                    
:ref:`expectation <block:expectation>`                                                                                                                                                                   None                                                                                                                                                                                                    
:ref:`normalize <block:normalize>`                                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`soft_variance <block:soft_variance>`                                                                                                                                                               Computes the element-wise "soft" variance (expectation of error absolute value)                                                                                                                         
:ref:`variance <block:variance>`                                                                                                                                                                         Computes the element-wise variance.                                                                                                                                                                     
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.video`

Blocks for encoding/decoding video based on MPlayer.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`SimpleCompression <block:SimpleCompression>`                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`mencoder <block:mencoder>`                                                                                                                                                                         Encodes a video stream using ``mencoder``.                                                                                                                                                              
:ref:`mplayer <block:mplayer>`                                                                                                                                                                           Plays a video stream.                                                                                                                                                                                   
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


.. _`module:procgraph.components`:

Module ``procgraph.components``
============================================================


.. _`block:Info`:

Block ``Info``
------------------------------------------------------------
Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 

Prints more compact information about the inputs than :ref:`block:print`. 

For numpy arrays it prints their shape and dtype instead of their values.

.. _`block:clock`:

Block ``clock``
------------------------------------------------------------
Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 

.. _`block:constant`:

Block ``constant``
------------------------------------------------------------
Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 

Output a numerical constant that never changes. 

Example: ::

    |constant value=42 name=meaning| -> ...

Two parameters:

* ``value``, necessary
* ``name``, optional signal name (default: const)

.. _`block:gain`:

Block ``gain``
------------------------------------------------------------
Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 

FIXME: to be replaced by simpler function.

.. _`block:identity`:

Block ``identity``
------------------------------------------------------------
Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 

This block outputs the inputs, unchanged. 

This is an example of a block whose signal configuration is dynamics:
init() gets called twice.

.. _`block:print`:

Block ``print``
------------------------------------------------------------
Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 

Print a representation of the input values along with their timestamp.

.. _`block:rand`:

Block ``rand``
------------------------------------------------------------
Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 

.. _`module:procgraph.components.dynamic`:

Module ``procgraph.components.dynamic``
============================================================


Blocks performing operations with a dynamic nature. 


This library contains blocks that perform operations with time.
This library is autoloaded.

.. _`block:derivative`:

Block ``derivative``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/derivative.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/derivative.py>`_. 

.. _`block:derivative2`:

Block ``derivative2``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/derivative2.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/derivative2.py>`_. 

.. _`block:forward_difference`:

Block ``forward_difference``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/derivative.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/derivative.py>`_. 

Computes ``x[t+1] - x[t-1]`` normalized with timestamp.

.. _`block:fps_data_limit`:

Block ``fps_data_limit``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/fps_data_limit.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/fps_data_limit.py>`_. 

This block limits the output update to a certain framerate.

.. _`block:fps_print`:

Block ``fps_print``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/fps_print.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/fps_print.py>`_. 

Prints the fps count for the input.

.. _`block:history`:

Block ``history``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/history.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/history.py>`_. 

This block collects the history of a quantity, and outputs (x, t). 

Arguments:
- interval (seconds)  interval to record

Output:
- x
- t

.. _`block:historyt`:

Block ``historyt``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/historyt.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/historyt.py>`_. 

This block collects the history of a quantity, and outputs (x, t). 

Arguments:
- interval (seconds)  interval to record

Output:
- a tuple (x,y)

.. _`block:last_n_samples`:

Block ``last_n_samples``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/history.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/history.py>`_. 

This block collects the last n samples of a quantity, and outputs (x, timestamp). 

Arguments:
- n, number of samples

Output:
- x
- t

.. _`block:sieve`:

Block ``sieve``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/sieve.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/sieve.py>`_. 

This block only transmits every n steps. 

Config:
- n

Input: variable
Output: variable (same as input)

.. _`block:sync`:

Block ``sync``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/sync.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/sync.py>`_. 

This block synchronizes a set of streams to the first stream (the master). 

The first signal is called the "master" signal.
The other (N-1) are slaves.

We guarantee that:

- if the slaves are faster than the master,
  then we output exactly the same.

Example diagrams: ::

    Master  *  *  *   *   *
    Slave   ++++++++++++++++

    Master  *  *  *   *   *
    output? v  v  x   v
    Slave   +    +      +
    output? v    v      v

.. _`block:sync2`:

Block ``sync2``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/sync2.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/sync2.py>`_. 

This block synchronizes a set of N sensor streams. 

The first signal is called the "master" signal.
The other (N-1) are slaves.

.. _`block:two_step_difference`:

Block ``two_step_difference``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/derivative2.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/derivative2.py>`_. 

Computes ``x[t+1] - x[t]`` normalized with timestamp.

.. _`block:wait`:

Block ``wait``
------------------------------------------------------------
Implemented in `/src/procgraph/components/dynamic/wait.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/wait.py>`_. 

This block waits a given number of updates before transmitting the output. 

Config:
- n (number of updates)

Input: variable
Output: variable (same as input)

.. _`module:procgraph.components.gui`:

Module ``procgraph.components.gui``
============================================================


Blocks using Matplotlib to display data.

.. _`block:fps_limit`:

Block ``fps_limit``
------------------------------------------------------------
Implemented in `/src/procgraph/components/gui/fps_limit.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/gui/fps_limit.py>`_. 

This block limits the output update to a certain framerate. 

Note that this uses realtime wall clock time -- not the data time!
This is mean for real-time applications, such as visualization.

.. _`block:plot`:

Block ``plot``
------------------------------------------------------------
Implemented in `/src/procgraph/components/gui/plot.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/gui/plot.py>`_. 

Just plots the vector instantaneously

.. _`module:procgraph.components.images`:

Module ``procgraph.components.images``
============================================================


Blocks for basic operations on images. 

The  module contains blocks that perform basic operations
on images. The library is autoloaded and has no software dependency.

For more complex operations see also:

* :ref:`module:procgraph.components.cv`
* :ref:`module:procgraph.components.pil`


**Example**

Convert a RGB image to grayscale, and back to a RGB image:::


    |input| -> |rgb2gray| -> |gray2rgb| -> |output|

.. _`block:compose`:

Block ``compose``
------------------------------------------------------------
Implemented in `/src/procgraph/components/images/compose.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/compose.py>`_. 

Configuration: 

- ``width``, ``height``: dimension in  pixels
- ``positions``: a structure giving the position of each signal in the canvas. Example: ::

      compose.positions = {y: [0,0], ys: [320,20]}

.. _`block:gray2rgb`:

Block ``gray2rgb``
------------------------------------------------------------
Implemented in `/src/procgraph/components/images/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/filters.py>`_. 

Converts a H x W grayscale into a H x W x 3 RGB by replicating channel.

.. _`block:grayscale`:

Block ``grayscale``
------------------------------------------------------------
Implemented in `/src/procgraph/components/images/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/filters.py>`_. 

.. _`block:grid`:

Block ``grid``
------------------------------------------------------------
Implemented in `/src/procgraph/components/images/imggrid.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/imggrid.py>`_. 

A block that creates a larger image by arranging them in a grid.

.. _`block:posneg`:

Block ``posneg``
------------------------------------------------------------
Implemented in `/src/procgraph/components/images/copied_from_reprep.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/copied_from_reprep.py>`_. 

Converts a 2D value to normalized uint8 RGB red=positive, blue=negative 0-255.

.. _`block:rgb2gray`:

Block ``rgb2gray``
------------------------------------------------------------
Implemented in `/src/procgraph/components/images/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/filters.py>`_. 

.. _`block:scale`:

Block ``scale``
------------------------------------------------------------
Implemented in `/src/procgraph/components/images/copied_from_reprep.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/copied_from_reprep.py>`_. 

Provides a RGB representation of the values by interpolating the range [min(value),max(value)] into the colorspace [min_color, max_color]. 

Input: a numpy array with finite values squeeze()able to (W,H).

Configuration:

-  ``min_value``:  If specified, this is taken to be the threshold. Everything
                     below min_value is considered to be equal to min_value.
-  ``max_value``:  Optional upper threshold.
-  ``min_color``:  color associated to minimum value. Default: [1,1,1] = white.
-  ``max_color``:  color associated to maximum value. Default: [0,0,0] = black.

Raises :py:class:`.ValueError` if min_value == max_value

Returns:  a (W,H,3) numpy array with dtype uint8 representing a RGB image.

.. _`module:procgraph.components.misc`:

Module ``procgraph.components.misc``
============================================================


Miscellaneous functions to be better organized.

.. _`block:as_json`:

Block ``as_json``
------------------------------------------------------------
Implemented in `/src/procgraph/components/misc/json_misc.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/misc/json_misc.py>`_. 

Converts the input into a JSON string.

.. _`block:pickle`:

Block ``pickle``
------------------------------------------------------------
Implemented in `/src/procgraph/components/misc/pickling.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/misc/pickling.py>`_. 

Dumps the input as a pickle file.

.. _`block:to_file`:

Block ``to_file``
------------------------------------------------------------
Implemented in `/src/procgraph/components/misc/to_file.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/misc/to_file.py>`_. 

Prints the input line by line to a given file.

.. _`module:procgraph.components.numpy_ops`:

Module ``procgraph.components.numpy_ops``
============================================================


Various operations wrapping numpy functions.

.. _`block:*`:

Block ``*``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

.. _`block:+`:

Block ``+``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

.. _`block:-`:

Block ``-``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

.. _`block:/`:

Block ``/``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

.. _`block:abs`:

Block ``abs``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

Wrapper around :py:func:`numpy.core.umath.absolute`.

.. _`block:astype`:

Block ``astype``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

.. _`block:dstack`:

Block ``dstack``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

Wrapper around :py:func:`numpy.dstack`.

.. _`block:gradient1d`:

Block ``gradient1d``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/gradient1d.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/gradient1d.py>`_. 

.. _`block:hstack`:

Block ``hstack``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

Wrapper around :py:func:`numpy.hstack`.

.. _`block:log`:

Block ``log``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

Wrapper around :py:func:`numpy.core.umath.log`.

.. _`block:outer`:

Block ``outer``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

Wrapper around :py:func:`numpy.multiply.outer`.

.. _`block:select`:

Block ``select``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

.. _`block:sign`:

Block ``sign``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

Wrapper around :py:func:`numpy.core.umath.sign`.

.. _`block:square`:

Block ``square``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

Wrapper around :py:func:`numpy.core.umath.square`.

.. _`block:take`:

Block ``take``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

.. _`block:vstack`:

Block ``vstack``
------------------------------------------------------------
Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 

Wrapper around :py:func:`numpy.vstack`.

.. _`module:procgraph.components.robotics`:

Module ``procgraph.components.robotics``
============================================================


Routines specific to robotics.

.. _`block:pose2commands`:

Block ``pose2commands``
------------------------------------------------------------
Implemented in `/src/procgraph/components/robotics/pose2velocity.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/robotics/pose2velocity.py>`_. 

.. _`block:pose2vel_`:

Block ``pose2vel_``
------------------------------------------------------------
Implemented in `/src/procgraph/components/robotics/pose2velocity.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/robotics/pose2velocity.py>`_. 

.. _`module:procgraph.components.signals`:

Module ``procgraph.components.signals``
============================================================


Simple routins for signals extraction, combination.

.. _`block:extract`:

Block ``extract``
------------------------------------------------------------
Implemented in `/src/procgraph/components/signals/extract.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/signals/extract.py>`_. 

This block extracts some of the components 

Arguments:

- index

.. _`block:join`:

Block ``join``
------------------------------------------------------------
Implemented in `/src/procgraph/components/signals/join.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/signals/join.py>`_. 

This block joins multiple signals into one.

.. _`module:procgraph.components.statistics`:

Module ``procgraph.components.statistics``
============================================================


Blocks for common statistical operations.

.. _`block:cov2corr`:

Block ``cov2corr``
------------------------------------------------------------
Implemented in `/src/procgraph/components/statistics/cov2corr.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/cov2corr.py>`_. 

Compute the correlation matrix from the covariance matrix. If zero_diagonal = True, the diagonal is set to 0 instead of 1.

.. _`block:covariance`:

Block ``covariance``
------------------------------------------------------------
Implemented in `/src/procgraph/components/statistics/covariance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/covariance.py>`_. 

.. _`block:expectation`:

Block ``expectation``
------------------------------------------------------------
Implemented in `/src/procgraph/components/statistics/expectation.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/expectation.py>`_. 

.. _`block:normalize`:

Block ``normalize``
------------------------------------------------------------
Implemented in `/src/procgraph/components/statistics/covariance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/covariance.py>`_. 

.. _`block:soft_variance`:

Block ``soft_variance``
------------------------------------------------------------
Implemented in `/src/procgraph/components/statistics/variance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/variance.py>`_. 

Computes the element-wise "soft" variance (expectation of error absolute value)

.. _`block:variance`:

Block ``variance``
------------------------------------------------------------
Implemented in `/src/procgraph/components/statistics/variance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/variance.py>`_. 

Computes the element-wise variance.

.. _`module:procgraph.components.video`:

Module ``procgraph.components.video``
============================================================


Blocks for encoding/decoding video based on MPlayer.

.. _`block:SimpleCompression`:

Block ``SimpleCompression``
------------------------------------------------------------
Implemented in `/src/procgraph/components/video/simple_compression.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/video/simple_compression.py>`_. 

.. _`block:mencoder`:

Block ``mencoder``
------------------------------------------------------------
Implemented in `/src/procgraph/components/video/mencoder.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/video/mencoder.py>`_. 

Encodes a video stream using ``mencoder``. 

Input: H x W x 3  uint8  numpy array representing RGB image.

Configuration:

- file
- vcodec   mpeg4
- vbitrate 1000000
- quiet

Note that allowed codec and bitrate depend on your version of mencoder.

.. _`block:mplayer`:

Block ``mplayer``
------------------------------------------------------------
Implemented in `/src/procgraph/components/video/mplayer.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/video/mplayer.py>`_. 

Plays a video stream. 

Config:
    - file

