
class PGException(Exception):
    pass

class BlockWriterError(PGException):
    ''' An error by who wrote the block ''' 
    pass

class UserError(PGException):
    ''' A semantic error by who wrote the model.'''
    pass

class SyntaxError(PGException):
    ''' A syntactic error by who wrote the model.'''
    pass