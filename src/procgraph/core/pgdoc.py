import sys, os
from collections import namedtuple
from optparse import OptionParser

from procgraph.core.model_loader import  ModelSpec
from procgraph.core.registrar import default_library 
from procgraph.core.block import Block
from procgraph.core.block_meta import split_docstring, FIXED

 
type_block = 'block'
type_model = 'model'
type_simple_block = 'simple_block'

ModelDoc = namedtuple('ModelDoc', 'name source module type implementation input '
                      'output config desc desc_rest')

ModuleDoc = namedtuple('ModuleDoc', 'name blocks desc desc_rest')


def get_module_name_with_doc(original_module_name):
    assert isinstance(original_module_name, str) 
  
    module_name = original_module_name
    
    while True:
        module = __import__(module_name, fromlist=['x'])
        if module.__doc__:
            return module.__name__
      
        parent_name = '.'.join(module.__name__.split('.')[:-1])

        # Empty!!
        if not parent_name or parent_name == 'procgraph':
            return original_module_name

        module_name = parent_name


def collect_info(block_type, block_generator): 
    
    if isinstance(block_generator, ModelSpec):
        parsed_model = block_generator.parsed_model
        type = type_model
        implementation = None
        assert isinstance(block_generator.defined_in, str)
        module = get_module_name_with_doc(block_generator.defined_in)
        
        source = parsed_model.where.filename
        desc, desc_rest = split_docstring(parsed_model.docstring) 
        
        config = parsed_model.config
        input = parsed_model.input
        output = parsed_model.output 
        
    elif issubclass(block_generator, Block): 
        type = type_block
        implementation = block_generator
        
        #print block_type, "block_generator.__module__", block_generator.__module__
        if block_generator.defined_in:
            original_module_name = block_generator.defined_in
            assert isinstance(block_generator.defined_in, str)
        else:
            original_module_name = block_generator.__module__
            
        assert isinstance(original_module_name, str)
        
        original_module = __import__(original_module_name, fromlist=['x'])
        
        source = original_module.__file__
        module = get_module_name_with_doc(original_module_name)
            
        desc, desc_rest = split_docstring(block_generator.__doc__) 
        
        config = block_generator.config
        input = block_generator.input
        output = block_generator.output

    else: 
        assert False
        
    #  print block_type, module
         

    if source.endswith('.pyc'):
        source = source[:-1]

    if not isinstance(module, str):
        print block_type, 'has it wrong'
    
    return ModelDoc(name=block_type, source=source, type=type,
                    module=module, implementation=implementation,
                    desc=desc, desc_rest=desc_rest,
                    input=input, output=output, config=config)

     

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
         
    if not args:
        print "Give at least one module"
        sys.exit(-1)
        
    for module in args:
        __import__(module) 
    
    library = default_library 
    
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

            if block.desc is None:
                print 'Warning: %s does not have a description.' % block_name
            
            desc = str(block.desc) 
            name = block_reference(block.name)
            f.write(name.ljust(col1) + ' ' + desc.ljust(col2) + '\n')             
            

        f.write('='*col1 + ' ' + '=' * col2 + '\n')
        f.write('\n\n')
    
    for module_name in sorted(modules):
        module = modules[module_name]
        
        f.write(module_anchor(module.name))
        f.write(rst_class('procgraph:module'))
        f.write('Module ``%s``\n' % module.name)
        f.write('=' * 60 + '\n\n\n')


        if module.desc:
            f.write(rst_class('procgraph:desc'))
            f.write(module.desc + '\n\n')
        if module.desc_rest:
            f.write(rst_class('procgraph:desc_rest'))
            f.write(module.desc_rest + '\n\n')
        
        for block_name in sorted(module.blocks):
            block = module.blocks[block_name]
            
            f.write(block_anchor(block.name))
            f.write(rst_class('procgraph:block'))
            f.write('``%s``\n' % block.name)
            f.write('-' * 60 + '\n')
            
            if block.desc:
                f.write(block.desc + '\n\n')
                
            if block.desc_rest:
                f.write(block.desc_rest + '\n\n')
                
            if block.config:
                f.write(rst_class('procgraph:config'))
                f.write('Configuration\n')
                f.write('^' * 60 + '\n\n')
                for c in block.config:
                    if c.has_default:
                        f.write('- ``%s`` (default: %s): %s\n\n' % 
                                (c.variable, c.default, c.desc))
                    else:
                        f.write('- ``%s``: %s\n\n' % (c.variable, c.desc))
                        # TODO: add desc_rest
      
            if block.input:
                f.write(rst_class('procgraph:input'))
                f.write('Input\n')
                f.write('^' * 60 + '\n\n')
                for i in block.input:
                    if i.type == FIXED:
                        f.write('- ``%s``: %s\n\n' % 
                                (i.name, i.desc))
                    else:
                        f.write('%s (variable: %s <= n <= %s)\n\n' % (i.desc, i.min, i.max))

            if block.output:
                f.write(rst_class('procgraph:output'))
                f.write('Output\n')
                f.write('^' * 60 + '\n\n')
                for o in block.output:
                    if o.type == FIXED:
                        f.write('- ``%s``: %s\n\n' % 
                                (o.name, o.desc))
                    else:
                        f.write('%s (variable number)\n\n' % (o.desc))
              
            
            url = get_source_ref(block.source, translate)
            f.write(rst_class('procgraph:source'))
            f.write('Implemented in %s. \n\n\n' % url)

def get_source_ref(source, translation):
    source = os.path.realpath(source)
    for prefix, ref   in translation.items():
        if source.startswith(prefix):
            rest = source[len(prefix):] 
            url = ref + '/' + rest
            return '`%s <%s>`_' % (rest, url) 
    return source 
        

def rst_class(c):
    return '\n.. rst-class:: %s\n\n' % c

def module_anchor(name):
    return ".. _`module:%s`:\n\n" % name

def block_anchor(name):
    return ".. _`block:%s`:\n\n" % name

def block_reference(name):
    #return ":ref:`block:%s`" % name
    return ":ref:`%s <block:%s>`" % (name, name) 

def module_reference(name):
    return ":ref:`module:%s`" % name
 
         
