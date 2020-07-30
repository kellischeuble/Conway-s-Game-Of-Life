import pyglet
from gui import create_window
from instructions import get_user_input, print_intro

def main(board_type, cell_size, frame_ps):

	create_window(board_type, cell_size, frame_ps)

if __name__ == '__main__': 

	print_intro()
	play, board_type, cell_size, frame_ps = get_user_input() 

	if play:
		main(board_type, cell_size, frame_ps)
	else:
		print("Go Home")
		exit()