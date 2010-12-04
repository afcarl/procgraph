from ...core.registrar_other import register_simple_block

register_simple_block(lambda x, y: x + y, '+', num_inputs=2)
register_simple_block(lambda x, y: x * y, '*', num_inputs=2)
register_simple_block(lambda x, y: x - y, '-', num_inputs=2)
register_simple_block(lambda x, y: x / y, '/', num_inputs=2)
 
