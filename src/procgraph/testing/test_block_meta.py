from procgraph.testing.utils import PGTestCase

from procgraph import Block, block_config, block_input, block_input_is_variable, \
block_output_is_variable, block_output
from procgraph.core.exceptions import BlockWriterError


def same_name_mistake_config():
    
    class MyBlock(Block):
        block_config('x', 'description')
        block_config('x', 'description 2', default=True)

def same_name_mistake_input():
    
    class MyBlock(Block):
        block_input('x')
        block_input('x')

def same_name_mistake_output():
    
    class MyBlock(Block):
        block_output('x')
        block_output('x')


def bad_mixing_1():
    
    class MyBlock(Block):
        block_output('x')
        block_output_is_variable()
        
def bad_mixing_2():
    
    class MyBlock(Block):
        block_output_is_variable()
        block_output('x')
        
def bad_mixing_3():
    
    class MyBlock(Block):
        block_input_is_variable()
        block_input('x')
        
def bad_mixing_4():
    
    class MyBlock(Block):
        block_input('x')
        block_input_is_variable()

def bad_mixing_5():
    
    class MyBlock(Block):
        block_input('x')
        block_output_is_variable()

def bad_mixing_6():
    
    class MyBlock(Block):
        block_output_is_variable()
        block_input('x')
        
def bad_mixing_7():
    
    class MyBlock(Block):
        block_output_is_variable()
        
def good_mixing_1():
    
    class MyBlock(Block):
        block_input_is_variable()
        block_output_is_variable()

def good_mixing_2():
    
    class MyBlock(Block):
        block_input_is_variable()
        block_output('only one')

def good_mixing_3():
    
    class MyBlock(Block):
        block_input_is_variable()



class SyntaxTestMultiple(PGTestCase):
    
    def test_same_name_mistake(self):
        ''' Test that we detect when a input, output, config name is repeated. '''
        self.assertRaises(BlockWriterError, same_name_mistake_config)
        self.assertRaises(BlockWriterError, same_name_mistake_input)
        self.assertRaises(BlockWriterError, same_name_mistake_output)
    
    def test_variable_inputs(self):
        self.assertRaises(BlockWriterError, bad_mixing_1)
        self.assertRaises(BlockWriterError, bad_mixing_2)
        self.assertRaises(BlockWriterError, bad_mixing_3)
        self.assertRaises(BlockWriterError, bad_mixing_4)
        self.assertRaises(BlockWriterError, bad_mixing_5)
        self.assertRaises(BlockWriterError, bad_mixing_6)
        self.assertRaises(BlockWriterError, bad_mixing_7)
        self.assertRaises(BlockWriterError, good_mixing_1)
        self.assertRaises(BlockWriterError, good_mixing_2)
        self.assertRaises(BlockWriterError, good_mixing_3)
            
    def test_ok(self):

        class MyBlock(Block):
            block_config('x', 'description')
            block_config('y', 'description 2', default=True)
            block_config('z')
            block_input('x')
            block_input('y')
            block_output('x')
            
        self.assertEqual(len(MyBlock.config), 3)
        self.assertEqual(len(MyBlock.input), 2)
        self.assertEqual(len(MyBlock.output), 1)
