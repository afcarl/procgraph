
class PGException(Exception):
    pass

class BlockWriterError(PGException):
    ''' An error by who wrote the block (e.g.: did not define signals).''' 
    pass

class ModelWriterError(PGException):
    ''' An error by who wrote the model, can be either Syntax or Semantic '''
    def __init__(self, error, block=None):
        Exception.__init__(self, error + ' (block %s)' % block)
        self.block = block


class SemanticError(ModelWriterError):
    ''' A semantic error by who wrote the model spec.'''
    def __init__(self, error, element=None):
        Exception.__init__(self, error)
        self.element = element

class PGSyntaxError(ModelWriterError):
    ''' A syntactic error by who wrote the model spec.'''
    def __init__(self, error, where=None):
        Exception.__init__(self, error)
        self.where = where
        
    def __str__(self):
        return Exception.__str__(self) + '\n' + self.where.__str__()

class ModelExecutionError(PGException):
    ''' Runtime errors, including misuse by the user '''
    def __init__(self, error, block):
        Exception.__init__(self, error)
        self.block = block
    def __str__(self):
        return Exception.__str__(self) + '\n' + self.block.where.__str__()

class BadInput(ModelExecutionError):
    def __init__(self, error, block, input_signal):
        ModelExecutionError.__init__(self, error, block)
        self.input_signal = input_signal
    
    
    
    
