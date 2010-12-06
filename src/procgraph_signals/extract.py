from procgraph import Block, COMPULSORY, register_simple_block


# Make it generic?
class Extract(Block):
    ''' 
    This block extracts some of the components of a vector.
    
    '''
    Block.alias('extract')
    Block.input('vector', 'Any numpy array')
    Block.output('part', 'The part extracted')
    Block.config('index', 'Index (or indices) to extract.') 

    def update(self):
        index = self.config.index
        vector = self.input.vector
        
        part = vector[index]
        
        self.output.part = part
         
         
def slice(signal, start=COMPULSORY, end=COMPULSORY):
    ''' Slices a signal by extracting from index ``start`` to index ``end``
        (INCLUSIVE).
        
        :param signal: Any 1d numpy array
        :param start:  Slice start.
        :param end:    Slice end (inclusive).
        
        :return: sliced: The sliced signal.
    '''
    return signal[start:(end + 1)]

    
register_simple_block(slice)

    
