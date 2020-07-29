from cell import Cell
import pyglet

class Board():
    def __init__(self, rows=30, columns=30):
        """
        """
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell() for column_cells in range(self.columns)] for row_cells in range(self.rows)]

    def set_beginning_board(self):
        for row in self.grid:
            for cell in row:
                cell.init_random_state()

    def update_board(self, new_board):
        """
        """

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                n = self.count_neighbors(i,j)

                if cell.is_alive() and (n == 2  or n == 3):
                    new_board.grid[i][j].set_alive()
                if not cell.is_alive() and (n == 3):
                    new_board.grid[i][j].set_alive()
                else:
                    new_board.grid[i][j].set_dead()

        self.grid = new_board.grid
                
    def count_neighbors(self, row, col):
        """
        """
        n = 0

        # TODO: 
        # Simplify this shiit
        
        if (row == 0 or row == self.rows-1):
            row = 1
        if (col ==0 or col == self.columns-1):
            col = 1
        if self.grid[row-1][col].is_alive():
            n += 1
        if self.grid[row+1][col].is_alive():
            n += 1
        if self.grid[row-1][col-1].is_alive():
            n += 1
        if self.grid[row][col-1].is_alive():
            n +=1
        if self.grid[row+1][col-1].is_alive():
            n +=1
        if self.grid[row-1][col+1].is_alive():
            n +=1
        if self.grid[row][col+1].is_alive():
            n +=1
        if self.grid[row+1][col+1].is_alive():
            n +=1
        
        return n

    def print_board(self):
        """
        """
        for row in self.grid:
            print([cell.get_print_character() for cell in row])

    def draw(self):

        for i, row in enumerate(self.grid):
            for col, cell in enumerate(row):
                if cell.is_alive():
                    # (0, 0), (0,20) (20,0), (20,20) < these are the coordinates
                   square_coords = (i * cell.size, col * cell.size,
                                    i * cell.size, col * cell.size + cell.size,
                                    i * cell.size + cell.size, col * cell.size,
                                    i * cell.size + cell.size, col * cell.size + cell.size)
                pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                    [0,1,2,1,2,3],
                                    ('v2i', square_coords))


















