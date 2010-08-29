.. |towrite| replace:: **to write** 

.. _`pgdoc:procgraph.components`:

Summary 
============================================================


:ref:`module:procgraph.components`

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`clock <block:clock>`                                                                                                                                                                               None                                                                                                                                                                                                    
:ref:`constant <block:constant>`                                                                                                                                                                         Output a numerical constant that never changes.                                                                                                                                                         
:ref:`gain <block:gain>`                                                                                                                                                                                 FIXME: to be replaced by simpler function.                                                                                                                                                              
:ref:`identity <block:identity>`                                                                                                                                                                         This block outputs the inputs, unchanged.                                                                                                                                                               
:ref:`info <block:info>`                                                                                                                                                                                 Prints more compact information about the inputs than :ref:`block:print`.                                                                                                                               
:ref:`print <block:print>`                                                                                                                                                                               Print a representation of the input values along with their timestamp.                                                                                                                                  
:ref:`rand <block:rand>`                                                                                                                                                                                 None                                                                                                                                                                                                    
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.dynamic`

Blocks performing operations with a dynamic nature. 

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`derivative <block:derivative>`                                                                                                                                                                     Computes the derivative of a quantity with 3 taps  (``x[t+1] - x[t-1]``). See also :ref:`block:derivative2`.                                                                                            
:ref:`derivative2 <block:derivative2>`                                                                                                                                                                   Computes the derivative of a quantity with 2 taps (``x[t+1] - x[t]``). See also :ref:`block:derivative`.                                                                                                
:ref:`forward_difference <block:forward_difference>`                                                                                                                                                     Computes ``x[t+1] - x[t-1]`` normalized with timestamp.                                                                                                                                                 
:ref:`fps_data_limit <block:fps_data_limit>`                                                                                                                                                             This block limits the output update to a certain framerate.                                                                                                                                             
:ref:`fps_print <block:fps_print>`                                                                                                                                                                       Prints the fps count for the input signals.                                                                                                                                                             
:ref:`history <block:history>`                                                                                                                                                                           This block collects the history of a quantity, and outputs two signals ``x`` and ``t``. See also :ref:`block:historyt` and :ref:`block:last_n_samples`.                                                 
:ref:`historyt <block:historyt>`                                                                                                                                                                         This block collects the signals samples of a signals, and outputs *one* signal containing a tuple  ``(t,x)``. See also :ref:`block:last_n_samples` and :ref:`block:history`.                            
:ref:`last_n_samples <block:last_n_samples>`                                                                                                                                                             This block collects the last N samples of a signals, and outputs two signals ``x`` and ``t``. See also :ref:`block:historyt` and :ref:`block:history`.                                                  
:ref:`sieve <block:sieve>`                                                                                                                                                                               This block decimates the data in time by transmitting only one in ``n`` updates.                                                                                                                        
:ref:`sync <block:sync>`                                                                                                                                                                                 This block synchronizes a set of streams to the first stream (the master).                                                                                                                              
:ref:`sync2 <block:sync2>`                                                                                                                                                                               This block synchronizes a set of N sensor streams.                                                                                                                                                      
:ref:`two_step_difference <block:two_step_difference>`                                                                                                                                                   Computes ``x[t+1] - x[t]`` normalized with timestamp.                                                                                                                                                   
:ref:`wait <block:wait>`                                                                                                                                                                                 This block waits a given number of updates before transmitting the output.                                                                                                                              
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.gui`

Blocks using Matplotlib to display data.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`fps_limit <block:fps_limit>`                                                                                                                                                                       This block limits the output update to a certain *realtime* framerate.                                                                                                                                  
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

