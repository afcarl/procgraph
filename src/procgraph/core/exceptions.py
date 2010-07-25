
class PGException(Exception):
    pass

class BlockWriterError(PGException):
    ''' An error by who wrote the block (e.g.: did not define signals).''' 
    pass

class ModelWriterError(PGException):
    ''' An error by who wrote the model, can be either Syntax or Semantic '''
    pass

class SemanticError(ModelWriterError):
    ''' A semantic error by who wrote the model spec.'''
    def __init__(self, error, element=None):
        Exception.__init__(self,error)
        self.element = element

class SyntaxError(ModelWriterError):
    ''' A syntactic error by who wrote the model spec.'''
    pass

class ModelExecutionError(PGException):
    ''' Runtime errors, including misuse by the user '''
    pass