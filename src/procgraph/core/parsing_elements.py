import sys
from pyparsing import lineno, col

class Where:
    def __init__(self, filename, string, character=None, line=None, column=None):
        self.filename = filename
        self.string = string
        if character is None:
            assert line is not None and column is not None
            self.line = line
            self.col = column
            self.character = None
        else:
            assert line is None and column is None
            self.character = character
            self.line = lineno(character, string)
            self.col = col(character, string)

    def __str__(self):
        s = ''
        s += ('In file %s:\n' % self.filename)
        context = 3;
        lines = self.string.split('\n')
        start = max(0, self.line - context)
        pattern = 'line %2d >'
        for i in range(start, self.line):
            s += ("%s%s\n" % (pattern % (i + 1), lines[i]))
            
        fill = len(pattern % (i + 1))
        space = ' ' * fill + ' ' * (self.col - 1) 
        s += (space + '^\n')
        s += (space + '|\n')
        s += (space + 'here\n')
        return s
        
    def print_where(self, s=sys.stdout):
        s.write('\n\n')
        prefix = '    '
        write = lambda x: s.write(prefix + x)
        write('In file %s:\n' % self.filename)
        context = 3;
        lines = self.string.split('\n')
        start = max(0, self.line - context)
        pattern = 'line %2d >'
        for i in range(start, self.line):
            write("%s%s\n" % (pattern % (i + 1), lines[i]))
            
        fill = len(pattern % (i + 1))
        space = ' ' * fill + ' ' * (self.col - 1) 
        write(space + '^\n')
        write(space + '|\n')
        write(space + 'here\n')
        
        
    #def __str__(self):
    #    return "{filename: %s, line %d, col %d}" % (self.filename, self.line, self.col)


class ParsedElement:
    def __init__(self):
        self.where = None
        

class ParsedSignalList(ParsedElement):
    def __init__(self, signals):
        ParsedElement.__init__(self)
        self.signals = signals
        
    def __repr__(self):
        return 'Signals%s' % self.signals
    
    @staticmethod
    def from_tokens(tokens):
        return ParsedSignalList(list(tokens))
    
    
class ImportStatement(ParsedElement):
    def __init__(self, package):
        ParsedElement.__init__(self)
        self.package = package
    
    def __repr__(self):
        return 'import(%s)' % self.package
    
    @staticmethod
    def from_tokens(tokens):
        package = "".join(tokens.asList())
        return ImportStatement(package)
    

class LoadStatement(ParsedElement):
    def __init__(self, what, where_from, format):
        ParsedElement.__init__(self)
        self.what = what
        self.where_from = where_from
        self.format = format 
    
    def __repr__(self):
        return 'load(%s from %s as %s)' % (self.what, self.where_from, self.format)
    
    @staticmethod
    def from_tokens(tokens):
        what = tokens['what']
        where_from = tokens['where']
        if 'format' in tokens:
            format = tokens['format']
        else:
            format = None
        return LoadStatement(what, where_from, format)

class SaveStatement(ParsedElement):
    def __init__(self, what, where_to, format):
        ParsedElement.__init__(self)
        self.what = what
        self.where_to = where_to
        self.format = format 
    
    def __repr__(self):
        return 'save(%s to %s as %s)' % (self.what, self.where_to, self.format)
    
    @staticmethod
    def from_tokens(tokens):
        what = tokens['what']
        where_to = tokens['where']
        if 'format' in tokens:
            format = tokens['format']
        else:
            format = None
        return SaveStatement(what, where_to, format)

class ParsedSignal(ParsedElement):
    def __init__(self, name, block_name, local_input, local_output):
        ParsedElement.__init__(self)
        self.name = name
        self.block_name = block_name
        self.local_input = local_input
        self.local_output = local_output
        
    def __repr__(self):
        s = 'Signal('
        if self.local_input is not None:
            s += "[%s]" % self.local_input
        if self.block_name is not None:
            s += "%s." % self.block_name
        s += str(self.name)
        if self.local_output is not None:
            s += "[%s]" % self.local_output
        s += ')'
        return s
    
    @staticmethod
    def from_tokens(tokens):
        name = tokens.get('name')
        block_name = tokens.get('block_name', None)
        local_input = tokens.get('local_input', None)
        local_output = tokens.get('local_output', None)
        return ParsedSignal(name, block_name, local_input, local_output)


class ParsedBlock(ParsedElement):
    def __init__(self, name, operation, config):
        ParsedElement.__init__(self)
        self.name = name
        self.operation = operation
        self.config = config
        
    def __repr__(self):
        return 'Block(op=%s,name=%s,config=%s)' % (self.operation, self.name, self.config)

    @staticmethod
    def from_tokens(tokens):
        blocktype = tokens['blocktype'] 
        config = tokens.get('config', {})
        name = tokens.get('name', None)
        return ParsedBlock(name, blocktype, config)


class ParsedAssignment(ParsedElement):
    def __init__(self, key, value):
        ParsedElement.__init__(self)

        self.key = key
        self.value = value
        
    def __repr__(self):
        return 'Assignment(%s=%s)' % (self.key, self.value)

    @staticmethod
    def from_tokens(tokens):
        return ParsedAssignment(tokens['key'], tokens['value'])
          
      
class Connection(ParsedElement):
    def __init__(self, elements):
        ParsedElement.__init__(self)
        self.elements = elements
    
    def __repr__(self):
        return 'Connection(%s)' % self.elements

    @staticmethod
    def from_tokens(tokens):
        return Connection(tokens)

class VariableReference(ParsedElement):
    def __init__(self, variable):
        ParsedElement.__init__(self)
        self.variable = variable
        
    def __repr__(self):
        return "ref:%s" % self.variable
    
    @staticmethod
    def from_tokens(tokens):
        return VariableReference(tokens['variable'])

class ParsedModel(ParsedElement):
    def __init__(self, name, elements):
        ParsedElement.__init__(self)
        self.name = name
        self.elements = elements
        
    def __repr__(self):
        return 'Model:%s(%s)' % (self.name, self.elements)
        
    @staticmethod
    def from_named_model(tokens):
        name = tokens['model_name']
        elements = list(tokens['content'])
        return ParsedModel(name, elements)
    
    @staticmethod
    def from_anonymous_model(tokens):
        elements = list(tokens)
        return ParsedModel(name=None, elements=elements)
    