Some functions specific to robotics applications.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`laser_display <block:laser_display>`                                                                                                                                                               Produces a plot of a range-finder scan.                                                                                                                                                                 
:ref:`pose2commands <block:pose2commands>`                                                                                                                                                               None                                                                                                                                                                                                    
:ref:`pose2vel_ <block:pose2vel_>`                                                                                                                                                                       None                                                                                                                                                                                                    
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph.components.signals`

Simple routins for signals extraction, combination.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`extract <block:extract>`                                                                                                                                                                           This block extracts some of the components of a vector.                                                                                                                                                 
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


.. rst-class:: procgraph:module

Module ``procgraph.components``
============================================================


.. _`block:clock`:


.. rst-class:: procgraph:block

clock
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 


.. _`block:constant`:


.. rst-class:: procgraph:block

constant
------------------------------------------------------------
Output a numerical constant that never changes. 

Example: ::

    |constant value=42 name=meaning| -> ...

Two parameters:

* ``value``, necessary
* ``name``, optional signal name (default: const)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 


.. _`block:gain`:


.. rst-class:: procgraph:block

gain
------------------------------------------------------------
FIXME: to be replaced by simpler function.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 


.. _`block:identity`:


.. rst-class:: procgraph:block

identity
------------------------------------------------------------
This block outputs the inputs, unchanged. 

This is an example of a block whose signal configuration is dynamics:
init() gets called twice.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 


.. _`block:info`:


.. rst-class:: procgraph:block

info
------------------------------------------------------------
Prints more compact information about the inputs than :ref:`block:print`. 

For numpy arrays it prints their shape and dtype instead of their values.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 


.. _`block:print`:


.. rst-class:: procgraph:block

print
------------------------------------------------------------
Print a representation of the input values along with their timestamp.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 


.. _`block:rand`:


.. rst-class:: procgraph:block

rand
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components.py>`_. 


.. _`module:procgraph.components.dynamic`:


.. rst-class:: procgraph:module

Module ``procgraph.components.dynamic``
============================================================



.. rst-class:: procgraph:desc

Blocks performing operations with a dynamic nature. 


.. rst-class:: procgraph:desc_rest


This library contains blocks that perform operations with time.
This library is autoloaded.

.. _`block:derivative`:


.. rst-class:: procgraph:block

derivative
------------------------------------------------------------
Computes the derivative of a quantity with 3 taps  (``x[t+1] - x[t-1]``). See also :ref:`block:derivative2`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: quantity to derive


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x_dot``: approximate derivative


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/derivative.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/derivative.py>`_. 


.. _`block:derivative2`:


.. rst-class:: procgraph:block

derivative2
------------------------------------------------------------
Computes the derivative of a quantity with 2 taps (``x[t+1] - x[t]``). See also :ref:`block:derivative`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: quantity to derive


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x_dot``: approximate derivative


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/derivative2.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/derivative2.py>`_. 


.. _`block:forward_difference`:


.. rst-class:: procgraph:block

forward_difference
------------------------------------------------------------
Computes ``x[t+1] - x[t-1]`` normalized with timestamp. 

You want to attach this to :ref:`block:last_n_samples`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x123``: An array with the last 3 values of x.

- ``t123``: An array with the last 3 values of the timestamp.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x_dot``: Derivative of x


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/derivative.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/derivative.py>`_. 


.. _`block:fps_data_limit`:


.. rst-class:: procgraph:block

fps_data_limit
------------------------------------------------------------
This block limits the output update to a certain framerate.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``fps``: Maximum framerate.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signals to decimate. (variable: 1 <= n <= None)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decimated signals. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/fps_data_limit.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/fps_data_limit.py>`_. 


.. _`block:fps_print`:


.. rst-class:: procgraph:block

fps_print
------------------------------------------------------------
Prints the fps count for the input signals.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

None (variable: 1 <= n <= None)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/fps_print.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/fps_print.py>`_. 


.. _`block:history`:


.. rst-class:: procgraph:block

history
------------------------------------------------------------
This block collects the history of a quantity, and outputs two signals ``x`` and ``t``. See also :ref:`block:historyt` and :ref:`block:last_n_samples`.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``interval``: Length of the interval to record.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Sequence of values.

- ``t``: Sequence of timestamps.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/history.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/history.py>`_. 


.. _`block:historyt`:


.. rst-class:: procgraph:block

