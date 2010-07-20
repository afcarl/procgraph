from procgraph.core.exceptions import SemanticError

name2class = {}

def register_block_class(name, block_class):
    global name2class
    if name in name2class:
        raise ValueError('Type %s already registered.' % name)
    
    name2class[name] = block_class
    
 
def exists_block_class(name):
    global name2class
    return name in name2class
    
def get_block_class(operation):
    global name2class
    if not operation in name2class:
        raise SemanticError('Could not find block type "%s".' % operation)
    
    return name2class[operation]


