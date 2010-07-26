'''
Created on 25/lug/2010

@author: andrea
'''
from procgraph.core.block import Block
from procgraph.core.registrar import default_library
from procgraph.core.model_loader import add_models_to_library


class Expectation(Block):
        
    def init(self):
        self.define_input_signals(['x'])
        self.define_output_signals(['Ex'])
        self.set_state('Ex', None)
        self.set_state('num_samples', 0)
        
    def update(self):
        x = self.get_input('x')
        num_samples = self.get_state('num_samples')
        Ex = self.get_state('Ex')
        
        if num_samples == 0:
            Ex = x.copy()
        else:
            Ex = (Ex * num_samples + x) / float(num_samples+1);
        
        self.set_state('Ex', Ex)
        self.set_state('num_samples', num_samples + 1)
        
        self.set_output('Ex', Ex)
            
    
default_library.register('expectation', Expectation)


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

 


from numpy import zeros 
from pybv.utils import weighted_average, outer

class SenselCovariance:

    def __init__(self, config):
        n = config.num_sensels
        self.cov_sensels = zeros((n, n))
        self.mean_sensels = zeros((n,))
        self.num_samples = 0
        
    def process_data(self, data):
        y = data.sensels
        self.mean_sensels = weighted_average(self.mean_sensels, self.num_samples, y)
        yn = y - self.mean_sensels
        T = outer(yn, yn)
        self.cov_sensels = weighted_average(self.cov_sensels, self.num_samples, T) 
        self.num_samples += 1

