from procgraph.core.model_loader import add_models_to_library
from procgraph.core.registrar import default_library

model_covariance = """
--- model covariance 
# number of sample to have reliable expectation
wait=10

|input name=x| --> x --> |expectation| --> |wait n=$wait| --> Ex

   x, Ex --> |sync| --> |-| --> x_normalized 
   
   x_normalized, x_normalized --> |outer| -->  |expectation| --> covariance 
   
   covariance --> |output name=cov_x|
    
"""
add_models_to_library(default_library, model_covariance)


model_normalize = """
--- model normalize 
# number of sample to have reliable expectation
wait=10

|input name=x| --> x --> |expectation| --> |wait n=$wait| --> Ex

   x, Ex --> |sync| --> |-| --> x_normalized --> |output name=x_n|
    
"""
add_models_to_library(default_library, model_normalize)
