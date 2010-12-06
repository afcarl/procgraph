''' ProcGraph: what you would get if simulink was written in python 
    and was actually useful for dealing with log data. '''

__version__ = '0.9.0'

from procgraph.core.exceptions import *

from procgraph.core.block_meta import block_config, block_input, block_output, \
    block_output_is_variable, block_input_is_variable, block_alias

from procgraph.core.block import Block, Generator

from procgraph.core.model_loader import pg_add_this_package_models

from procgraph.core.registrar_other import \
    register_model_spec, register_simple_block, COMPULSORY

from procgraph.scripts.pg import pg

from procgraph.core.import_magic import import_magic, import_succesful


