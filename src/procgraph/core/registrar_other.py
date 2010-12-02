import traceback, inspect

from procgraph import Block, ModelExecutionError
from procgraph.core.registrar import default_library
from procgraph.core.model_loader import add_models_to_library


COMPULSORY = 'compulsory-param'
TIMESTAMP = 'timestamp-param'

def make_generic(name, num_inputs, num_outputs,
                 operation, params={}, docs=None):

    # make a copy
    parameters = dict(params)

    class GenericOperation(Block):
        Block.alias(name)
        
        # filled out later
        defined_in = None
        
        if docs is None:
            __doc__ = operation.__doc__
        else:
            __doc__ = docs
            
        my_operation = operation


        for key, value in parameters.items():
            if not value in [TIMESTAMP]:
                if value == COMPULSORY:
                    Block.config(key)
                else:
                    Block.config(key, default=value)
        for i in range(num_inputs):
            Block.input(str(i))
        for i in range(num_outputs):
            Block.output(str(i))
       
        def update(self):
            args = []
            for i in range(num_inputs):
                args.append(self.get_input(i))
                
            params = {}
            for key, value in parameters.items():
                if value == TIMESTAMP:
                    params[key] = max(self.get_input_signals_timestamps())
                else:
                    params[key] = self.get_config(key)
                
            try:
                result = operation(*args, **params)
            except Exception as e:
                traceback.print_exc()
                raise ModelExecutionError("While executing %s: %s." % \
                                          (operation, e), block=self)
        
            if num_outputs == 1:
                self.set_output(0, result)
            else:
                for i in range(num_outputs):
                    self.set_output(i, result[i])
        
    return GenericOperation
    
def register_simple_block(function, name=None, num_inputs=1, num_outputs=1, params={}, doc=None):
    # Get a module to which we can associate this block
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    
    assert name is None or isinstance(name, str)
    if name is None:
        name = function.__name__
    
    block = make_generic(name,
                         num_inputs, num_outputs, function, params=params, docs=doc)
    
    block.defined_in = mod.__name__
    
    assert isinstance(block.defined_in, str) 

def register_block(block_class, name=None):
    assert name is None or isinstance(name, str)
    if name is None:
        name = block_class.__name__
    default_library.register(name, block_class)

def register_model_spec(model_spec):
    frm = inspect.stack()[1]
    mod = inspect.getmodule(frm[0])
    assert mod is not None
    defined_in = mod.__name__
    add_models_to_library(default_library, model_spec, defined_in=defined_in)

 
