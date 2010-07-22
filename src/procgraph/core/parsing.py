from pyparsing import Regex, Word, delimitedList, alphas, Optional, OneOrMore,\
    stringEnd, alphanums, ZeroOrMore, Group, Suppress, lineEnd, \
    ParserElement, Combine, nums, Literal, CaselessLiteral, col, lineno,\
    restOfLine, QuotedString, ParseException, Forward,ParseResults, Dict

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
    
def eval_dictionary(s,loc,tokens):
    print "Dict Tokens: %s" % tokens
    if not 'content' in tokens:
        return {}
    d = {}
    for a in tokens:
        print "A: %s" % a
        if 'value' in a:
            d[a['key']]=a['value']
    
    #return ShieldDict(d.items())
    return d
    #if d:
    #    return ParseResults(toklist=d)
    #else:
    #    return [{}]


class ShieldDict:
    def __init__(self, items):
        self.items = items
        
    def __repr__(self):
        return 'Dict(%s)' % self.items

class ShieldList:
    def __init__(self, elements):
        self.elements = elements
    def __repr__(self):
        return 'List(%s)' % self.elements
    
def eval_list2(s,loc,tokens):
    print "List Tokens: %s" % tokens
    if not 'content' in tokens:
        return ShieldList(tokens)
        #return [[]]
    return ShieldList(tokens.asList())

def eval_list(s,loc,tokens):
#    if not 'content' in tokens:
#        return [[]]
    elements = tokens.asList()
    return elements


def python_interpretation(s,loc,tokens):
    val = eval(tokens[0])
    #print '%s -> %s (%s)' % (tokens, val, type(val))
    return val

# Important: should be at the beginning
# make end of lines count
ParserElement.setDefaultWhitespaceChars(" \t") 
    
# These are just values
# Definition of numbers
number = Word(nums) 
point = Literal('.')
e = CaselessLiteral('E')
plusorminus = Literal('+') | Literal('-')
integer = Combine( Optional(plusorminus) + number )
floatnumber = Combine( integer +
                   Optional( point + Optional(number) ) +
                   Optional( e + integer )
                 )
integer.setParseAction(python_interpretation)
floatnumber.setParseAction(python_interpretation)
# comments
comment = Suppress(Literal('#') + restOfLine)
good_name =  Combine(Word(alphas)+Optional(Word(alphanums +'_')))

quoted = QuotedString('"','\\',unquoteResults=True)
reference = Combine( Suppress('$') + good_name('variable'))

reference.setParseAction(VariableReference.from_tokens)

dictionary = Forward()
array = Forward()
value = Forward()
value << (array ^ dictionary ^ reference ^ integer \
          ^ floatnumber ^  Word(alphanums) ^ quoted)('val')

# dictionaries
    
dict_key = good_name ^ quoted
dictionary << (Suppress("{") + \
    Group(Optional(delimitedList((dict_key('key') +Suppress(':')+ value('value')))))('content') +   \
    Suppress("}"))
    
dictionary.setParseAction(eval_dictionary)
    
#array << Suppress("[") + (delimitedList(value))('content') +Suppress("]")  
#array.setParseAction(eval_list)

array << Group(Suppress("[") + Optional(delimitedList(value)) +Suppress("]"))
#array.setParseAction(eval_list)


def parse_value(string):
    ''' This is useful for debugging '''
    try:
        tokens = value.parseString(string)
        print 'tokens: %s' % tokens
        if isinstance(tokens['val'], dict) or\
           isinstance(tokens['val'], int) or\
           isinstance(tokens['val'], float):
          return tokens['val']
        ret = tokens['val'].asList()
        print "Parsed '%s' into %s (%d), ret: %s" % (string, tokens, len(tokens),
                                                     ret)
        return ret


    except ParseException as e:
        raise SyntaxError('Error in parsing string: %s' % e)
        
        
def parse_model(string):
    ''' Returns a list of ParsedModel ''' 
    
    # make this check a special case, otherwise it's hard to debug
    if not string.strip():
        raise SyntaxError('Passed empty string.')
    
    
    arrow = Suppress(Regex(r'-+>'))
    
    # good_name =  Combine(Word(alphas) + Word(alphanums +'_' ))
    # XXX: don't put '.' at the beginning
    qualified_name = Combine( good_name +'.' + (integer ^ good_name ) )
    

    block_name = good_name
    block_type =   Word(alphanums +'_+-/*' )
     
    signal = Optional(Suppress('[') + (integer ^ good_name  )('local_input') + Suppress(']')) \
            +  Optional(block_name('block_name') + Suppress(".")) + (integer ^ good_name)('name') + \
            Optional(Suppress('[') +  (integer ^ good_name  )('local_output') + Suppress(']'))
    signal.setParseAction(ParsedSignal.from_tokens)
    
    signals = delimitedList(signal)
    signals.setParseAction(ParsedSignalList.from_tokens)
    
    key = good_name ^ qualified_name
    
    
    
    key_value_pair = Group(key("key") + Suppress('=') + value("value"))
    parameter_list =  delimitedList(key_value_pair) ^ OneOrMore(key_value_pair) 
    parameter_list.setParseAction( lambda s,l,t: dict([(a[0],a[1]) for a in t ]))
    
    block = Suppress("|") + Optional(block_name("name") + Suppress(":")) + block_type("blocktype") + \
         Optional(parameter_list("config")) +  Suppress("|")
    
    block.setParseAction(ParsedBlock.from_tokens) 
    
    between = arrow + Optional( signals + arrow)
    
    # Different patterns
    arrow_arrow =  signals + arrow +  Optional( block + ZeroOrMore(between + block) ) \
     + arrow +  signals
    source =   block + ZeroOrMore(between + block)  \
     + arrow +  signals
    sink =   signals + arrow + block + ZeroOrMore(between + block)  
    
    source_sink = block + ZeroOrMore(between + block)
    
    # all of those are colled a connection
    connection = arrow_arrow ^ source_sink ^ source ^ sink  
    connection.setParseAction(Connection.from_tokens)
    
    assignment   = (key("key") + Suppress('=') + value("value"))
    assignment.setParseAction(ParsedAssignment.from_tokens) 
    
    action = connection ^ assignment ^ comment
    
    newline = Suppress(lineEnd)
    
    model_content =  ZeroOrMore(newline) + action + \
        ZeroOrMore( OneOrMore(newline) + action) + \
    ZeroOrMore(newline) 
    
    named_model = \
    Suppress(Combine('---' + Optional(Word('-')))) + Suppress('model') + \
        good_name('model_name') + newline + \
        model_content('content')
        
    named_model.setParseAction(ParsedModel.from_named_model)
    
    anonymous_model = model_content.copy()
    anonymous_model.setParseAction(ParsedModel.from_anonymous_model)
    
    comments = ZeroOrMore( (comment + newline) ^ newline)
    pg_file = comments + ( OneOrMore(named_model) ^ anonymous_model ) +\
        stringEnd 
    
    try:
        parsed = pg_file.parseString(string)
        return list(parsed)
    except ParseException as e:
        raise SyntaxError('Error in parsing string: %s' % e)
        

