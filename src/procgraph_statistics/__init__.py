''' 
    Blocks for common statistical operations.

'''


procgraph_info = {
    # List of python packages 
    'requires': ['astatsa']
}


from . import expectation
from . import variance
from . import covariance
from . import cov2corr
from . import minimum
from . import covariance2
