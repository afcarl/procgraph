from procgraph.components.basic import register_model_spec

register_model_spec("""
--- model variance 
''' Computes the variance '''

|input name=x| --> |expectation| --> Ex

   x, Ex --> |-| --> error 
   
   error -> |square| --> |expectation| --> |output name=var_x|
    
""")

register_model_spec("""
--- model soft_variance 
''' Computes soft variance (expectation of error absolute value) '''
|input name=x| --> |expectation| --> Ex

   x, Ex --> |-| --> error 
   
   error -> |abs| --> |expectation| --> |output name=var_x|
    
""") 
