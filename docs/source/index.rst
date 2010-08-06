.. procgraph documentation master file, created by
   sphinx-quickstart on Tue Jul 27 15:21:25 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to procgraph's documentation!
=====================================

.. container:: col1

	**Getting started**

	* :ref:`install`
	* :ref:`why`
	* :ref:`limitations`
	

	**Tutorial**
	
	* :ref:`tutorial0`

.. container:: col2

	**Advanced usage**

	* :ref:`creating_new_blocks` 
	



.. block:: gray2rgb
  
  Block description description

 .. input:: An rgb imager

 .. config:: An rgb image

 .. output:: An rgb image

Libraries documentation
-----------------------

**Basic operations**

* :ref:`library:numpy_ops`
* :ref:`library:statistics`:
  :ref:`block:expectation`,
  :ref:`block:covariance`,
  :ref:`block:variance`,
  :ref:`block:cov2corr`.


**Operations with time**

* :ref:`library:dynamic`:
  :ref:`block:wait`,
  :ref:`block:sieve`,
  :ref:`block:derivative`,
  :ref:`block:history`,
  :ref:`block:historyn`.
 
**Images and video**

* :ref:`library:images`: 
  :ref:`block:compose`,
  :ref:`block:grid`,
  :ref:`block:rgb2gray`,
  :ref:`block:gray2rgb`,
  :ref:`block:posneg`,
  :ref:`block:scale`.

* :ref:`library:pil`:
  :ref:`block:resize`,
  :ref:`block:text`.

* :ref:`library:cv`:
  :ref:`block:gradient`,  
  :ref:`block:smooth`.

* :ref:`library:video`:
  :ref:`block:mencoder`,  
  :ref:`block:mplayer`.

**Plotting**

* :ref:`library:pylab` \*

**GUI and user interaction**

* :ref:`library:gui`

**Robotics**

* :ref:`library:robotics`:
  :ref:`block:pose2velocity`.

* :ref:`library:rawseeds`:
  :ref:`block:RawseedsCam`,
  :ref:`block:RawseedsHokuyo`,
  :ref:`block:RawseedsOdo`,
  :ref:`block:RawseedsRF`.


Indices and tables
==================

.. toctree::
   :maxdepth: 2

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

