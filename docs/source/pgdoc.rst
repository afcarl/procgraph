.. |towrite| replace:: **to write** 

.. _`pgdoc:procgraph.components`:

Summary 
============================================================


:ref:`module:procgraph.components.debug_components`

Components used for debugging and unit tests.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`* <block:*>`                                                                                                                                                                                       |towrite|                                                                                                                                                                                               
:ref:`+ <block:+>`                                                                                                                                                                                       |towrite|                                                                                                                                                                                               
:ref:`- <block:->`                                                                                                                                                                                       Implements the difference of two signals, taking care of overflows.                                                                                                                                     
:ref:`/ <block:/>`                                                                                                                                                                                       |towrite|                                                                                                                                                                                               
:ref:`constant <block:constant>`                                                                                                                                                                         Output a numerical constant that never changes.                                                                                                                                                         
:ref:`gain <block:gain>`                                                                                                                                                                                 A simple example of a gain block.                                                                                                                                                                       
:ref:`identity <block:identity>`                                                                                                                                                                         This block outputs the inputs, unchanged.                                                                                                                                                               
:ref:`info <block:info>`                                                                                                                                                                                 Prints more compact information about the inputs than :ref:`block:print`.                                                                                                                               
:ref:`print <block:print>`                                                                                                                                                                               Print a representation of the input values along with their timestamp.                                                                                                                                  
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_cv`

Operations using the OpenCV library. 

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`gradient <block:gradient>`                                                                                                                                                                         Computes the gradient of an image Input:  a 2D numpy array with float32 Outpt:  gx, gy: a 2D numpy array with float32                                                                                   
:ref:`smooth <block:smooth>`                                                                                                                                                                             Smooths an image.                                                                                                                                                                                       
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_foo`

An example package for ProcGraph that shows how to organize your code. 

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`block_example <block:block_example>`                                                                                                                                                               This is a documented example of the simplest block possible.                                                                                                                                            
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_hdf`

This is a set of blocks to read and write logs in HDF5 format. 

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`hdfread <block:hdfread>`                                                                                                                                                                           This block reads a log written with HDFwrite.                                                                                                                                                           
:ref:`hdfread_test <block:hdfread_test>`                                                                                                                                                                 This is a simple test that reading from HDF files is happening correctly.                                                                                                                               
:ref:`hdfwrite <block:hdfwrite>`                                                                                                                                                                         This block writes the incoming signals to a file in HDF_ format.                                                                                                                                        
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_images`

Blocks for basic operations on images. 

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`blend <block:blend>`                                                                                                                                                                               This block blends two or more images.                                                                                                                                                                   
:ref:`border <block:border>`                                                                                                                                                                             Adds a block around the input image.                                                                                                                                                                    
:ref:`compose <block:compose>`                                                                                                                                                                           Compose several images in the same canvas. You should probably use :ref:`block:grid` in many situations.                                                                                                
:ref:`gray2rgb <block:gray2rgb>`                                                                                                                                                                         Converts a H x W grayscale into a H x W x 3 RGB by replicating channel.                                                                                                                                 
:ref:`grayscale <block:grayscale>`                                                                                                                                                                       |towrite|                                                                                                                                                                                               
:ref:`grid <block:grid>`                                                                                                                                                                                 A block that creates a larger image by arranging them in a grid.                                                                                                                                        
:ref:`posneg <block:posneg>`                                                                                                                                                                             Converts a 2D value to normalized uint8 RGB red=positive, blue=negative 0-255.                                                                                                                          
:ref:`rgb2gray <block:rgb2gray>`                                                                                                                                                                         |towrite|                                                                                                                                                                                               
:ref:`scale <block:scale>`                                                                                                                                                                               Provides a RGB representation of the values by interpolating the range [min(value),max(value)] into the colorspace [min_color, max_color].                                                              
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_io_misc`

Miscellaneous functions to be better organized.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`as_json <block:as_json>`                                                                                                                                                                           Converts the input into a JSON string.                                                                                                                                                                  
:ref:`pickle <block:pickle>`                                                                                                                                                                             Dumps the input as a :py:mod:`pickle` file.                                                                                                                                                             
:ref:`pickle_group <block:pickle_group>`                                                                                                                                                                 Dumps the input as a :py:mod:`pickle` file, in the form of a dictionary  signal name -> value.                                                                                                          
:ref:`to_file <block:to_file>`                                                                                                                                                                           Prints the input line by line to a given file.                                                                                                                                                          
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_mpl`

Blocks using Matplotlib to display data.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`plot <block:plot>`                                                                                                                                                                                 Plots the inputs using matplotlib.                                                                                                                                                                      
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_mplayer`

Blocks for encoding/decoding video based on MPlayer.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`mencoder <block:mencoder>`                                                                                                                                                                         Encodes a video stream using ``mencoder``.                                                                                                                                                              
:ref:`mplayer <block:mplayer>`                                                                                                                                                                           Decodes a video stream.                                                                                                                                                                                 
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_numpy_ops`

