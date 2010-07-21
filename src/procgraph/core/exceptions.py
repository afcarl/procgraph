
class PGException(Exception):
    pass

class BlockWriterError(PGException):
    ''' An error by who wrote the block ''' 
    pass

class ModelWriterError(PGException):
    ''' An error by who wrote the model, can be either Syntax or Semantic '''
    pass

class SemanticError(ModelWriterError):
    ''' A semantic error by who wrote the model.'''
    pass

class SyntaxError(ModelWriterError):
    ''' A syntactic error by who wrote the model.'''
    pass

class ModelExecutionError(PGException):
    ''' Runtime errors, including misuse by the user '''
    pass