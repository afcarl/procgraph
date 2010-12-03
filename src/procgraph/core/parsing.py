from pyparsing import Regex, Word, delimitedList, alphas, Optional, OneOrMore, \
    stringEnd, alphanums, ZeroOrMore, Group, Suppress, lineEnd, \
    ParserElement, Combine, nums, Literal, CaselessLiteral, \
    restOfLine, QuotedString, ParseException, Forward 

from .parsing_elements import VariableReference, ParsedBlock, \
    ParsedAssignment, ImportStatement, ParsedModel, ParsedSignal, \
    ParsedSignalList, Connection, Where, \
 output_from_tokens, input_from_tokens, config_from_tokens
from .exceptions import PGSyntaxError


def eval_dictionary(s, loc, tokens): #@UnusedVariable
    #print "Dict Tokens: %s" % tokens
    if not 'content' in tokens:
        return {}
    d = {}
    for a in tokens:
        #print "A: %s" % a
        if 'value' in a:
            d[a['key']] = a['value']
    
    return d 

def python_interpretation(s, loc, tokens): #@UnusedVariable
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

# All kinds of python strings

single_quoted = QuotedString('"', '\\', unquoteResults=True) | \
                 QuotedString("'", '\\', unquoteResults=True) 
multi_quoted = QuotedString(quoteChar='"""', escChar='\\',
                              multiline=True, unquoteResults=True) | \
                 QuotedString(quoteChar="'''", escChar='\\',
                              multiline=True, unquoteResults=True)
quoted = multi_quoted | single_quoted 

reference = Combine(Suppress('$') + good_name('variable'))

# FIXME: add wrap also here?
reference.setParseAction(VariableReference.from_tokens)

dictionary = Forward()
array = Forward()
value = Forward()
value << (
          quoted | 
          array | 
          dictionary | 
          reference | 
          good_name | 
          integer | 
          floatnumber
         )('val')

# dictionaries
    
dict_key = good_name | quoted
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
     
array << Group(Suppress("[") + Optional(delimitedList(value)) + Suppress("]"))


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
    
    # Shortcuts
    S = Suppress
    O = Optional
      
    arrow = S(Regex(r'-+>'))
    
    # good_name =  Combine(Word(alphas) + Word(alphanums +'_' ))
    # XXX: don't put '.' at the beginning
    qualified_name = Combine(good_name + '.' + (integer | good_name))
    
    block_name = good_name 
    block_type = good_name | Word('_+-/*') | quoted | reference
     
    signal = O(S('[') + (integer | good_name)('local_input') + S(']')) \
            + O(block_name('block_name') + S(".")) + (integer | good_name)('name') + \
            O(S('[') + (integer | good_name)('local_output') + S(']'))
    signal.setParseAction(wrap(ParsedSignal.from_tokens))
    
    signals = delimitedList(signal)
    signals.setParseAction(wrap(ParsedSignalList.from_tokens))
    
    key = good_name ^ qualified_name
    
    key_value_pair = Group(key("key") + S('=') + value("value"))
    parameter_list = delimitedList(key_value_pair) ^ OneOrMore(key_value_pair) 
    parameter_list.setParseAction(
        lambda s, l, t: dict([(a[0], a[1]) for a in t ])) #@UnusedVariable
    
    block = S("|") + O(block_name("name") + S(":")) + block_type("blocktype") + \
         O(parameter_list("config")) + S("|")
    
    block.setParseAction(wrap(ParsedBlock.from_tokens)) 
    
    between = arrow + O(signals + arrow)
    
    # Different patterns
    arrow_arrow = signals + arrow + O(block + ZeroOrMore(between + block)) \
                 + arrow + signals
    source = block + ZeroOrMore(between + block)  \
             + arrow + signals
    sink = signals + arrow + block + ZeroOrMore(between + block)  
    
    source_sink = block + ZeroOrMore(between + block)
    
    # all of those are colled a connection
    connection = arrow_arrow | (source_sink ^ source ^ sink)
      
    connection.setParseAction(wrap(Connection.from_tokens))
    
    # allow breaking lines with backslash
    continuation = '\\' + lineEnd
    # connection.ignore(continuation)
    
    
    assignment = (key("key") + S('=') + value("value"))
    assignment.setParseAction(wrap(ParsedAssignment.from_tokens)) 
    
    package_name = good_name + ZeroOrMore('.' + good_name)
    import_statement = S('import') + package_name('package')
    import_statement.setParseAction(wrap(ImportStatement.from_tokens))
    
    # Loading statements: a bad idea
    
#    loading = O(S('on')) + S('init') + S(':') + \
#        S('load') + key('what') + O(S('from')) + value('where') + \
#         O(S('as') + good_name('format'))
#    loading.setParseAction(wrap(LoadStatement.from_tokens))
#    
#    saving = O(S('on')) + S('finish') + S(':') + \
#        S('save') + key('what') + O(S('to')) + value('where') + \
#         O(S('as') + good_name('format'))
#    saving.setParseAction(wrap(SaveStatement.from_tokens))
    
    config = S('config') + good_name('variable') + O(S('=') + value('default')) + \
        O(quoted('docstring'))
    config.setParseAction(wrap(config_from_tokens))
    
    input = S('input') + good_name('name') + O(quoted('docstring'))
    input.setParseAction(wrap(input_from_tokens))

    output = S('output') + good_name('name') + O(quoted('docstring'))
    output.setParseAction(wrap(output_from_tokens))
    
    newline = S(lineEnd)
    
    # TODO: remove this
    # dataio = loading ^ saving
    
    docs = S(ZeroOrMore(multi_quoted + OneOrMore(newline)))
    
    action = \
        comment | \
        config | \
        input | \
        output | \
        (docs + connection) | \
        (docs + assignment) | \
        (docs + import_statement)
        
    #dataio ^ \
              
    
    model_content = ZeroOrMore(newline) + action + \
                    ZeroOrMore(OneOrMore(newline) + action) + \
                    ZeroOrMore(newline) 
    
    named_model = \
        Suppress(Combine('---' + Optional(Word('-')))) + Suppress('model') + \
        good_name('model_name') + OneOrMore(newline) + \
        O(quoted('docstring')) + \
        model_content('content')
        
    named_model.setParseAction(wrap(ParsedModel.from_named_model))
    
    anonymous_model = model_content.copy()
    anonymous_model.setParseAction(wrap(ParsedModel.from_anonymous_model))
    
    comments = ZeroOrMore((comment + newline) | newline)
    pg_file = comments + (OneOrMore(named_model) | anonymous_model) + \
        stringEnd 
    
    try:
        parsed = pg_file.parseString(string)
        return list(parsed)
    except ParseException as e:
        where = Where(filename, string, line=e.lineno, column=e.col)
        raise PGSyntaxError('Error in parsing string: %s' % e, where=where)
    
        
