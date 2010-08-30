from numpy import ceil, sqrt, zeros

from procgraph import Block, block_config, block_alias, \
                block_input_is_variable, block_output 

from procgraph.components import check_rgb_or_grayscale
from procgraph.components.images.compose import place_at  


class ImageGrid(Block):
    ''' A block that creates a larger image by arranging them in a grid. '''
    
    block_alias('grid')
    
    block_config('cols', 'Columns in the grid.')
    
    block_input_is_variable('Images to arrange in a grid.')
    block_output('grid', 'Images arranged in a grid.')
    
    def init(self):        
        self.define_output_signals(['grid'])
        self.set_config_default('cols', None)
        
    def update(self):
        n = self.num_input_signals()
        for i in range(n):
            if self.get_input(i) is None:
                # we only go if everything is ready
                return
            check_rgb_or_grayscale(self, i)
            
        cols = self.config.cols
        
        if cols is None:
            cols = int(ceil(sqrt(n)))
            
        if not isinstance(cols, int):
            raise Exception('Expected an integer for cols, not %s.' % cols)
            
        rows = int(ceil(n * 1.0 / cols))
        
        assert cols > 0 and rows > 0
        assert n <= cols * rows
        
        # find width and height for the grid 
        col_width = zeros(cols, dtype='int32')
        row_height = zeros(rows, dtype='int32')
        for i in range(n):
            col = i % cols
            row = (i - i % cols) / cols
            assert 0 <= col < cols
            assert 0 <= row < rows

            image = self.get_input(i)
            width = image.shape[1]
            height = image.shape[0]

            col_width[col] = max(width, col_width[col])
            row_height[row] = max(height, row_height[row])
        
        canvas_width = sum(col_width)
        canvas_height = sum(row_height)
             
        # find position for each col and row
        col_x = zeros(cols, dtype='int32')
        for col in range(1, cols):
            col_x[col] = col_x[col - 1] + col_width[col - 1]
        
        assert(canvas_width == col_x[-1] + col_width[-1])
        
        row_y = zeros(rows, dtype='int32')
        for row in range(1, rows):
            row_y[row] = row_y[row - 1] + row_height[row - 1]
        assert(canvas_height == row_y[-1] + row_height[-1])
        
        canvas = zeros((canvas_height, canvas_width, 3), dtype='uint8')
        
        for i in range(n):
            col = i % cols
            row = (i - i % cols) / cols
            assert 0 <= col < cols
            assert 0 <= row < rows
            image = self.get_input(i)
            x = col_x[col]
            y = row_y[row]
            place_at(canvas, image, x, y)
            
        self.set_output(0, canvas)

 
            
