from pyparsing import Regex, Word, delimitedList, alphas, Optional, OneOrMore, \
    stringEnd, alphanums, ZeroOrMore, Group, Suppress, lineEnd, \
    ParserElement, Combine, nums, Literal, CaselessLiteral, \
    restOfLine, QuotedString, ParseException, Forward 
from procgraph.core.parsing_elements import VariableReference, ParsedBlock, \
    ParsedAssignment, ImportStatement, ParsedModel, ParsedSignal, \
    ParsedSignalList , Connection, Where
from procgraph.core.exceptions import PGSyntaxError


def eval_dictionary(s, loc, tokens):
    #print "Dict Tokens: %s" % tokens
    if not 'content' in tokens:
        return {}
    d = {}
    for a in tokens:
        #print "A: %s" % a
        if 'value' in a:
            d[a['key']] = a['value']
    
    return d

#def eval_list(s,loc,tokens): 
#    elements = tokens.asList()
#    return elements

def python_interpretation(s, loc, tokens):
    val = eval(tokens[0]) # XXX why 0?
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
integer = Combine(Optional(plusorminus) + number)
floatnumber = Combine(integer + 
                   Optional(point + Optional(number)) + 
                   Optional(e + integer)
                 )
integer.setParseAction(python_interpretation)
floatnumber.setParseAction(python_interpretation)
# comments
comment = Suppress(Literal('#') + restOfLine)
good_name = Combine(Word(alphas) + Optional(Word(alphanums + '_')))

quoted = QuotedString('"', '\\', unquoteResults=True)
reference = Combine(Suppress('$') + good_name('variable'))

reference.setParseAction(VariableReference.from_tokens)

dictionary = Forward()
array = Forward()
value = Forward()
value << (array ^ dictionary ^ reference ^ integer \
          ^ floatnumber ^ good_name ^ quoted)('val')

# dictionaries
    
dict_key = good_name ^ quoted
dictionary << (Suppress("{") + \
    Optional(\
             delimitedList(\
                           Group(\
                                 dict_key('key') + Suppress(':') + value('value')\
                                 ) \
                           ) \
             )('content') + \
    Suppress("}"))
    
    
dictionary.setParseAction(eval_dictionary)
    
#array << Suppress("[") + (delimitedList(value))('content') +Suppress("]")  
#array.setParseAction(eval_list)

array << Group(Suppress("[") + Optional(delimitedList(value)) + Suppress("]"))
#array.setParseAction(eval_list)


def parse_value(string):
    ''' This is useful for debugging '''
    # XXX this is a mess that needs cleaning
    # perhaps now it works without ceremonies
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
        

def parse_model(string, filename=None):
    ''' Returns a list of ParsedModel ''' 

    # We pass a "where" object to the constructors
    def wrap(constructor):
        def from_tokens(string, location, tokens):
            element = constructor(tokens)
            element.where = Where(filename, string, location)
            return element 
        return from_tokens
    
    # make this check a special case, otherwise it's hard to debug
    if not string.strip():
        raise PGSyntaxError('Passed empty string.', Where(filename, string, 0))
    
    arrow = Suppress(Regex(r'-+>'))
    
    # good_name =  Combine(Word(alphas) + Word(alphanums +'_' ))
    # XXX: don't put '.' at the beginning
    qualified_name = Combine(good_name + '.' + (integer ^ good_name))
    
    block_name = good_name
    block_type = Word(alphanums + '_+-/*')
     
    signal = Optional(Suppress('[') + (integer ^ good_name)('local_input') + Suppress(']')) \
            + Optional(block_name('block_name') + Suppress(".")) + (integer ^ good_name)('name') + \
            Optional(Suppress('[') + (integer ^ good_name)('local_output') + Suppress(']'))
    signal.setParseAction(wrap(ParsedSignal.from_tokens))
    
    signals = delimitedList(signal)
    signals.setParseAction(wrap(ParsedSignalList.from_tokens))
    
    key = good_name ^ qualified_name
    
    key_value_pair = Group(key("key") + Suppress('=') + value("value"))
    parameter_list = delimitedList(key_value_pair) ^ OneOrMore(key_value_pair) 
    parameter_list.setParseAction(lambda s, l, t: dict([(a[0], a[1]) for a in t ]))
    
    block = Suppress("|") + Optional(block_name("name") + Suppress(":")) + block_type("blocktype") + \
         Optional(parameter_list("config")) + Suppress("|")
    
    block.setParseAction(wrap(ParsedBlock.from_tokens)) 
    
    between = arrow + Optional(signals + arrow)
    
    # Different patterns
    arrow_arrow = signals + arrow + Optional(block + ZeroOrMore(between + block)) \
     + arrow + signals
    source = block + ZeroOrMore(between + block)  \
     + arrow + signals
    sink = signals + arrow + block + ZeroOrMore(between + block)  
    
    source_sink = block + ZeroOrMore(between + block)
    
    # all of those are colled a connection
    connection = arrow_arrow ^ source_sink ^ source ^ sink
      
    connection.setParseAction(wrap(Connection.from_tokens))
    
    assignment = (key("key") + Suppress('=') + value("value"))
    assignment.setParseAction(ParsedAssignment.from_tokens) 
    
    package_name = good_name + ZeroOrMore('.' + good_name)
    import_statement = Suppress('import') + package_name('package')
    import_statement.setParseAction(wrap(ImportStatement.from_tokens))
    
    
    action = connection ^ assignment ^ comment ^ import_statement
    
    newline = Suppress(lineEnd)
    
    model_content = ZeroOrMore(newline) + action + \
        ZeroOrMore(OneOrMore(newline) + action) + \
    ZeroOrMore(newline) 
    
    named_model = \
    Suppress(Combine('---' + Optional(Word('-')))) + Suppress('model') + \
        good_name('model_name') + newline + \
        model_content('content')
        
    named_model.setParseAction(wrap(ParsedModel.from_named_model))
    
    anonymous_model = model_content.copy()
    anonymous_model.setParseAction(wrap(ParsedModel.from_anonymous_model))
    
    comments = ZeroOrMore((comment + newline) ^ newline)
    pg_file = comments + (OneOrMore(named_model) ^ anonymous_model) + \
        stringEnd 
    
    try:
        parsed = pg_file.parseString(string)
        return list(parsed)
    except ParseException as e:
        where = Where(filename, string, line=e.lineno, column=e.col)
        raise PGSyntaxError('Error in parsing string: %s' % e, where=where)
    
        
