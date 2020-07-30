    
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
            
        
        board_size = input("""\nHow many rows/columns do you want? \n -----------------
        Options: \n 1. 15x15, 2. 30x30, 3. 60x60 (1/2/3)\n""")
        if board_size == "1":
            board_size == 15
        elif board_size == "2":
            board_size = 30
        elif board_size == "3":
            board_size = 60
        else:
            wrong_input()

        frame_ps = input("""\nHow fast do you want it to go? \n -----------------
        Options: \n 1. Very slow 2. Medium 3. Fast (1/2/3)\n""")
        if frame_ps == "1":
            frame_ps = 1
        elif frame_ps == "2":
            frame_ps = 20
        elif frame_ps == "3":
            frame_ps = 60
        else:
            wrong_input()
        print(board_type, board_size, frame_ps)
        return True, board_type, board_size, frame_ps
    
    else: 
        return False, None, None, None