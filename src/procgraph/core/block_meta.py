from collections import namedtuple
from procgraph.core.exceptions import BlockWriterError, ModelWriterError
import sys

FIXED = 'fixed-signal'
VARIABLE = 'variable-signal'

#BlockConfig = namedtuple('BlockConfig', 'variable has_default default desc desc_rest where')
#BlockInput = namedtuple('BlockInput', 'type name min max desc desc_rest where')
#BlockOutput = namedtuple('BlockOutput', 'type name  desc desc_rest where')

class BlockConfig:
    def __init__(self, variable, has_default, default, desc, desc_rest, where):
        self.variable = variable
        self.has_default = has_default
        self.default = default
        self.desc = desc
        self.desc_rest = desc_rest
        self.where = where
        
class BlockInput:
    def __init__(self, type, name, min, max, desc, desc_rest, where):
        self.type = type
        self.name = name
        self.min = min
        self.max = max
        self.desc = desc
        self.desc_rest = desc_rest
        self.where = where
        
class BlockOutput:
    def __init__(self, type, name, desc, desc_rest, where):
        self.type = type
        self.name = name
        self.desc = desc
        self.desc_rest = desc_rest
        self.where = where

def block_config(name, description=None, default='not-given'):
    desc, desc_rest = split_docstring(description)
    has_default = default != 'not-given'
    if filter(lambda x: x.variable == name, BlockMeta.tmp_config):
        raise BlockWriterError('Already described config variable "%s".' % name)
    BlockMeta.tmp_config.append(BlockConfig(name, has_default, default, desc, desc_rest, None))

def block_input(name, description=None):
    desc, desc_rest = split_docstring(description)
    if filter(lambda x: x.name == name, BlockMeta.tmp_input):
        raise BlockWriterError('Already described input variable "%s".' % name)
    if BlockMeta.tmp_input and BlockMeta.tmp_input[-1].type == VARIABLE:
        raise BlockWriterError('Cannot mix variable and fixed input.')
    BlockMeta.tmp_input.append(BlockInput(FIXED, name, None, None, desc, desc_rest, None))

def block_input_is_variable(description=None, min=None, max=None):
    desc, desc_rest = split_docstring(description)
    if BlockMeta.tmp_input:
        raise BlockWriterError('Cannot mix variable and fixed input'
                               ' or variable with variable.')
    BlockMeta.tmp_input.append(BlockInput(VARIABLE, None, min, max, desc, desc_rest, None))
    
def block_output(name, description=None):
    desc, desc_rest = split_docstring(description)
    if filter(lambda x: x.name == name, BlockMeta.tmp_output):
        raise BlockWriterError('Already described output variable "%s".' % name)
    if BlockMeta.tmp_output and BlockMeta.tmp_output[-1].type == VARIABLE:
        raise BlockWriterError('Cannot mix variable and fixed output.')
    
    BlockMeta.tmp_output.append(BlockOutput(FIXED, name, desc, desc_rest, None))
    
def block_output_is_variable(description=None, suffix=None):
    desc, desc_rest = split_docstring(description)
    if BlockMeta.tmp_output:
        raise BlockWriterError('Cannot mix variable and fixed output'
                               ' or variable with variable.')
    BlockMeta.tmp_output.append(BlockOutput(VARIABLE, suffix, desc, desc_rest, None))
    
class BlockMeta(type):
    tmp_config = []
    tmp_input = []
    tmp_output = [] 
    
    def __init__(cls, clsname, bases, clsdict): 
        setattr(cls, 'config', BlockMeta.tmp_config)
        setattr(cls, 'output', BlockMeta.tmp_output)
        setattr(cls, 'input', BlockMeta.tmp_input)
        BlockMeta.tmp_config = []
        BlockMeta.tmp_output = []
        BlockMeta.tmp_input = []

        has_variable_input = filter(lambda x: x.type == VARIABLE, BlockMeta.tmp_input)
        has_variable_output = filter(lambda x: x.type == VARIABLE, BlockMeta.tmp_output)
        
        if has_variable_output and not has_variable_input:
            raise ModelWriterError('Cannot have variable output without variable input.')


def trim(docstring):
    if not docstring:
        return ''
    lines = docstring.expandtabs().splitlines()

    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxint
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))

    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxint:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())

    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    
    result = '\n'.join(trimmed)
    
    #print 'input: """%s"""' % docstring
    #print 'result: """%s"""' % result
    return result

def split_docstring(s):
    ''' Splits a docstring in a tuple (first, rest). '''
    if s is None:
        return None, None
    s = trim(s)
    all_lines = s.split('\n') 
    valid_lines = filter(None, map(str.strip, all_lines))
    if valid_lines:
        for i in range(len(all_lines)):
            if all_lines[i]: # found first
                # join all non-empty lines with the first
                j = i
                while j < len(all_lines) - 1 and all_lines[j].strip():
                    j += 1
                first = ' '.join(all_lines[i:(j + 1)])
                rest = '\n'.join(all_lines[j + 1:])
                return first, rest
        assert False
    else:
        return None, None
    