Various operations wrapping numpy functions.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`abs <block:abs>`                                                                                                                                                                                   Wrapper around :py:func:`numpy.core.umath.absolute`.                                                                                                                                                    
:ref:`arctan <block:arctan>`                                                                                                                                                                             Wrapper around :py:func:`numpy.arctan`.                                                                                                                                                                 
:ref:`astype <block:astype>`                                                                                                                                                                             |towrite|                                                                                                                                                                                               
:ref:`deg2rad <block:deg2rad>`                                                                                                                                                                           Converts degrees to radians.                                                                                                                                                                            
:ref:`dstack <block:dstack>`                                                                                                                                                                             Wrapper around :py:func:`numpy.dstack`.                                                                                                                                                                 
:ref:`fliplr <block:fliplr>`                                                                                                                                                                             Wrapper for :py:func:`numpy.fliplr`.                                                                                                                                                                    
:ref:`flipud <block:flipud>`                                                                                                                                                                             Wrapper for :py:func:`numpy.flipud`.                                                                                                                                                                    
:ref:`gradient1d <block:gradient1d>`                                                                                                                                                                     |towrite|                                                                                                                                                                                               
:ref:`hstack <block:hstack>`                                                                                                                                                                             Wrapper around :py:func:`numpy.hstack`.                                                                                                                                                                 
:ref:`log <block:log>`                                                                                                                                                                                   Wrapper around :py:func:`numpy.core.umath.log`.                                                                                                                                                         
:ref:`max <block:max>`                                                                                                                                                                                   Maximum over all elements.                                                                                                                                                                              
:ref:`maximum <block:maximum>`                                                                                                                                                                           |towrite|                                                                                                                                                                                               
:ref:`mean <block:mean>`                                                                                                                                                                                 Compute the arithmetic mean along the specified axis.                                                                                                                                                   
:ref:`minimum <block:minimum>`                                                                                                                                                                           |towrite|                                                                                                                                                                                               
:ref:`normalize_Linf <block:normalize_Linf>`                                                                                                                                                             Normalize a vector such that ``|x|_inf = max(abs(x))= 1``                                                                                                                                               
:ref:`outer <block:outer>`                                                                                                                                                                               Wrapper around :py:func:`numpy.multiply.outer`.                                                                                                                                                         
:ref:`rad2deg <block:rad2deg>`                                                                                                                                                                           Converts radians to degrees.                                                                                                                                                                            
:ref:`select <block:select>`                                                                                                                                                                             |towrite|                                                                                                                                                                                               
:ref:`sign <block:sign>`                                                                                                                                                                                 Wrapper around :py:func:`numpy.core.umath.sign`.                                                                                                                                                        
:ref:`smooth1d <block:smooth1d>`                                                                                                                                                                         smooth the data using a window with requested size.                                                                                                                                                     
:ref:`square <block:square>`                                                                                                                                                                             Wrapper around :py:func:`numpy.core.umath.square`.                                                                                                                                                      
:ref:`sum <block:sum>`                                                                                                                                                                                   Sum over all elements.                                                                                                                                                                                  
:ref:`take <block:take>`                                                                                                                                                                                 |towrite|                                                                                                                                                                                               
:ref:`vstack <block:vstack>`                                                                                                                                                                             Wrapper around :py:func:`numpy.vstack`.                                                                                                                                                                 
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_pil`

Blocks for image operations based on the PIL library

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`imread <block:imread>`                                                                                                                                                                             |towrite|                                                                                                                                                                                               
:ref:`resize <block:resize>`                                                                                                                                                                             |towrite|                                                                                                                                                                                               
:ref:`text <block:text>`                                                                                                                                                                                 This block provides text overlays over an image.                                                                                                                                                        
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_robotics`

Some functions specific to robotics applications. 

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`laser_display <block:laser_display>`                                                                                                                                                               Produces a plot of a range-finder scan.                                                                                                                                                                 
:ref:`laser_dot_display <block:laser_dot_display>`                                                                                                                                                       Produces a plot of a range-finder scan variation (derivative).                                                                                                                                          
:ref:`organic_scale <block:organic_scale>`                                                                                                                                                               A (almost failed) attempt to scale a signal into [-1,1] according to the history.                                                                                                                       
:ref:`pose2commands <block:pose2commands>`                                                                                                                                                               Computes the velocity commands from the odometry data.                                                                                                                                                  
:ref:`pose2vel_ <block:pose2vel_>`                                                                                                                                                                       Block used by :ref:`block:pose2commands`.                                                                                                                                                               
:ref:`skim <block:skim>`                                                                                                                                                                                 Skims the top and bottom percentile from the data.                                                                                                                                                      
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_signals`

Blocks performing operations with a dynamic nature. 

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`derivative <block:derivative>`                                                                                                                                                                     Computes the derivative of a quantity with 3 taps  (``x[t+1] - x[t-1]``). See also :ref:`block:derivative2`.                                                                                            
:ref:`derivative2 <block:derivative2>`                                                                                                                                                                   Computes the derivative of a quantity with 2 taps (``x[t+1] - x[t]``). See also :ref:`block:derivative`.                                                                                                
:ref:`extract <block:extract>`                                                                                                                                                                           This block extracts some of the components of a vector.                                                                                                                                                 
:ref:`forward_difference <block:forward_difference>`                                                                                                                                                     Computes ``x[t+1] - x[t-1]`` normalized with timestamp.                                                                                                                                                 
:ref:`fps_data_limit <block:fps_data_limit>`                                                                                                                                                             This block limits the output update to a certain framerate.                                                                                                                                             
:ref:`fps_limit <block:fps_limit>`                                                                                                                                                                       This block limits the output update to a certain *realtime* framerate.                                                                                                                                  
:ref:`fps_print <block:fps_print>`                                                                                                                                                                       Prints the fps count for the input signals.                                                                                                                                                             
:ref:`history <block:history>`                                                                                                                                                                           This block collects the history of a quantity, and outputs two signals ``x`` and ``t``. See also :ref:`block:historyt` and :ref:`block:last_n_samples`.                                                 
:ref:`historyt <block:historyt>`                                                                                                                                                                         This block collects the signals samples of a signals, and outputs *one* signal containing a tuple  ``(t,x)``. See also :ref:`block:last_n_samples` and :ref:`block:history`.                            
:ref:`join <block:join>`                                                                                                                                                                                 This block joins multiple signals into one.                                                                                                                                                             
:ref:`last_n_samples <block:last_n_samples>`                                                                                                                                                             This block collects the last N samples of a signals, and outputs two signals ``x`` and ``t``. See also :ref:`block:historyt` and :ref:`block:history`.                                                  
:ref:`low_pass <block:low_pass>`                                                                                                                                                                         Implements simple low-pass filtering.                                                                                                                                                                   
:ref:`make_tuple <block:make_tuple>`                                                                                                                                                                     Creates a tuple out of the input signals values.                                                                                                                                                        
:ref:`sieve <block:sieve>`                                                                                                                                                                               This block decimates the data in time by transmitting only one in ``n`` updates.                                                                                                                        
:ref:`slice <block:slice>`                                                                                                                                                                               Slices a signal by extracting from index ``start`` to index ``end`` (INCLUSIVE).                                                                                                                        
:ref:`sync <block:sync>`                                                                                                                                                                                 This block synchronizes a set of streams to the first stream (the master).                                                                                                                              
:ref:`two_step_difference <block:two_step_difference>`                                                                                                                                                   Computes ``x[t+1] - x[t]`` normalized with timestamp.                                                                                                                                                   
:ref:`wait <block:wait>`                                                                                                                                                                                 This block waits a given number of updates before transmitting the output.                                                                                                                              
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


:ref:`module:procgraph_statistics`

Blocks for common statistical operations.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`cov2corr <block:cov2corr>`                                                                                                                                                                         Compute the correlation matrix from the covariance matrix. If zero_diagonal = True, the diagonal is set to 0 instead of 1.                                                                              
:ref:`covariance <block:covariance>`                                                                                                                                                                     Computes the covariance matrix of the input                                                                                                                                                             
:ref:`expectation <block:expectation>`                                                                                                                                                                   Computes the sample expectation of a signal.                                                                                                                                                            
:ref:`normalize <block:normalize>`                                                                                                                                                                       Removes the mean from a signal.                                                                                                                                                                         
:ref:`soft_variance <block:soft_variance>`                                                                                                                                                               Computes the element-wise "soft" variance (expectation of error absolute value)                                                                                                                         
:ref:`variance <block:variance>`                                                                                                                                                                         Computes the element-wise variance.                                                                                                                                                                     
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


.. _`module:procgraph.components.debug_components`:


.. rst-class:: procgraph:module

Package ``procgraph.components.debug_components``
============================================================



.. rst-class:: procgraph:desc

Components used for debugging and unit tests.

.. _`block:*`:


.. rst-class:: procgraph:block

``*``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|

- ``1``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components/operations.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components/operations.py>`_. 


