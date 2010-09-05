from procgraph.testing.utils import PGTestCase
from procgraph.core.registrar import default_library, Library
from procgraph.core.model_loader import model_from_string

# All of these models, when interpreted,
# have an output that equals 42

examples_42 = [
('''
--- model master

|slave my_param=42| ---> |output name=meaning| 

--- model slave
config my_param

|c1:constant| --> |output name=c|

c1.value = $my_param

''', {}),

('''
--- model master

|slave my_param=$my_param2| ---> |output name=meaning| 

my_param2 = 42

--- model slave
config my_param

|c1:constant| --> |output name=c|

c1.value = $my_param

''', {}),
('''
--- model master 

|s1:slave| ---> |output name=meaning| 

s1.my_param = 42

--- model slave
config my_param

|c1:constant| --> |output name=c|

c1.value = $my_param

''', {}),
('''
--- model master
my_param2 = 42

|s1:slave| ---> |output name=meaning| 

s1.my_param = $my_param2

--- model slave
config my_param

|c1:constant| --> |output name=c|

c1.value = $my_param

''', {}),
('''
--- model master 
config my_param2

|s1:slave| ---> |output name=meaning| 

s1.my_param = $my_param2

--- model slave
config my_param

|c1:constant| --> |output name=c|

c1.value = $my_param

''', {'my_param2': 42}),
(''' # Default naming
--- model master 

|slave| ---> |output name=meaning| 

--- model slave
config my_param

|constant| --> |output name=c|

constant.value = $my_param

''', {'slave.my_param': 42}),
(''' # Default naming -- recursive.
--- model master 

|slave| ---> |output name=meaning| 

--- model slave

|constant| --> |output name=c| 

''', {'slave.constant.value': 42})

]
 

class ParamsTest(PGTestCase):
    
    def test1(self):
        for model_spec, config in examples_42:
            # don't pollute the main library with the block definitions
            library = Library(default_library)
            model = model_from_string(model_spec, config=config, library=library)
            
            model.reset_execution()
            while model.has_more():
                model.update()

            self.assertEqual(model.get_output(0), 42)
