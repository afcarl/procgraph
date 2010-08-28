

Types of nodes:

	A - fixed number of inputs, fixed number of outputs
		Most of the blocks.
	
	B - variable number of inputs (>= K), fixed number of outputs
		For example: min, max, most numpy functions
			
	C - variable number of inputs (>= K), same number of outputs
		For example: sync


In the case of a Model: only type A is supported.

In the case of a Block, we allow all 3.

	class TypeA(Block):
		input('input1', 'desc')
		input('input2', 'desc')
		output('input2', 'desc')
		...
		
		
	class TypeB(Block):
		input_variable('Signals to be summed.', min=K)
		output('output2', 'Sum of the signals.')
		...

	class TypeC(Block):
		input_variable('Signals to be summed.', min=K)
		output_variable('Synchronized signals.')
		

In the case of a simple block