.. _`block:+`:


.. rst-class:: procgraph:block

``+``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|

- ``1``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components/operations.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components/operations.py>`_. 


.. _`block:-`:


.. rst-class:: procgraph:block

``-``
------------------------------------------------------------
Implements the difference of two signals, taking care of overflows. 

Because that is rarely the semantics you want to give them.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``safe`` (default: None): Whether to use safe promotions. If not specified, we will do it but warn once.

- ``cases`` (default: {'uint16': 'int32', 'uint8': 'int16', 'uint32': 'int64'}): Promotion rules


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: First signal

- ``y``: Second signal


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x_minus_y``: Result of x - y


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components/operations.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components/operations.py>`_. 


.. _`block:/`:


.. rst-class:: procgraph:block

``/``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|

- ``1``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components/operations.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components/operations.py>`_. 


.. _`block:constant`:


.. rst-class:: procgraph:block

``constant``
------------------------------------------------------------
Output a numerical constant that never changes. 

Example: ::

    |constant value=42 name=meaning| -> ...

Two parameters:

* ``value``, necessary
* ``name``, optional signal name (default: const)


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``value``: Constant value to output.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``constant``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components/constant.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components/constant.py>`_. 


.. _`block:gain`:


.. rst-class:: procgraph:block

``gain``
------------------------------------------------------------
A simple example of a gain block.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``k``: Multiplicative gain


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``in``: Input value


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``out``: Output multiplied by k.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components/gain.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components/gain.py>`_. 


.. _`block:identity`:


.. rst-class:: procgraph:block

``identity``
------------------------------------------------------------
This block outputs the inputs, unchanged. 

This is an example of a block whose signal configuration is dynamics:
init() gets called twice.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Input signals. (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Output signals, equal to input. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components/identity.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components/identity.py>`_. 


.. _`block:info`:


.. rst-class:: procgraph:block

``info``
------------------------------------------------------------
Prints more compact information about the inputs than :ref:`block:print`. 

For numpy arrays it prints their shape and dtype instead of their values.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signals to describe. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components/info.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components/info.py>`_. 


.. _`block:print`:


.. rst-class:: procgraph:block

``print``
------------------------------------------------------------
Print a representation of the input values along with their timestamp.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signals to print. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph/components/debug_components/printc.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph/components/debug_components/printc.py>`_. 


.. _`module:procgraph_cv`:


.. rst-class:: procgraph:module

Package ``procgraph_cv``
============================================================



.. rst-class:: procgraph:desc

Operations using the OpenCV library. 


.. rst-class:: procgraph:desc_rest

**Packages dependencies**

* ``opencv`` (or ``cv``)

.. _`block:gradient`:


.. rst-class:: procgraph:block

``gradient``
------------------------------------------------------------
Computes the gradient of an image Input:  a 2D numpy array with float32 Outpt:  gx, gy: a 2D numpy array with float32


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``aperture_size`` (default: 3): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|

- ``1``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_cv/opencv_utils.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_cv/opencv_utils.py>`_. 


.. _`block:smooth`:


.. rst-class:: procgraph:block

``smooth``
------------------------------------------------------------
Smooths an image. 

Input:

* grayscale:  a 2D numpy float32 array.

Output:

* a 2D  numpy float32 array.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``gaussian_std`` (default: 5.0): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_cv/opencv_utils.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_cv/opencv_utils.py>`_. 


.. _`module:procgraph_foo`:


.. rst-class:: procgraph:module

Package ``procgraph_foo``
============================================================



.. rst-class:: procgraph:desc

An example package for ProcGraph that shows how to organize your code. 


.. rst-class:: procgraph:desc_rest

This is the documentation string for the package. Like all docstrings,
it consists of a short summary (above) and a longer description (this.)

.. _`block:block_example`:


.. rst-class:: procgraph:block

``block_example``
------------------------------------------------------------
This is a documented example of the simplest block possible. 

