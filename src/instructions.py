    
board_types = ["random", "checker_board"]
board_sizes = ["15x15", "30x30", "60x60"]

def print_intro():
    """
    Prints out the rules of the game and user input
    """
    print("Hello, welcome to Conway's Game of Life")
    print("Here are the rules: \n")
    print("""
    1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.\n
    2. Any live cell with two or three live neighbours lives on to the next generation.\n
    3. Any live cell with more than three live neighbours dies, as if by overpopulation.\n
    4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.\n
    """)

def wrong_input():
    print("\n!!!!!! Please enter in the right input next time !!!! \n")
    exit()

def user_input():
    """
    Determines the starting board type, board size, and frames/second
    """

    play = input("Are you ready to play? (y/n)\n")
    
    if play.lower() == "y":
        
        board_type = input("""\nWhat would you like your starting board to be? \n -----------------
        Options: \n 1. Random 2. Checker Board (1/2)\n""")
        if board_type == "1":
            board_type = "random"
        elif board_type == "2":
            board_type = "checker"
        else:
            wrong_input()
            
        
        cell_size = input("""\nHow large do you want the cells to be? \n -----------------
        Options: \n 1. Small, 2. Medium, 3. Large (1/2/3)\n""")
        if cell_size == "1":
            cell_size = 8
        elif cell_size == "2":
            cell_size = 20
        elif cell_size == "3":
            cell_size = 50
        else:
            wrong_input()

        frame_ps = input("""\nHow fast do you want it to go? \n -----------------
        Options: \n 1. Very slow 2. Medium 3. Fast (1/2/3)\n""")
        if frame_ps == "1":
            frame_ps = 1
        elif frame_ps == "2":
            frame_ps = 10
        elif frame_ps == "3":
            frame_ps = 50
        else:
            wrong_input()
        print(board_type, type(cell_size), cell_size, frame_ps)
        return True, board_type, cell_size, frame_ps
    
    else: 
        return False, None, None, None