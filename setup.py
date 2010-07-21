from setuptools import setup

setup(name='procgraph',
	version="0.1",
      package_dir={'':'src'},
      py_modules=['procgraph'],
      install_requires=['pyparsing'],
      entry_points={
         'console_scripts': [
           'pg = procgraph.scripts.pg:main'
        ]
      }, 
)


