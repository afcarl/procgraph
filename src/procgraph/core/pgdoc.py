from collections import namedtuple
from optparse import OptionParser

from procgraph.core.model_loader import pg_look_for_models, ModelSpec
from procgraph.core.registrar import default_library 
from procgraph.core.block import Block
import sys
import os


# type = 'model', 'block', 'simple_block'
# implementation: either Class or wrapped function
# 'desc' is the first line of a docstring, 'desc_rest' are the remaining lines
type_block = 'block'
type_model = 'model'
type_simple_block = 'simple_block'

ModelDoc = namedtuple('ModelDoc', 'name source module type implementation input '
                      'output config desc desc_rest')
ModelInput = namedtuple('ModelInput', 'name desc desc_rest')
ModelOutput = namedtuple('ModelOutput', 'name desc desc_rest')
ModelConfig = namedtuple('ModelConfig', 'name default desc desc_rest')
ModuleDoc = namedtuple('ModuleDoc', 'name blocks desc desc_rest')


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
    

def collect_info(block_type, block_generator):
    #print block_type
    
    if isinstance(block_generator, ModelSpec):
        parsed_model = block_generator.parsed_model
        type = type_model
        implementation = None
        module = block_generator.defined_in # XXX
        while  module.__doc__ is None:
            module = module.__package__
        source = parsed_model.where.filename
        desc, desc_rest = split_docstring(parsed_model.docstring) 
        
    elif issubclass(block_generator, Block):
        if block_generator.__name__ == 'GenericOperation':
            func = block_generator.my_operation
            type = type_simple_block
            implementation = func
            source = block_generator.defined_in.__file__ # xxx
            module = block_generator.defined_in
            while  module.__doc__ is None:
                module = module.__package__
                
            doc = block_generator.doc
            if doc is None:
                doc = func.__doc__
            desc, desc_rest = split_docstring(doc)
            
            #func.__file__
            #print block_type, 'SIMPLE_BLOCK', func, func.__name__, func.__module__
        else:
            type = type_block
            implementation = block_generator
            
            module = __import__(block_generator.__module__, fromlist=['x'])
            source = module.__file__
            while  module.__doc__ is None:
                module = module.__package__
                #print "changing to %s" % str(module)
            desc, desc_rest = split_docstring(block_generator.__doc__) 

    else: 
        assert False
#    print " - type\t", type
#    print " - implementation\t", implementation
#    print " - module\t", module
#    print " - source\t", source
#    print " - desc \t", str(desc)
#    print " - desc_rest \t", str(desc_rest)[:30], '...'

    if source.endswith('.pyc'):
        source = source[:-1]

    return ModelDoc(name=block_type, source=source, type=type,
                    module=module, implementation=implementation,
                    desc=desc, desc_rest=desc_rest,
                    input=None, output=None, config=None)

     

def get_all_info(library):
    
    blocks = []
    for block_type, generator in library.name2block.items():
        blocks.append (collect_info(block_type, generator))

    
    # get all modules
    module_names = set(map(lambda x: x.module, blocks))
    # create module -> list of blocks
    
    modules = {}
    
    for name in module_names:
        module_blocks = dict(map(lambda block: (block.name, block),
                         filter(lambda block:block.module == name, blocks)))
        
        actual = __import__(name, fromlist=['ceremony'])
        
        desc, desc_rest = split_docstring(actual.__doc__)
        

        modules[name] = ModuleDoc(name=name, blocks=module_blocks,
                                  desc=desc, desc_rest=desc_rest)
        
        

    return modules

def main(): 
    parser = OptionParser()
     
    parser.add_option("--output", default='pgdoc.rst', help="HTML output file.")
    parser.add_option("--label", default=None, help="Adds a RST label to the generated docs.")
    parser.add_option("--translate", action='append', default=[], help="directory=url")

    (options, args) = parser.parse_args()
    
    
    translate = {}
    for couple in options.translate:
        root, reference = couple.split('=', 1)
        root = os.path.realpath(root)
        translate[root] = reference 
        
    print translate  
    
    if not args:
        print "Give at least one module"
        sys.exit(-1)
        
    for module in args:
        __import__(module)
    #import procgraph.components
    #import bootstrap_experiments_201008
    
    library = default_library
    #pg_look_for_models(library)
    
    all_modules = get_all_info(library)
    # only retain the ones that we have to document 
    modules = {}
    for module in all_modules:
        for arg in args:
            if module.startswith(arg):
                modules[module] = all_modules[module]

    f = open(options.output, 'w')
    
    if options.label is None:
        options.label = args[0]
        print 'Using "%s" as label.' % options.label
    
    f.write('.. |towrite| replace:: **to write** \n\n')
    
    f.write(".. _`%s`:\n\n" % options.label)

    f.write('Summary \n')
    f.write('=' * 60 + '\n\n\n')


    # first write a summary
    for module_name in sorted(modules):
        module = modules[module_name]
        
        f.write('%s\n\n' % module_reference(module.name))
        
        if module.desc:
            f.write(module.desc + '\n\n')
        
        col1 = 200
        col2 = 200
        f.write('='*col1 + ' ' + '=' * col2 + '\n')
        
        for block_name in sorted(module.blocks):
            block = module.blocks[block_name]
            
            desc = str(block.desc) 
            name = block_reference(block.name)
            f.write(name.ljust(col1) + ' ' + desc.ljust(col2) + '\n')             
            

        f.write('='*col1 + ' ' + '=' * col2 + '\n')
        f.write('\n\n')
    
    for module_name in sorted(modules):
        module = modules[module_name]
        
        f.write(module_anchor(module.name))
        f.write('Module ``%s``\n' % module.name)
        f.write('=' * 60 + '\n\n\n')


        if module.desc:
            f.write(module.desc + '\n\n')
        if module.desc_rest:
            f.write(module.desc_rest + '\n\n')
        
        for block_name in sorted(module.blocks):
            block = module.blocks[block_name]
            
            f.write(block_anchor(block.name))
            f.write('Block ``%s``\n' % block.name)
            f.write('-' * 60 + '\n')
            
            url = get_source_ref(block.source, translate)
            f.write('Implemented in %s. \n\n' % url)
            
            if block.desc:
                f.write(block.desc + '\n\n')
            if block.desc_rest:
                f.write(block.desc_rest + '\n\n')

def get_source_ref(source, translation):
    source = os.path.realpath(source)
    for prefix, ref   in translation.items():
        if source.startswith(prefix):
            rest = source[len(prefix):]
            print rest
            url = ref + '/' + rest
            return '`%s <%s>`_' % (rest, url) 
    return source 
        
def module_anchor(name):
    return ".. _`module:%s`:\n\n" % name

def block_anchor(name):
    return ".. _`block:%s`:\n\n" % name

def block_reference(name):
    #return ":ref:`block:%s`" % name
    return ":ref:`%s <block:%s>`" % (name, name) 

def module_reference(name):
    return ":ref:`module:%s`" % name
 
         
