from procgraph.core.exceptions import SemanticError, ModelExecutionError, \
    x_not_found
import pickle


class ModelLoadAndSave():
    
    def __init__(self):
        # Array of tuples (what, where, format)
        self.__load_actions = []
        self.__save_actions = []

    def add_load_action(self, what, where, format, element):
        '''
        element: ParsedElement, used for pretty printing of errors. 
        '''
        self.__load_actions.append((what, where, format, element))    

    def add_save_action(self, what, where, format, element):
        '''
        element: ParsedElement, used for pretty printing of errors. 
        '''
        self.__save_actions.append((what, where, format, element))

    def process_load_actions(self):        
        for what, where, format, element in self.__load_actions:
            block, var = self.__resolve(what, element)
            load, save = self.__get_functions(where, format, element) #@UnusedVariable
            data = load()
            
            if var is not None:
                block.set_state(var, data)
            else:
                if not isinstance(data, dict):
                    raise ModelExecutionError(
                        'For loading into %s I expected a dict, got instead %s.'\
                        (what, data.__class__.__name__))
                for key, value in data.items():
                    block.set_state(key, value)
                    
    def process_save_actions(self):        
        for what, where, format, element in self.__save_actions:
            block, var = self.__resolve(what, element)
            load, save = self.__get_functions(where, format, element) #@UnusedVariable
            
            if var is not None:
                data = block.get_state(var)
            else:
                data = {}
                for key in block.get_state_vars():
                    data[key] = block.get_state(key)

            save(data)

    def __resolve(self, what, element):
        ''' Returns a block, or a tuple (block, varname) '''
        # "where" can be:
        # - "blockname"
        # - "blockname.varname"
        assert isinstance(what, str)

        if '.' in what:
            block, name = what.split('.', 1)
            # TODO: recursive
        else:
            block = what
            name = None
        
        if not block in self.name2block:
            raise SemanticError(
                    x_not_found('block', block, self.name2block), element)
            
        block = self.name2block[block]
        
        return block, name
        
     
    
    def __get_functions(self, where, format, element):
        ''' Returns a pair of function load, save.
            where: filename (used for hint if format is none)
            
            element: ParsedElement (for pretty printing of the error)
        '''
        
        if format is None:
            if where.endswith('pickle'):
                format = 'pickle'
            if where.endswith('mat'):
                format = 'matlab'
            if where.endswith('npy'):
                format = 'numpy'                
            if where.endswith('raw'):
                format = 'numpy_raw'
        
        # default is pickle
        if format is None:
            format = 'pickle'
    
        functions = {
            'pickle': 
            (lambda: pickle.load(open(where)),
             lambda x: pickle.dump(x, open(where, 'w'))) 
        }
        
        if not format in functions:
            raise ModelExecutionError(
                    x_not_found('format', format, functions), element)
       
        return functions[format]
        
            
        
        
        
