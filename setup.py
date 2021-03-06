import os, sys
from setuptools import setup, find_packages
from collections import namedtuple


def get_version(filename):
    import ast
    version = None
    with file(filename) as f:
        for line in f:
            if line.startswith('__version__'):
                version = ast.parse(line).body[0].value.s
                break
        else:
            raise ValueError('No version found in %r.' % filename)
    if version is None:
        raise ValueError(filename)
    return version

version = get_version(filename='src/procgraph/__init__.py')


# Load autogenerated list of packages and dependencies
# from procgraph_packages import index

index = {'packages': {'procgraph.components.debug_components': {'blocks': ['info',
                                                                   'constant',
                                                                   '+',
                                                                   '*',
                                                                   '-',
                                                                   '/',
                                                                   'gain',
                                                                   'print',
                                                                   'identity'],
                                                        'desc': 'Components used for debugging and unit tests.',
                                                        'requires': {}},
              'procgraph_cv': {'blocks': ['gradient', 'smooth'],
                               'desc': 'Blocks using the OpenCV library.',
                               'requires': {'cv': ['cv', 'opencv']}},
              'procgraph_foo': {'blocks': ['block_example'],
                                'desc': 'An example package for ProcGraph that shows how to organize your code. ',
                                'requires': {'pickle': ['cPickle',
                                                        'pickle']}},
              'procgraph_hdf': {'blocks': ['hdfread_many',
                                           'hdfread_test',
                                           'hdfread_many_test',
                                           'hdfwrite',
                                           'hdfread'],
                                'desc': 'This is a set of blocks to read and write logs in HDF_ format. ',
                                'requires': {'tables': ['tables']}},
              'procgraph_images': {'blocks': ['rgb2gray',
                                              'compose',
                                              'reshape2d',
                                              'solid',
                                              'blend',
                                              'skim_top_and_bottom',
                                              'posterize',
                                              'gray2rgb',
                                              'scale',
                                              'grid',
                                              'skim_top',
                                              'posneg',
                                              'border'],
                                   'desc': 'Blocks for basic operations on images. ',
                                   'requires': {}},
              'procgraph_io_misc': {'blocks': ['pickle_load',
                                               'to_file',
                                               'pickle',
                                               'pickle_group',
                                               'as_json'],
                                    'desc': 'Miscellaneous functions to be better organized.',
                                    'requires': {'json': ['simplejson']}},
              'procgraph_mpl': {'blocks': ['plot'],
                                'desc': 'Blocks using Matplotlib to display data.',
                                'requires': {'matplotlib': ['matplotlib'],
                                             'matplotlib.pylab': ['matplotlib.pylab']}},
              'procgraph_mplayer': {'blocks': ['mplayer', 'mencoder'],
                                    'desc': 'Blocks for encoding/decoding video based on MPlayer.',
                                    'requires': {}},
              'procgraph_numpy_ops': {'blocks': ['smooth1d',
                                                 'square',
                                                 'sign',
                                                 'minimum',
                                                 'select',
                                                 'rad2deg',
                                                 'outer',
                                                 'log',
                                                 'sum',
                                                 'astype',
                                                 'arctan',
                                                 'abs',
                                                 'take',
                                                 'real',
                                                 'deg2rad',
                                                 'hstack',
                                                 'flipud',
                                                 'max',
                                                 'vstack',
                                                 'gradient1d',
                                                 'dstack',
                                                 'maximum',
                                                 'fliplr',
                                                 'normalize_Linf',
                                                 'mean'],
                                      'desc': 'Various operations wrapping numpy functions.',
                                      'requires': {}},
              'procgraph_pil': {'blocks': ['imread', 'text', 'resize'],
                                'desc': 'Blocks for image operations based on the PIL library',
                                'requires': {'PIL': ['PIL']}},
              'procgraph_robotics': {'blocks': ['pose2commands',
                                                'laser_display',
                                                'skim',
                                                'organic_scale',
                                                'pose2vel_',
                                                'laser_dot_display'],
                                     'desc': 'Some functions specific to robotics applications. ',
                                     'requires': {'geometry': ['geometry']}},
              'procgraph_ros': {'blocks': ['bagread_test',
                                           'ros2python',
                                           'bagread'],
                                'desc': 'This is a set of blocks to read and write logs in ROS_ Bag format. ',
                                'requires': {'ros': ['ros']}},
              'procgraph_signals': {'blocks': ['derivative2',
                                               'slice',
                                               'two_step_difference',
                                               'derivative',
                                               'join',
                                               'sync',
                                               'fps_data_limit',
                                               'history',
                                               'historyt',
                                               'forward_difference',
                                               'low_pass',
                                               'make_tuple',
                                               'fps_limit',
                                               'fps_print',
                                               'last_n_samples',
                                               'sieve',
                                               'extract',
                                               'any',
                                               'wait'],
                                    'desc': 'Blocks performing operations with a dynamic nature. ',
                                    'requires': {}},
              'procgraph_statistics': {'blocks': ['cov2corr',
                                                  'normalize',
                                                  'expectation',
                                                  'covariance',
                                                  'soft_variance',
                                                  'variance'],
                                       'desc': 'Blocks for common statistical operations.',
                                       'requires': {}},
              'procgraph_yaml': {'blocks': ['yaml2object'],
                                 'desc': 'YAML conversions.',
                                 'requires': {'yaml': ['yaml']}}}}