historyt
------------------------------------------------------------
This block collects the signals samples of a signals, and outputs *one* signal containing a tuple  ``(t,x)``. See also :ref:`block:last_n_samples` and :ref:`block:history`.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``interval``: Length of interval (seconds).


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``history``: Tuple ``(t,x)`` containing two arrays.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/historyt.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/historyt.py>`_. 


.. _`block:last_n_samples`:


.. rst-class:: procgraph:block

last_n_samples
------------------------------------------------------------
This block collects the last N samples of a signals, and outputs two signals ``x`` and ``t``. See also :ref:`block:historyt` and :ref:`block:history`.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``n``: Number of samples to retain.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Sequence of values.

- ``t``: Sequence of timestamps.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/history.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/history.py>`_. 


.. _`block:sieve`:


.. rst-class:: procgraph:block

sieve
------------------------------------------------------------
This block decimates the data in time by transmitting only one in ``n`` updates.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``n``: Decimation level; ``n = 3`` means transmit one in three.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``data``: Arbitrary input signals.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``decimated``: Decimated signals.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/sieve.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/sieve.py>`_. 


.. _`block:sync`:


.. rst-class:: procgraph:block

sync
------------------------------------------------------------
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


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signals to synchronize. The first is the master. (variable: 2 <= n <= None)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Synchronized signals. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/sync.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/sync.py>`_. 


.. _`block:sync2`:


.. rst-class:: procgraph:block

sync2
------------------------------------------------------------
This block synchronizes a set of N sensor streams. 

The first signal is called the "master" signal.
The other (N-1) are slaves.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/sync2.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/sync2.py>`_. 


.. _`block:two_step_difference`:


.. rst-class:: procgraph:block

two_step_difference
------------------------------------------------------------
Computes ``x[t+1] - x[t]`` normalized with timestamp.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x12``: An array with the last 2 values of x.

- ``t12``: An array with the last 2 values of the timestamp.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x_dot``: Derivative of x


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/derivative2.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/derivative2.py>`_. 


.. _`block:wait`:


.. rst-class:: procgraph:block

wait
------------------------------------------------------------
This block waits a given number of updates before transmitting the output. 

Config:
- n (number of updates)

Input: variable
Output: variable (same as input)


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``n``: Number of updates to wait at the beginning.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arbitrary signals. (variable: None <= n <= None)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arbitrary signals, minus the first ``n`` updates. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/dynamic/wait.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/dynamic/wait.py>`_. 


.. _`module:procgraph.components.gui`:


.. rst-class:: procgraph:module

Module ``procgraph.components.gui``
============================================================



.. rst-class:: procgraph:desc

Blocks using Matplotlib to display data.

.. _`block:fps_limit`:


.. rst-class:: procgraph:block

fps_limit
------------------------------------------------------------
This block limits the output update to a certain *realtime* framerate. 

Note that this uses realtime wall clock time -- not the data time!
This is mean for real-time applications, such as visualization.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``fps``: Realtime fps limit.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arbitrary signals. (variable: None <= n <= None)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arbitrary signals with limited framerate. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/gui/fps_limit.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/gui/fps_limit.py>`_. 


.. _`block:plot`:


.. rst-class:: procgraph:block

plot
------------------------------------------------------------
Just plots the vector instantaneously


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/gui/plot.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/gui/plot.py>`_. 


.. _`module:procgraph.components.images`:


.. rst-class:: procgraph:module

Module ``procgraph.components.images``
============================================================



.. rst-class:: procgraph:desc

Blocks for basic operations on images. 


.. rst-class:: procgraph:desc_rest

The  module contains blocks that perform basic operations
on images. The library is autoloaded and has no software dependency.

For more complex operations see also:

* :ref:`module:procgraph.components.cv`
* :ref:`module:procgraph.components.pil`


**Example**

Convert a RGB image to grayscale, and back to a RGB image:::


    |input| -> |rgb2gray| -> |gray2rgb| -> |output|

.. _`block:compose`:


.. rst-class:: procgraph:block

compose
------------------------------------------------------------
Configuration: 

- ``width``, ``height``: dimension in  pixels
- ``positions``: a structure giving the position of each signal in the canvas. Example: ::

      compose.positions = {y: [0,0], ys: [320,20]}


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/images/compose.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/compose.py>`_. 


.. _`block:gray2rgb`:


.. rst-class:: procgraph:block

