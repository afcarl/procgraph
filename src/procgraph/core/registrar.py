
class Library:
    
    def __init__(self, parent=None):
        self.parent = parent
        
        self.name2block = {}
        
    def exists(self, block_type):
        if block_type in self.name2block:
            return True
        else:
            if self.parent:
                return self.parent.exists(block_type)
            else:
                return False
        
    def register(self, block_type, generator):
        if  self.exists(block_type):
            raise ValueError('Type %s already registered.' % block_type)
    
        self.name2block[block_type] = generator
    
    def instance(self, block_type, name, config, parent_library=None, where=None):
        # we give the children a reference to the library object
        # that was called first, not its parent
        if parent_library is None:
            parent_library = self

        if not self.exists(block_type):
            raise ValueError('Asked to instance "%s" which does not exist' %
                             block_type)
        if block_type in self.name2block:
            generator = self.name2block[block_type]
            block = generator(name=name, config=config, library=parent_library)
        else: 
            assert self.parent
            block = self.parent.instance(block_type,name,config,
                                        parent_library=parent_library)
        block.where = where
        return block
    
    
    def get_known_blocks(self):
        blocks = self.name2block.keys()
        if self.parent:
            blocks.extend(self.parent.get_known_blocks())
        return blocks
        
        
default_library = Library()
 
        