This docstring will be included in the generated documentation.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``bias`` (default: 0): Bias for the accelerator.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``baz``: Measured baz in the particle accelerator.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``baz_compensated``: Compensated baz value according to calibration.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_foo/example0_simplest_block.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_foo/example0_simplest_block.py>`_. 


.. _`module:procgraph_hdf`:


.. rst-class:: procgraph:module

Package ``procgraph_hdf``
============================================================



.. rst-class:: procgraph:desc

This is a set of blocks to read and write logs in HDF5 format. 


.. rst-class:: procgraph:desc_rest

You need the ``pytables`` package to be installed.

.. _`block:hdfread`:


.. rst-class:: procgraph:block

``hdfread``
------------------------------------------------------------
This block reads a log written with HDFwrite.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``file``: HDF file to read

- ``signals`` (default: None): Which signals to output (and in what order). Should be a comma-separated list. If you do not specify it will be all signal in the original order


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|towrite| (number defined at runtime


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_hdf/hdfread.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_hdf/hdfread.py>`_. 


.. _`block:hdfread_test`:


.. rst-class:: procgraph:block

``hdfread_test``
------------------------------------------------------------
This is a simple test that reading from HDF files is happening correctly.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``file``: input hdf file


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_hdf/models/hdfread_test.pg <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_hdf/models/hdfread_test.pg>`_. 


.. _`block:hdfwrite`:


.. rst-class:: procgraph:block

``hdfwrite``
------------------------------------------------------------
This block writes the incoming signals to a file in HDF_ format. 

.. HDF: http://en.wikipedia.org/wiki/Hierarchical_Data_Format

The HDF format is organized as follows: ::

     /            (root)
     /procgraph_log             (group with name procgraph)
     /procgraph_log/signal1     (table)
     /procgraph_log/signal2     (table)
     ...

Each table has the following fields:

     time         (float)
     value        (the datatype of the signal)

If a signal changes datatype, then an error is thrown.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``file``: HDF file to write

- ``compress`` (default: 1): Whether to compress the hdf table.

- ``complib`` (default: zlib): Compression library (zlib, bzip2, blosc, lzo).

- ``complevel`` (default: 9): Compression level (0-9)


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signals to be written (variable number: n >= 1)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_hdf/hdfwrite.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_hdf/hdfwrite.py>`_. 


.. _`module:procgraph_images`:


.. rst-class:: procgraph:module

Package ``procgraph_images``
============================================================



.. rst-class:: procgraph:desc

Blocks for basic operations on images. 


.. rst-class:: procgraph:desc_rest

The  module contains blocks that perform basic operations
on images. The library is autoloaded and has no software dependency.

For more complex operations see also:

* :ref:`module:procgraph_cv`
* :ref:`module:procgraph_pil`


**Example**

Convert a RGB image to grayscale, and back to a RGB image:::


    |input| -> |rgb2gray| -> |gray2rgb| -> |output|

.. _`block:blend`:


.. rst-class:: procgraph:block

``blend``
------------------------------------------------------------
This block blends two or more images. 

RGB images are interpreted as having full alpha (opaque)

All images must have the same width.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

