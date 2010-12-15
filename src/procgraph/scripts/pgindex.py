from optparse import OptionParser
from setuptools import find_packages
from pprint import pprint

from .pgdoc import get_all_info
from ..core.registrar import default_library 
from ..core.import_magic import REQUIRES_PARSED

def main(): 
    parser = OptionParser()
     
    parser.add_option("--output", default='procgraph_packages.py')
    parser.add_option("--src", default='src', help="Source directory")
    
    (options, args) = parser.parse_args()
    
    if args:
        raise Exception('No arguments necessary.')
    
    given_modules = find_packages(options.src)
    given_modules.remove('procgraph.block_utils')
    given_modules.remove('procgraph.core')
    given_modules.remove('procgraph.scripts')
    given_modules.remove('procgraph.testing')
    
    for module in given_modules:
        __import__(module, fromlist=['ceremony']) 
    
    
    all_modules = get_all_info(default_library)
    
    # check they were not empty
    all_info = {'packages': {}}
    for module in given_modules:
        if not module in all_modules:
            print('Warning: I found no blocks defined *directly* in %r. ' 
                  'No index will be generated.' % module)
            continue
        
        info = all_modules[module]
        extract = {}
        #extract['name'] = info.name
        extract['desc'] = info.desc
        extract['blocks'] = info.blocks.keys()
        extract['requires'] = info.procgraph_info.get(REQUIRES_PARSED, {})
        all_info['packages'][info.name] = extract
    
    print("Writing to %r." % options.output)
    with open(options.output, 'w') as f:
        f.write('# Autogenerated file -- do not modify.\n\n')
        f.write('# This file is generated by "pgindex".  \n')
        f.write(
'# It lists the default ProcGraph packages and their dependencies \n'
'# so that we can warn the user if some dependency is not found at \n'
"# install time. ProcGraph's policy is to be very liberal; for example, \n"
"# the `procgraph_cv' package is installed even though OpenCV is not found.\n"
"# and an error will be thrown only if the user actually uses those blocks. \n\n"                
        )
        f.write('index = ')
        pprint(all_info, f)

if __name__ == '__main__':
    main()
