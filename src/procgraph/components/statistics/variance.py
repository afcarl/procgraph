from procgraph.core.model_loader import add_models_to_library
from procgraph.core.registrar import default_library


# Computes the variance
model_spec = """
--- model variance 
|input name=x| --> |expectation| --> Ex

   x, Ex --> |-| --> error 
   
   error -> |square| --> |expectation| --> |output name=var_x|
    
"""
add_models_to_library(default_library, model_spec)

# Computes soft variance
model_spec = """
--- model soft_variance 
|input name=x| --> |expectation| --> Ex

   x, Ex --> |-| --> error 
   
   error -> |abs| --> |expectation| --> |output name=var_x|
    
"""
add_models_to_library(default_library, model_spec)

 
#
#
#from numpy import zeros 
#from pybv.utils import weighted_average, outer
#
#class SenselCovariance:
#
#    def __init__(self, config):
#        n = config.num_sensels
#        self.cov_sensels = zeros((n, n))
#        self.mean_sensels = zeros((n,))
#        self.num_samples = 0
#        
#    def process_data(self, data):
#        y = data.sensels
#        self.mean_sensels = weighted_average(self.mean_sensels, self.num_samples, y)
#        yn = y - self.mean_sensels
#        T = outer(yn, yn)
#        self.cov_sensels = weighted_average(self.cov_sensels, self.num_samples, T) 
#        self.num_samples += 1

