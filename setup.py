from setuptools import setup, find_packages
from collections import namedtuple
#
## Check that the dependendencies are there before installing modules
#Option = namedtuple('Option', 'module desc requires')
#
#optional_packages = [
#    
#    Option('procgraph_cv',
#            'Functions to interact with the OpenCV.',
#              ['cv']),
#              
#    Option('procgraph_pil',
#            'Functions to interact with the PIL image library.',
#              ['PIL']),
#              
#    Option('procgraph_mpl',
#            'Functions to interact with matplotlib.',
#            ['PIL', 'matplotlib']),
#            
#    Option('procgraph_robotics', # uses procgraph_mpl
#            'Misc. functions for robotics data sources.',
#            ['PIL', 'matplotlib', 'snp_geometry']),
#                
#    Option('procgraph_hdf', # uses procgraph_mpl
#            'Reading and writing HDF logs..',
#            ['tables'])
#]
#
#
#def is_package_available(p):
#	''' Checks that a package is available. '''
#	try:
#		__import__(p)
#		return True
# 	except ImportError, e:
# 	    return False
#
#ok_to_install = []
#for op in optional_packages:
#	for r in op.requires:
#		if not is_package_available(r):
#			print("Will not install '%s' because '%s' not available." % 
#				  (op.module, r))
#			raw_input('Press any to continue')  
#			break 
#	else:
#		print "Adding optional module %20s" % op.module
#		ok_to_install.append(op.module)

packages = find_packages(where='src')

setup(name='procgraph',
	  version="0.9",
      package_dir={'':'src'},
      #packages=['procgraph'] + ok_to_install,
      packages=packages,
      install_requires=['pyparsing',
                        'simplejson',
                        'numpy',
                        'setproctitle',
                        'termcolor'],
      entry_points={
         'console_scripts': [
           'pg = procgraph.scripts.pg:main',
           'pgdoc = procgraph.scripts.pgdoc:main'
        ]
      },
)


