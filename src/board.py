from cell import Cell

class Board():
    def __init__(self, rows=12, columns=12):
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


