gray2rgb
------------------------------------------------------------
Converts a H x W grayscale into a H x W x 3 RGB by replicating channel.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/images/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/filters.py>`_. 


.. _`block:grayscale`:


.. rst-class:: procgraph:block

grayscale
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/images/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/filters.py>`_. 


.. _`block:grid`:


.. rst-class:: procgraph:block

grid
------------------------------------------------------------
A block that creates a larger image by arranging them in a grid.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/images/imggrid.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/imggrid.py>`_. 


.. _`block:posneg`:


.. rst-class:: procgraph:block

posneg
------------------------------------------------------------
Converts a 2D value to normalized uint8 RGB red=positive, blue=negative 0-255.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/images/copied_from_reprep.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/copied_from_reprep.py>`_. 


.. _`block:rgb2gray`:


.. rst-class:: procgraph:block

rgb2gray
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/images/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/filters.py>`_. 


.. _`block:scale`:


.. rst-class:: procgraph:block

scale
------------------------------------------------------------
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


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/images/copied_from_reprep.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/images/copied_from_reprep.py>`_. 


.. _`module:procgraph.components.misc`:


.. rst-class:: procgraph:module

Module ``procgraph.components.misc``
============================================================



.. rst-class:: procgraph:desc

Miscellaneous functions to be better organized.

.. _`block:as_json`:


.. rst-class:: procgraph:block

as_json
------------------------------------------------------------
Converts the input into a JSON string.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/misc/json_misc.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/misc/json_misc.py>`_. 


.. _`block:pickle`:


.. rst-class:: procgraph:block

pickle
------------------------------------------------------------
Dumps the input as a pickle file.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/misc/pickling.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/misc/pickling.py>`_. 


.. _`block:to_file`:


.. rst-class:: procgraph:block

to_file
------------------------------------------------------------
Prints the input line by line to a given file.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/misc/to_file.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/misc/to_file.py>`_. 


.. _`module:procgraph.components.numpy_ops`:


.. rst-class:: procgraph:module

Module ``procgraph.components.numpy_ops``
============================================================



.. rst-class:: procgraph:desc

Various operations wrapping numpy functions.

.. _`block:*`:


.. rst-class:: procgraph:block

*
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:+`:


.. rst-class:: procgraph:block

+
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:-`:


.. rst-class:: procgraph:block

-
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:/`:


.. rst-class:: procgraph:block

/
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:abs`:


.. rst-class:: procgraph:block

abs
------------------------------------------------------------
Wrapper around :py:func:`numpy.core.umath.absolute`.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:astype`:


.. rst-class:: procgraph:block

astype
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:dstack`:


.. rst-class:: procgraph:block

dstack
------------------------------------------------------------
Wrapper around :py:func:`numpy.dstack`.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:gradient1d`:


.. rst-class:: procgraph:block

gradient1d
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/gradient1d.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/gradient1d.py>`_. 


.. _`block:hstack`:


.. rst-class:: procgraph:block

hstack
------------------------------------------------------------
Wrapper around :py:func:`numpy.hstack`.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:log`:


.. rst-class:: procgraph:block

log
------------------------------------------------------------
Wrapper around :py:func:`numpy.core.umath.log`.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:outer`:


.. rst-class:: procgraph:block

outer
------------------------------------------------------------
Wrapper around :py:func:`numpy.multiply.outer`.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:select`:


.. rst-class:: procgraph:block

select
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:sign`:


.. rst-class:: procgraph:block

sign
------------------------------------------------------------
Wrapper around :py:func:`numpy.core.umath.sign`.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:square`:


.. rst-class:: procgraph:block

square
------------------------------------------------------------
Wrapper around :py:func:`numpy.core.umath.square`.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:take`:


.. rst-class:: procgraph:block

take
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`block:vstack`:


.. rst-class:: procgraph:block

vstack
------------------------------------------------------------
Wrapper around :py:func:`numpy.vstack`.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/numpy_ops/filters.py>`_. 


.. _`module:procgraph.components.robotics`:


.. rst-class:: procgraph:module

Module ``procgraph.components.robotics``
============================================================



.. rst-class:: procgraph:desc

