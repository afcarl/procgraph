from pyparsing import lineno, col

class Location:
    def __init__(self, string, character):
        self.string = string
        self.character = character
        self.line = lineno(character,string)
        self.col =  col(character, string)
        
    def __str__(self):
        return "{line %d, col %d}" % (self.line, self.col)


class ParsedSignalList:
    def __init__(self, l):
        self.signals = l
        
    def __repr__(self):
        return 'Signals%s' % self.signals
    
    @staticmethod
    def from_tokens (original_string,location,tokens):
        return ParsedSignalList(list(tokens))
    
class ImportStatement:
    def __init__(self, package, location):
        self.package = package
        self.location = location
    
    def __repr__(self):
        return 'import(%s)' % self.package
    
    @staticmethod
    def from_tokens(original_string,location,tokens):
        package = "".join(tokens.asList())
        return ImportStatement(package, location)
    

class ParsedSignal:
    def __init__(self, name, block_name, local_input, local_output, location=None):
        self.name = name
        self.block_name = block_name
        self.local_input = local_input
        self.local_output = local_output
        self.location = location
        
    def __repr__(self):
        s = 'Signal('
        if self.local_input is not None:
            s += "[%s]" % self.local_input
        if self.block_name is not None:
            s += "%s." % self.block_name
        s += str(self.name)
        if self.local_output is not None:
            s += "[%s]" % self.local_output
        s+=')'
        if self.location:
            s += '@%s' % self.location
        return s
    
    @staticmethod
    def from_tokens (original_string,location,tokens):
        name = tokens.get('name')
        block_name = tokens.get('block_name', None)
        local_input = tokens.get('local_input', None)
        local_output = tokens.get('local_output', None)
        where = Location(original_string,location)
        return ParsedSignal(name, block_name, local_input, local_output, where)

class ParsedBlock:
    def __init__(self, name, operation, config):
        self.name = name
        self.operation = operation
        self.config = config
        
    def __repr__(self):
        return 'Block(op=%s,name=%s,config=%s)' % (self.operation,self.name,self.config)

    @staticmethod
    def from_tokens(original_string,location,tokens):
        blocktype = tokens['blocktype'] 
        config = tokens.get('config', {})
        name = tokens.get('name', None)
        return ParsedBlock(name, blocktype, config)

class ParsedAssignment:
    def __init__(self, key,value):
        self.key = key
        self.value = value
        
    def __repr__(self):
        return 'Assignment(%s=%s)' % (self.key, self.value)

    @staticmethod
    def from_tokens(original_string,location,tokens):
        return ParsedAssignment(tokens['key'], tokens['value'])
          
      
class Connection:
    def __init__(self, elements):
        self.elements = elements
    def __repr__(self):
        return 'Connection(%s)' % self.elements
    @staticmethod
    def from_tokens(original_string, location, tokens):
        return Connection(tokens)

class VariableReference:
    def __init__(self, variable):
        self.variable = variable
    def __repr__(self):
        return "${%s}" % self.variable
    @staticmethod
    def from_tokens(original_string, location, tokens):
        return VariableReference(tokens['variable'])

class ParsedModel:
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements

    def __repr__(self):
        return 'Model:%s(%s)' % (self.name, self.elements)
    
        
    @staticmethod
    def from_named_model(original_string, location, tokens):
        name = tokens['model_name']
        elements = list(tokens['content'])
        return ParsedModel(name, elements)
    
    @staticmethod
    def from_anonymous_model(original_string, location, tokens):
        elements = list(tokens)
        return ParsedModel(name=None, elements=elements)
    