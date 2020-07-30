from cell import Cell
import pyglet

class Board():
    def __init__(self, cell_size, rows=60, columns=60):
        """
        Initializes board with given number of rows, columns
        holding all Dead cells
        """
        self.rows = rows
        self.columns = columns
        self.grid = [[Cell(cell_size) for column_cells in range(self.columns)] for row_cells in range(self.rows)]

    def set_beginning_board(self):
        for row in self.grid:
            for cell in row:
                cell.init_random_state()
    
    def set_checker_board(self):
        """
        TODO: fix (just straight  line)
        """
        counter = 1
        for row in self.grid:
            for cell in row:
                if counter % 2 == 0:
                    cell.set_alive()
                else:
                    cell.set_dead()
                counter+=1

    def update_board(self, new_board):
        """
        New state will be added to the new_board
        (out of place) depending on the number of 
        neighbors and the rules below
        """

        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                n = self.count_neighbors(i,j)

                if cell.is_alive() and (n == 2  or n == 3):
                    new_board.grid[i][j].set_alive()
                elif not cell.is_alive() and n == 3:
                    new_board.grid[i][j].set_alive()
                else:
                    new_board.grid[i][j].set_dead()

        self.grid = new_board.grid
                
    def count_neighbors(self, row, col):
        """
        Counts neighbors by going in a circle around
        the given cell point at position row, col.

        Turns off any cells in the outer layer because
        it goes out of range otherwise. I want to change this
        later. One option is to change it so that the board wraps
        around itself.
        """
        
        n = 0
        
        if (row == 0 or row == self.rows-1):
            return n
        if (col == 0 or col == self.columns-1):
            return n


        if self.grid[row-1][col-1].is_alive():
            n += 1
        if self.grid[row-1][col].is_alive():
            n += 1
        if self.grid[row-1][col+1].is_alive():
            n +=1
        if self.grid[row][col-1].is_alive():
            n +=1
        if self.grid[row+1][col-1].is_alive():
            n +=1
        if self.grid[row][col+1].is_alive():
            n +=1
        if self.grid[row+1][col+1].is_alive():
            n +=1
        if self.grid[row+1][col].is_alive():
            n +=1
        
        return n

    def draw(self):
        """
        Function to draw the cuurrent board to 
        pyglet application
        """

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

    def print_board(self):
        """
        Function to print board to terminal
        For testing purposes
        """
        for row in self.grid:
            print([cell.get_print_character() for cell in row])


