Some functions specific to robotics applications.

.. _`block:laser_display`:


.. rst-class:: procgraph:block

laser_display
------------------------------------------------------------
Produces a plot of a range-finder scan. 


display_sick.groups = [{ indices: [0,179], theta: [-1.57,+1.57],
         color: 'r', origin: [0,0,0]}]


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/robotics/laser_display.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/robotics/laser_display.py>`_. 


.. _`block:pose2commands`:


.. rst-class:: procgraph:block

pose2commands
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/robotics/pose2velocity.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/robotics/pose2velocity.py>`_. 


.. _`block:pose2vel_`:


.. rst-class:: procgraph:block

pose2vel_
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/robotics/pose2velocity.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/robotics/pose2velocity.py>`_. 


.. _`module:procgraph.components.signals`:


.. rst-class:: procgraph:module

Module ``procgraph.components.signals``
============================================================



.. rst-class:: procgraph:desc

Simple routins for signals extraction, combination.

.. _`block:extract`:


.. rst-class:: procgraph:block

extract
------------------------------------------------------------
This block extracts some of the components of a vector. 

Arguments:

- index


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/signals/extract.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/signals/extract.py>`_. 


.. _`block:join`:


.. rst-class:: procgraph:block

join
------------------------------------------------------------
This block joins multiple signals into one.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/signals/join.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/signals/join.py>`_. 


.. _`module:procgraph.components.statistics`:


.. rst-class:: procgraph:module

Module ``procgraph.components.statistics``
============================================================



.. rst-class:: procgraph:desc

Blocks for common statistical operations.

.. _`block:cov2corr`:


.. rst-class:: procgraph:block

cov2corr
------------------------------------------------------------
Compute the correlation matrix from the covariance matrix. If zero_diagonal = True, the diagonal is set to 0 instead of 1.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/statistics/cov2corr.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/cov2corr.py>`_. 


.. _`block:covariance`:


.. rst-class:: procgraph:block

covariance
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/statistics/covariance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/covariance.py>`_. 


.. _`block:expectation`:


.. rst-class:: procgraph:block

expectation
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/statistics/expectation.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/expectation.py>`_. 


.. _`block:normalize`:


.. rst-class:: procgraph:block

normalize
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/statistics/covariance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/covariance.py>`_. 


.. _`block:soft_variance`:


.. rst-class:: procgraph:block

soft_variance
------------------------------------------------------------
Computes the element-wise "soft" variance (expectation of error absolute value)


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``wait`` (default: 100): Number of samples to wait before declaring the expectation valid.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/statistics/variance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/variance.py>`_. 


.. _`block:variance`:


.. rst-class:: procgraph:block

variance
------------------------------------------------------------
Computes the element-wise variance.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``wait`` (default: 100): Number of samples to wait before declaring the expectation valid.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/statistics/variance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/statistics/variance.py>`_. 


.. _`module:procgraph.components.video`:


.. rst-class:: procgraph:module

Module ``procgraph.components.video``
============================================================



.. rst-class:: procgraph:desc

Blocks for encoding/decoding video based on MPlayer.

.. _`block:SimpleCompression`:


.. rst-class:: procgraph:block

SimpleCompression
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/video/simple_compression.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/video/simple_compression.py>`_. 


.. _`block:mencoder`:


.. rst-class:: procgraph:block

mencoder
------------------------------------------------------------
Encodes a video stream using ``mencoder``. 

Note that allowed codec and bitrate depend on your version of mencoder.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``file``: Output file (AVI format.)

- ``fps`` (default: 10): Framerate of resulting movie.

- ``vcodec`` (default: mpeg4): Codec to use.

- ``vbitrate`` (default: 1000000): Bitrate -- default is reasonable.

- ``quiet`` (default: True): If True, suppress mencoder's messages


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``image``: H x W x 3  uint8 numpy array representing an RGB image.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/video/mencoder.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/video/mencoder.py>`_. 


.. _`block:mplayer`:


.. rst-class:: procgraph:block

mplayer
------------------------------------------------------------
Plays a video stream. 

Config:
    - file


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/video/mplayer.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/video/mplayer.py>`_. 


