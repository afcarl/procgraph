from procgraph.core.model import Model
from procgraph.components.rawseeds import *
import sys

# First we define the computational structure

model_desc = """
   |logreader:RawseedsRF| -> y -> |expectation| -> y_mean
   
   #y, y_mean -> |generic in=2| 
   
   
   y_mean -> |output name=mean|
    
"""

# The model needs parameters, for example the location of the log file.
# We pass these to the method from_string as an hash.


file = "${PBENV_DATA}/Bicocca_2009-02-25a-SICK_FRONT.csv"
model = Model.from_string(model_desc, {'logreader.file': file})

model.summary()
# We run the model step by step
while model.has_more():
    model.update()
    sys.stderr.write('.')
    #print model.get_output('mean')
    
    # print model.get_output('y')