from procgraph.components.basic import register_model_spec

register_model_spec("""
--- model covariance 
# number of sample to have reliable expectation
wait=10

|input name=x| --> x --> |expectation| --> |wait n=$wait| --> Ex

   x, Ex --> |sync| --> |-| --> x_normalized 
   
   x_normalized, x_normalized --> |outer| -->  |expectation| --> covariance 
   
   covariance --> |output name=cov_x|
    
""")

register_model_spec("""
--- model normalize 
# number of sample to have reliable expectation
wait=10

|input name=x| --> x --> |expectation| --> |wait n=$wait| --> Ex

   x, Ex --> |sync| --> |-| --> x_normalized --> |output name=x_n|
    
""")
