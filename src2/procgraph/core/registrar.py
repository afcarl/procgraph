
name2class = {}

def register_block_class(name, block_class):
    global name2class
    name2class[name] = block_class
    
    
def get_block_class(operation):
    global name2class
    if not operation in name2class:
        raise ValueError('Could not find block type "%s".' % operation)
    
    return name2class[operation]
