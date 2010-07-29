from numpy import multiply, sqrt
from procgraph.core.registrar import default_library
from procgraph.components.basic import make_generic
outer = multiply.outer

def cov2corr(covariance, zero_diagonal=True):
    ''' Compute the correlation matrix from the covariance matrix.
    If zero_diagonal = True, the diagonal is set to 0 instead of 1. '''
    # TODO: add checks
    sigma = sqrt(covariance.diagonal())
    M = outer(sigma, sigma)
    correlation = covariance / M
    
    if zero_diagonal:
        for i in range(covariance.shape[0]):
            correlation[i,i] = 0
    
    return correlation

default_library.register('cov2corr', make_generic(1,1,cov2corr,zero_diagonal=True)) 
