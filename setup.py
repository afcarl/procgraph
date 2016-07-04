import os, sys
from setuptools import setup, find_packages
from collections import namedtuple

# Load autogenerated list of packages and dependencies
from procgraph_packages import index

version = '1.9'


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


