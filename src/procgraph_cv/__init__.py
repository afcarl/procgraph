''' Operations using the OpenCV library. 

**Packages dependencies**

* ``opencv`` (or ``cv``)


'''

procgraph_info = {
    # List of python packages 
    'requires':  [ ('cv', ('cv', 'opencv')) ]
} 


from procgraph import import_magic

# If cv is installed, it will be a reference to it, otherwise a 
# shadow object which will throw when you actually try to use it.
cv = import_magic(__name__, 'cv')


import opencv_utils 
