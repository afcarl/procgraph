
class Library:
    
    def __init__(self, parent=None):
        self.parent = parent
        
        self.name2block = {}
        
    def exists(self, block_type):
        if block_type in self.name2block:
            return True
        else:
            if self.parent is not None:
                return self.parent.exists(block_type)
            else:
                return False
        
    def register(self, block_type, generator):
        if  self.exists(block_type):
            raise ValueError('Type %s already registered.' % block_type)
    
        self.name2block[block_type] = generator
    
    def instance(self, block_type, name, config, library=None):
        if library is None:
            library = self
        #try:
        generator = self.get_generator_for_block_type(block_type)
        #except Exception as e:
        #    raise ValueError('Asked to instance "%s" which does not exist' % 
        #                     block_type)
       # try:
        block = generator(name=name, config=config, library=library)
        return block
        #except TypeError as e:
        #    raise Exception('Could not instance a block of type "%s": %s' % 
        #                             (block_type, e))
            
                
    
    def get_generator_for_block_type(self, block_type):
        ''' Returns the generator object for the block type.
        
            A generator can instance using:
            
                generator(name, config, library)
                
            and it can provide (before instancing) the properties:
            
                generator.config
                generator.input
                generator.output
        '''
                
        if not self.exists(block_type):
            raise ValueError('Asked for generator for "%s" which does not exist.' % 
                             block_type)
            
        if block_type in self.name2block:
            generator = self.name2block[block_type]
            return generator
        else: 
            assert self.parent
            return self.parent.get_generator_for_block_type(block_type)
    
    def get_known_blocks(self):
        blocks = self.name2block.keys()
        if self.parent:
            blocks.extend(self.parent.get_known_blocks())
        return blocks
        
        
default_library = Library()
 
        