images to blend (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``rgb``: The output is a RGB image (no alpha)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_images/blend.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_images/blend.py>`_. 


.. _`block:border`:


.. rst-class:: procgraph:block

``border``
------------------------------------------------------------
Adds a block around the input image.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``color`` (default: [1, 1, 1]): border color

- ``left`` (default: 0): pixel length for left border

- ``right`` (default: 0): pixel length for right border

- ``top`` (default: 0): pixel length for top border

- ``bottom`` (default: 0): pixel length for bottom border


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``rgb``: Input image.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``rgb``: Image with borders added around.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_images/border.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_images/border.py>`_. 


.. _`block:compose`:


.. rst-class:: procgraph:block

``compose``
------------------------------------------------------------
Compose several images in the same canvas. You should probably use :ref:`block:grid` in many situations. 

Example configuration: ::

    compose.positions = {y: [0,0], ys: [320,20]}


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``width``: Dimension in pixels.

- ``height``: Dimension in pixels.

- ``positions``: A structure giving the position of each signal in the canvas.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Images to compose. (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``canvas``: RGB image


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_images/compose.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_images/compose.py>`_. 


.. _`block:gray2rgb`:


.. rst-class:: procgraph:block

``gray2rgb``
------------------------------------------------------------
Converts a H x W grayscale into a H x W x 3 RGB by replicating channel.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_images/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_images/filters.py>`_. 


.. _`block:grayscale`:


.. rst-class:: procgraph:block

``grayscale``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_images/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_images/filters.py>`_. 


.. _`block:grid`:


.. rst-class:: procgraph:block

``grid``
------------------------------------------------------------
A block that creates a larger image by arranging them in a grid.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``cols`` (default: None): Columns in the grid.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Images to arrange in a grid. (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``grid``: Images arranged in a grid.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_images/imggrid.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_images/imggrid.py>`_. 


.. _`block:posneg`:


.. rst-class:: procgraph:block

``posneg``
------------------------------------------------------------
Converts a 2D value to normalized uint8 RGB red=positive, blue=negative 0-255.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``max_value`` (default: None): |towrite|

- ``skim`` (default: 0): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_images/copied_from_reprep.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_images/copied_from_reprep.py>`_. 


.. _`block:rgb2gray`:


.. rst-class:: procgraph:block

``rgb2gray``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_images/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_images/filters.py>`_. 


.. _`block:scale`:


.. rst-class:: procgraph:block

``scale``
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


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``max_value`` (default: None): |towrite|

- ``nan_color`` (default: [1, 0, 0]): |towrite|

- ``min_value`` (default: None): |towrite|

- ``min_color`` (default: [1, 1, 1]): |towrite|

- ``max_color`` (default: [0, 0, 0]): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_images/copied_from_reprep.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_images/copied_from_reprep.py>`_. 


.. _`module:procgraph_io_misc`:


.. rst-class:: procgraph:module

Package ``procgraph_io_misc``
============================================================



.. rst-class:: procgraph:desc

Miscellaneous functions to be better organized.

.. _`block:as_json`:


.. rst-class:: procgraph:block

``as_json``
------------------------------------------------------------
Converts the input into a JSON string. 

TODO: add example


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inputs to transcribe as JSON. (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``json``: JSON string.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_io_misc/json_misc.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_io_misc/json_misc.py>`_. 


.. _`block:pickle`:


.. rst-class:: procgraph:block

``pickle``
------------------------------------------------------------
Dumps the input as a :py:mod:`pickle` file.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``file``: File to write to.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Anything pickable.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_io_misc/pickling.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_io_misc/pickling.py>`_. 


.. _`block:pickle_group`:


.. rst-class:: procgraph:block

``pickle_group``
------------------------------------------------------------
Dumps the input as a :py:mod:`pickle` file, in the form of a dictionary  signal name -> value.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``file``: File to write to.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|towrite| (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_io_misc/pickling.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_io_misc/pickling.py>`_. 


.. _`block:to_file`:


.. rst-class:: procgraph:block

``to_file``
------------------------------------------------------------
Prints the input line by line to a given file.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``file``: File to write.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``values``: Anything you wish to print to file.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_io_misc/to_file.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_io_misc/to_file.py>`_. 


.. _`module:procgraph_mpl`:


.. rst-class:: procgraph:module

Package ``procgraph_mpl``
============================================================



.. rst-class:: procgraph:desc

Blocks using Matplotlib to display data.

.. _`block:plot`:


.. rst-class:: procgraph:block

``plot``
------------------------------------------------------------
Plots the inputs using matplotlib. 

This block accepts an arbitrary number of signals.
Each signals is treated independently and plot separately.

Each signal can either be:

1.  A tuple of length 2. It is interpreted as a tuple ``(x,y)``,
    and we plot ``x`` versus ``y`` (see also :ref:`block:make_tuple`).

2.  A list of numbers, or a 1-dimensional numpy array of length N.
    In this case, it is interpreted as the y values, and we set  ``x = 1:N``.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``width`` (default: 320): Image dimension

- ``height`` (default: 240): Image dimension

- ``xlabel`` (default: None): |towrite|

- ``ylabel`` (default: None): |towrite|

- ``legend`` (default: None): |towrite|

- ``title`` (default: None): |towrite|

- ``format`` (default: -): |towrite|

- ``symmetric`` (default: False): An alternative to y_min, y_max. Makes sure the plot is symmetric for y.

- ``x_min`` (default: None): |towrite|

- ``x_max`` (default: None): |towrite|

- ``y_min`` (default: None): |towrite|

- ``y_max`` (default: None): |towrite|

- ``keep`` (default: False): |towrite|

- ``transparent`` (default: False): If true, outputs a RGBA image instead of RGB.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Data to plot. (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``rgb``: Resulting image.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_mpl/plot.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_mpl/plot.py>`_. 


.. _`module:procgraph_mplayer`:


.. rst-class:: procgraph:module

Package ``procgraph_mplayer``
============================================================



.. rst-class:: procgraph:desc

Blocks for encoding/decoding video based on MPlayer.

.. _`block:mencoder`:


.. rst-class:: procgraph:block

``mencoder``
------------------------------------------------------------
Encodes a video stream using ``mencoder``. 

Note that allowed codec and bitrate depend on your version of mencoder.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``file``: Output file (AVI format.)

- ``fps`` (default: None): Framerate of resulting movie. If not specified, it will be guessed from data.

- ``fps_safe`` (default: 10): If the frame autodetect gives strange results, we use this safe value instead.

- ``vcodec`` (default: mpeg4): Codec to use.

- ``vbitrate`` (default: 2000000): Bitrate -- default is reasonable.

- ``quiet`` (default: True): If True, suppress mencoder's messages

- ``timestamps`` (default: True): If True, also writes <file>.timestamps that includes a line with the timestamp for each frame


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``image``: H x W x 3  uint8 numpy array representing an RGB image.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_mplayer/mencoder.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_mplayer/mencoder.py>`_. 


.. _`block:mplayer`:


.. rst-class:: procgraph:block

``mplayer``
------------------------------------------------------------
Decodes a video stream.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``file``: Input video file. Any format that ``mplayer`` understands.

- ``quiet`` (default: True): If true, suppress messages from mplayer.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``video``: RGB stream as numpy array.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_mplayer/mplayer.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_mplayer/mplayer.py>`_. 


.. _`module:procgraph_numpy_ops`:


.. rst-class:: procgraph:module

Package ``procgraph_numpy_ops``
============================================================



.. rst-class:: procgraph:desc

Various operations wrapping numpy functions.

.. _`block:abs`:


.. rst-class:: procgraph:block

``abs``
------------------------------------------------------------
Wrapper around :py:func:`numpy.core.umath.absolute`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:arctan`:


.. rst-class:: procgraph:block

``arctan``
------------------------------------------------------------
Wrapper around :py:func:`numpy.arctan`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:astype`:


.. rst-class:: procgraph:block

``astype``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``dtype``: |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:deg2rad`:


.. rst-class:: procgraph:block

``deg2rad``
------------------------------------------------------------
Converts degrees to radians.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:dstack`:


.. rst-class:: procgraph:block

``dstack``
------------------------------------------------------------
Wrapper around :py:func:`numpy.dstack`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|

- ``1``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:fliplr`:


.. rst-class:: procgraph:block

``fliplr``
------------------------------------------------------------
Wrapper for :py:func:`numpy.fliplr`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:flipud`:


.. rst-class:: procgraph:block

``flipud``
------------------------------------------------------------
Wrapper for :py:func:`numpy.flipud`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:gradient1d`:


.. rst-class:: procgraph:block

``gradient1d``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/gradient1d.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/gradient1d.py>`_. 


.. _`block:hstack`:


.. rst-class:: procgraph:block

``hstack``
------------------------------------------------------------
Wrapper around :py:func:`numpy.hstack`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|

- ``1``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:log`:


.. rst-class:: procgraph:block

``log``
------------------------------------------------------------
Wrapper around :py:func:`numpy.core.umath.log`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:max`:


.. rst-class:: procgraph:block

``max``
------------------------------------------------------------
Maximum over all elements.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:maximum`:


.. rst-class:: procgraph:block

``maximum``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``threshold``: |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:mean`:


.. rst-class:: procgraph:block

``mean``
------------------------------------------------------------
Compute the arithmetic mean along the specified axis. 

Returns the average of the array elements.  The average is taken over
the flattened array by default, otherwise over the specified axis.
`float64` intermediate and return values are used for integer inputs.

Parameters
----------
a : array_like
    Array containing numbers whose mean is desired. If `a` is not an
    array, a conversion is attempted.
axis : int, optional
    Axis along which the means are computed. The default is to compute
    the mean of the flattened array.
dtype : data-type, optional
    Type to use in computing the mean.  For integer inputs, the default
    is `float64`; for floating point inputs, it is the same as the
    input dtype.
out : ndarray, optional
    Alternate output array in which to place the result.  The default
    is ``None``; if provided, it must have the same shape as the
    expected output, but the type will be cast if necessary.
    See `doc.ufuncs` for details.

Returns
-------
m : ndarray, see dtype parameter above
    If `out=None`, returns a new array containing the mean values,
    otherwise a reference to the output array is returned.

See Also
--------
average : Weighted average

Notes
-----
The arithmetic mean is the sum of the elements along the axis divided
by the number of elements.

Note that for floating-point input, the mean is computed using the
same precision the input has.  Depending on the input data, this can
cause the results to be inaccurate, especially for `float32` (see
example below).  Specifying a higher-precision accumulator using the
`dtype` keyword can alleviate this issue.

Examples
--------
>>> a = np.array([[1, 2], [3, 4]])
>>> np.mean(a)
2.5
>>> np.mean(a, axis=0)
array([ 2.,  3.])
>>> np.mean(a, axis=1)
array([ 1.5,  3.5])

In single precision, `mean` can be inaccurate:

>>> a = np.zeros((2, 512*512), dtype=np.float32)
>>> a[0, :] = 1.0
>>> a[1, :] = 0.1
>>> np.mean(a)
0.546875

Computing the mean in float64 is more accurate:

>>> np.mean(a, dtype=np.float64)
0.55000000074505806


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``axis`` (default: 0): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:minimum`:


.. rst-class:: procgraph:block

``minimum``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``threshold``: |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:normalize_Linf`:


.. rst-class:: procgraph:block

``normalize_Linf``
------------------------------------------------------------
Normalize a vector such that ``|x|_inf = max(abs(x))= 1``


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:outer`:


.. rst-class:: procgraph:block

``outer``
------------------------------------------------------------
Wrapper around :py:func:`numpy.multiply.outer`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|

- ``1``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:rad2deg`:


.. rst-class:: procgraph:block

``rad2deg``
------------------------------------------------------------
Converts radians to degrees.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:select`:


.. rst-class:: procgraph:block

``select``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``every``: |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:sign`:


.. rst-class:: procgraph:block

``sign``
------------------------------------------------------------
Wrapper around :py:func:`numpy.core.umath.sign`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:smooth1d`:


.. rst-class:: procgraph:block

``smooth1d``
------------------------------------------------------------
smooth the data using a window with requested size. 

This method is based on the convolution of a scaled window with the signal.
The signal is prepared by introducing reflected copies of the signal
(with the window size) in both ends so that transient parts are minimized
in the begining and end part of the output signal.

input:
    x: the input signal
    window_len: the dimension of the smoothing window; should be an odd integer
    window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
        flat window will produce a moving average smoothing.

output:
    the smoothed signal

example:

t=linspace(-2,2,0.1)
x=sin(t)+randn(len(t))*0.1
y=smooth(x)

see also:

numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
scipy.signal.lfilter

TODO: the window parameter could be the window itself if an array instead of a string


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``window_len`` (default: 11): |towrite|

- ``window`` (default: hanning): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/smooth1d.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/smooth1d.py>`_. 


.. _`block:square`:


.. rst-class:: procgraph:block

``square``
------------------------------------------------------------
Wrapper around :py:func:`numpy.core.umath.square`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:sum`:


.. rst-class:: procgraph:block

``sum``
------------------------------------------------------------
Sum over all elements.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:take`:


.. rst-class:: procgraph:block

``take``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``indices``: |towrite|

- ``axis`` (default: 0): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`block:vstack`:


.. rst-class:: procgraph:block

``vstack``
------------------------------------------------------------
Wrapper around :py:func:`numpy.vstack`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|

- ``1``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_numpy_ops/filters.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_numpy_ops/filters.py>`_. 


.. _`module:procgraph_pil`:


.. rst-class:: procgraph:module

Package ``procgraph_pil``
============================================================



.. rst-class:: procgraph:desc

Blocks for image operations based on the PIL library

.. _`block:imread`:


.. rst-class:: procgraph:block

``imread``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_pil/imread.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_pil/imread.py>`_. 


.. _`block:resize`:


.. rst-class:: procgraph:block

``resize``
------------------------------------------------------------
|towrite|


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``width`` (default: None): |towrite|

- ``height`` (default: None): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_pil/pil_operations.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_pil/pil_operations.py>`_. 


.. _`block:text`:


.. rst-class:: procgraph:block

``text``
------------------------------------------------------------
This block provides text overlays over an image. 

You should provide a list of dictionary in the configuration variable
 ``texts``. Each dictionary in the list describes one piece of text.

An example of valid configuration is the following: ::

    text.texts = [{string: "raw image", position: [10,30], halign: left,
                  color: black, bg: white }]

The meaning of the fields is as follow:

``string``
  Text to display. See the section below about keyword expansion.

``position``
  Array of two integers giving the position of the text in the image

``color``
  Text color. It can be a keyword color or an hexadecimal string (``white`` or
  ``#ffffff``).

``bg``
  background color

``halign``
  Horizontal alignment. Choose between ``left`` (default), ``center``, ``right``.

``valign``
  Vertical alignment. Choose between ``top`` (default), ``middle``, ``center``.

``size``
  Font size in pixels

``font``
  Font family. Must be a ttf file (``Arial.ttf``)

**Expansion**: Also we expand macros in the text using ``format()``.
The available keywords are:

``frame``
  number of frames since the beginning

``time``
  seconds since the beginning of the log

``timestamp``
  absolute timestamp


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``texts``: Text specification


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``rgb``: Input image.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``rgb``: Output image with overlaid text.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_pil/text.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_pil/text.py>`_. 


.. _`module:procgraph_robotics`:


.. rst-class:: procgraph:module

Package ``procgraph_robotics``
============================================================



.. rst-class:: procgraph:desc

Some functions specific to robotics applications. 


.. rst-class:: procgraph:desc_rest


Requires: http://github.com/AndreaCensi/snp_geometry

.. _`block:laser_display`:


.. rst-class:: procgraph:block

``laser_display``
------------------------------------------------------------
Produces a plot of a range-finder scan. 

Example of configuration: ::

    display_sick.groups = [{ indices: [0,179], theta: [-1.57,+1.57],
         color: 'r', origin: [0,0,0]}]


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``width`` (default: 320): |towrite|

- ``height`` (default: 320): |towrite|

- ``max_readings`` (default: 30): |towrite|

- ``groups``: How to group and draw the readings. (see example)

- ``title`` (default: None): By default it displays the signal name. Set the empty string to disable.

- ``transparent`` (default: False): Gives transparent RGBA rather than RGB.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``readings``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``image``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_robotics/laser_display.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_robotics/laser_display.py>`_. 


.. _`block:laser_dot_display`:


.. rst-class:: procgraph:block

``laser_dot_display``
------------------------------------------------------------
Produces a plot of a range-finder scan variation (derivative). 

It is a variation of :ref:`block:laser_display`.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``width`` (default: 320): |towrite|

- ``height`` (default: 320): |towrite|

- ``groups``: How to group and draw the readings. (see example)

- ``title`` (default: None): By default it displays the signal name. Set the empty string to disable.

- ``transparent`` (default: False): Gives transparent RGBA rather than RGB.

- ``R0`` (default: 1): |towrite|

- ``amp`` (default: 0.5): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``readings_dot``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``image``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_robotics/laser_dot_display.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_robotics/laser_dot_display.py>`_. 


.. _`block:organic_scale`:


.. rst-class:: procgraph:block

``organic_scale``
------------------------------------------------------------
A (almost failed) attempt to scale a signal into [-1,1] according to the history.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``skim`` (default: 5): |towrite|

- ``skim_hist`` (default: 5): |towrite|

- ``hist`` (default: 100): |towrite|

- ``tau`` (default: 0.1): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``value``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``value_scaled``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_robotics/organic_scale.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_robotics/organic_scale.py>`_. 


.. _`block:pose2commands`:


.. rst-class:: procgraph:block

``pose2commands``
------------------------------------------------------------
Computes the velocity commands from the odometry data.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``pose``: Odometry ``[x,y,theta]``.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``commands``: Estimated commands ``[vx,vy,omega]``.

- ``vx``: |towrite|

- ``vy``: |towrite|

- ``omega``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_robotics/pose2velocity.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_robotics/pose2velocity.py>`_. 


.. _`block:pose2vel_`:


.. rst-class:: procgraph:block

``pose2vel_``
------------------------------------------------------------
Block used by :ref:`block:pose2commands`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``q12``: Last two poses.

- ``t12``: Last two timestamps.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``commands``: Estimated commands ``[vx,vy,omega]``.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_robotics/pose2velocity.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_robotics/pose2velocity.py>`_. 


.. _`block:skim`:


.. rst-class:: procgraph:block

``skim``
------------------------------------------------------------
Skims the top and bottom percentile from the data.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``percent`` (default: 5): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_robotics/misc.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_robotics/misc.py>`_. 


.. _`module:procgraph_signals`:


.. rst-class:: procgraph:module

Package ``procgraph_signals``
============================================================



.. rst-class:: procgraph:desc

Blocks performing operations with a dynamic nature. 


.. rst-class:: procgraph:desc_rest

This library contains blocks that perform operations with time.
This library is autoloaded.

.. _`block:derivative`:


.. rst-class:: procgraph:block

``derivative``
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

Implemented in `/src/procgraph_signals/derivative.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/derivative.py>`_. 


.. _`block:derivative2`:


.. rst-class:: procgraph:block

``derivative2``
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

Implemented in `/src/procgraph_signals/derivative2.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/derivative2.py>`_. 


.. _`block:extract`:


.. rst-class:: procgraph:block

``extract``
------------------------------------------------------------
This block extracts some of the components of a vector.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``index``: |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``vector``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``part``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/extract.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/extract.py>`_. 


.. _`block:forward_difference`:


.. rst-class:: procgraph:block

``forward_difference``
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

Implemented in `/src/procgraph_signals/derivative.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/derivative.py>`_. 


.. _`block:fps_data_limit`:


.. rst-class:: procgraph:block

``fps_data_limit``
------------------------------------------------------------
This block limits the output update to a certain framerate.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``fps``: Maximum framerate.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signals to decimate. (variable number: n >= 1)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Decimated signals. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/fps_data_limit.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/fps_data_limit.py>`_. 


.. _`block:fps_limit`:


.. rst-class:: procgraph:block

``fps_limit``
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

Arbitrary signals. (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arbitrary signals with limited framerate. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/fps_limit.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/fps_limit.py>`_. 


.. _`block:fps_print`:


.. rst-class:: procgraph:block

``fps_print``
------------------------------------------------------------
Prints the fps count for the input signals.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

|towrite| (variable number: n >= 1)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/fps_print.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/fps_print.py>`_. 


.. _`block:history`:


.. rst-class:: procgraph:block

``history``
------------------------------------------------------------
This block collects the history of a quantity, and outputs two signals ``x`` and ``t``. See also :ref:`block:historyt` and :ref:`block:last_n_samples`.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``interval`` (default: 10): Length of the interval to record.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``values``: Any signal.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Sequence of values.

- ``t``: Sequence of timestamps.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/history.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/history.py>`_. 


.. _`block:historyt`:


.. rst-class:: procgraph:block

``historyt``
------------------------------------------------------------
This block collects the signals samples of a signals, and outputs *one* signal containing a tuple  ``(t,x)``. See also :ref:`block:last_n_samples` and :ref:`block:history`. 

If ``natural`` is true, it uses the time from the beginning of the log.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``interval`` (default: 10): Length of interval (seconds).

- ``natural`` (default: True): If true, set 0 as the log beginning.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Any signal.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``history``: Tuple ``(t,x)`` containing two arrays.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/historyt.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/historyt.py>`_. 


.. _`block:join`:


.. rst-class:: procgraph:block

``join``
------------------------------------------------------------
This block joins multiple signals into one.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signals to be joined together. (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``joined``: Joined signals.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/join.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/join.py>`_. 


.. _`block:last_n_samples`:


.. rst-class:: procgraph:block

``last_n_samples``
------------------------------------------------------------
This block collects the last N samples of a signals, and outputs two signals ``x`` and ``t``. See also :ref:`block:historyt` and :ref:`block:history`.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``n``: Number of samples to retain.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Any data


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Sequence of values.

- ``t``: Sequence of timestamps.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/last_n_samples.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/last_n_samples.py>`_. 


.. _`block:low_pass`:


.. rst-class:: procgraph:block

``low_pass``
------------------------------------------------------------
Implements simple low-pass filtering. 

Formula used: ::

    y[k] = alpha * u[k] + (1-alpha) * y[k-1]


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``alpha``: |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``value``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``lowpass``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/low_pass.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/low_pass.py>`_. 


.. _`block:make_tuple`:


.. rst-class:: procgraph:block

``make_tuple``
------------------------------------------------------------
Creates a tuple out of the input signals values. 

Often used for plotting two signals as (x,y); see :ref:`block:plot`.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Signals to unite in a tuple. (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``tuple``: Tuple containing signals.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/make_tuple.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/make_tuple.py>`_. 


.. _`block:sieve`:


.. rst-class:: procgraph:block

``sieve``
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

Implemented in `/src/procgraph_signals/sieve.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/sieve.py>`_. 


.. _`block:slice`:


.. rst-class:: procgraph:block

``slice``
------------------------------------------------------------
Slices a signal by extracting from index ``start`` to index ``end`` (INCLUSIVE).


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``start``: |towrite|

- ``end``: |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/extract.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/extract.py>`_. 


.. _`block:sync`:


.. rst-class:: procgraph:block

``sync``
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

Signals to synchronize. The first is the master. (variable number: n >= 2)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Synchronized signals. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/sync.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/sync.py>`_. 


.. _`block:two_step_difference`:


.. rst-class:: procgraph:block

``two_step_difference``
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

Implemented in `/src/procgraph_signals/derivative2.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/derivative2.py>`_. 


.. _`block:wait`:


.. rst-class:: procgraph:block

``wait``
------------------------------------------------------------
This block waits a given number of updates before transmitting the output.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``n``: Number of updates to wait at the beginning.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arbitrary signals. (variable number)


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Arbitrary signals, minus the first ``n`` updates. (variable number)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_signals/wait.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_signals/wait.py>`_. 


.. _`module:procgraph_statistics`:


.. rst-class:: procgraph:module

Package ``procgraph_statistics``
============================================================



.. rst-class:: procgraph:desc

Blocks for common statistical operations.

.. _`block:cov2corr`:


.. rst-class:: procgraph:block

``cov2corr``
------------------------------------------------------------
Compute the correlation matrix from the covariance matrix. If zero_diagonal = True, the diagonal is set to 0 instead of 1.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``zero_diagonal`` (default: True): |towrite|


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``0``: |towrite|


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_statistics/cov2corr.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_statistics/cov2corr.py>`_. 


.. _`block:covariance`:


.. rst-class:: procgraph:block

``covariance``
------------------------------------------------------------
Computes the covariance matrix of the input


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``wait`` (default: 10): Number of sample to have reliable expectation.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Unidimensional numpy array.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``cov_x``: Square matrix representing sample covariance.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_statistics/covariance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_statistics/covariance.py>`_. 


.. _`block:expectation`:


.. rst-class:: procgraph:block

``expectation``
------------------------------------------------------------
Computes the sample expectation of a signal.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Any numpy array.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``Ex``: Expectation of input.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_statistics/expectation.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_statistics/expectation.py>`_. 


.. _`block:normalize`:


.. rst-class:: procgraph:block

``normalize``
------------------------------------------------------------
Removes the mean from a signal.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``wait`` (default: 10): Number of sample to have reliable expectation.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Unidimensional numpy array.


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x_n``: Signal without the mean.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_statistics/covariance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_statistics/covariance.py>`_. 


.. _`block:soft_variance`:


.. rst-class:: procgraph:block

``soft_variance``
------------------------------------------------------------
Computes the element-wise "soft" variance (expectation of error absolute value)


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``wait`` (default: 100): Number of samples to wait before declaring the expectation valid.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Any numpy array


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``var_x``: Soft variance of ``x``.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_statistics/variance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_statistics/variance.py>`_. 


.. _`block:variance`:


.. rst-class:: procgraph:block

``variance``
------------------------------------------------------------
Computes the element-wise variance.


.. rst-class:: procgraph:config

Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``wait`` (default: 100): Number of samples to wait before declaring the expectation valid.


.. rst-class:: procgraph:input

Input
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``x``: Any numpy array


.. rst-class:: procgraph:output

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``var_x``: Variance of ``x``.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_statistics/variance.py <https://github.com/AndreaCensi/procgraph/blob/master//src/procgraph_statistics/variance.py>`_. 