def is_package_available(p):
	''' Checks that a package is available. '''
	try:
		__import__(p)
		return True
 	except ImportError as e:
         # print("Warning: cannot import %r: %s" % (p, e)) 
         return False

missing = {}
problems = set()
for module, info in index['packages'].items():
    for requirement, options in info['requires'].items():
        if not any([is_package_available(op) for op in options]):
            print("For package %r, dependency %r cannot be satisfied." % 
				  (module, requirement))
            missing[requirement] = options
            # XXX: this is slightly incorrect if different packages want
            # the same module but give different alternatives.
            problems.add(module)

if missing:
    print('\n\n')
    print('Dependency search problems summary')
    print('----------------------------------\n')
    print('I could not find the following packages installed:\n')
    for requirement, options  in missing.items():
    	if len(options) > 1:
    		possible = " or ".join([x.__repr__() for x in options])
    		o = '(Satisfiable by %s.)' % possible
    	else:
    		o = ''
        print(' - %-20s  %s' % (requirement, o))

    print('\nThese missing requirements could make the following packages '
		  'not work properly:\n')

    for p in problems:
        desc = index['packages'][p]['desc']
        print(' - %-20s  (%s)' % (p, desc))

    print('\nI will go ahead and install everything, but you should install the missing \n'
          'packages for maximum functionality. An error will be thrown when you actually \n'
          'try to use the blocks in those packages. \n')
    # if os.isatty(0):	    
# 	raw_input('             Press any key to continue...')  
    print('\n\n')

# check we are not forgetting new packages that weren't included in the 
# autogenerated list yet.
packages = find_packages(where='src')
for p in packages:
    if p == 'procgraph' or p.startswith('procgraph.'): continue
    if not p in index['packages']:
        print('Warning: packages %r is not in the autogenerated index.' % p)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()



setup(name='procgraph',
      author="Andrea Censi",
      author_email="censi@mit.edu",
      url='http://andreacensi.github.com/procgraph/',

      description='ProcGraph ("processing graph") is a Python library '
                    'for rapid prototyping of processing pipelines for '
                    'logged and realtime data.',
      long_description=read('README.txt'),
      keywords="",
      license="LGPL",

      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Topic :: Scientific/Engineering'
      ],

      version=version,
      package_dir={'':'src'},
      packages=find_packages(where='src'),
#       package_data={'': ['*.pg'],
# 				'prograph_cv': ['models/cv_demo_feature.pg']},
	  include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools-git',
        'pyparsing',
        'setproctitle',
        'termcolor',
        'SystemCmd',
        'PyContracts',
        'qtfaststart',
      ],
      # TODO: add many depedendencies
      tests_require=['nose>1.1.2,<2'],
      entry_points={
         'console_scripts': [
           'pg = procgraph.scripts.pgmain:main',
           'pgdoc = procgraph.scripts.pgdoc:main',
           'pgindex = procgraph.scripts.pgindex:main',
           # some other utils
    	     'pg-video-info = procgraph_mplayer.scripts.video_info:main',
    	     'pg-video-convert = procgraph_mplayer.scripts.video_convert:main',
	         'pg-video-crop = procgraph_mplayer.scripts.crop_video:main',
           'pg-video-join = procgraph_mplayer.scripts.join_video:main',
           'pg-video-background = procgraph_mplayer.scripts.find_background:main',
           'pg-video-tomp4 = procgraph_mplayer.scripts.tomp4:main',
        ]
      },
      download_url=('http://github.com/AndreaCensi/procgraph/tarball/%s'
				  	% version),
)


