import pyglet
from instructions import user_input, print_intro

from board import Board

def main(board_type, board_size, frame_ps):

	window = pyglet.window.Window(
		width=600,
		height=600,
		caption="Conway's Game of Life"
	)
	
	# label = pyglet.text.Label('Hello, world',
	#                           font_name='Times New Roman',
	#                           font_size=36,
	#                           x=window.width//2, y=window.height//2,
	#                           anchor_x='center', anchor_y='center')

	board = Board()
	if board_type == "checker":
		board.set_checker_board()
	else:
		board.set_beginning_board()

	@window.event
	def on_draw():
		window.clear()
		board.draw()

	@window.event
	def update(dt):
		board.update_board(Board())

	@window.event
	def on_key_press(symbol, modifiers):
		print(f"the {symbol} key was pressed")

	pyglet.clock.schedule_interval(update, 1.0/10.0)
	pyglet.app.run()

if __name__ == '__main__': 

	print_intro()
	play, board_type, board_size, frame_ps = user_input() 

	if play:
		main(board_type, board_size, frame_ps)
	else:
		print("Go Home")
		exit()