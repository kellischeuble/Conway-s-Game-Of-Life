import random

def create_board(cols, rows):
    """
    Populates board given values of columns and rows
    with random states between 0 and 1 (dead or alive)
    """
    board = list()

    for row in range(rows):
        board.append([random.randint(0,1) for col in range(cols)])

    return board

def count_neighbors(board, x, y):
    """
    Counts neighbors of given points
    """
    neighbors = 0

    # TODO: 
    # Simplify
    # Deal with edges

    # left
    neighbors += board[x-1][y]

    # right
    neighbors += board[x+1][y]

    # top 3
    neighbors += board[x-1][y-1]
    neighbors += board[x][y-1]
    neighbors += board[x+1][y-1]

    # bottom 3
    neighbors += board[x-1][y+1]
    neighbors += board[x][y+1]
    neighbors += board[x+1][y+1]
    
    return neighbors


