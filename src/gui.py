import pyglet
from board import Board

def create_window(board_type, cell_size, frame_ps):
    
	window = pyglet.window.Window(
		width=800,
		height=800,
		caption="Conway's Game of Life"
	)

	board = Board(cell_size)
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
		board.update_board(Board(cell_size))

	@window.event
	def on_key_press(symbol, modifiers):
		print(f"the {symbol} key was pressed")

	pyglet.clock.schedule_interval(update, 1.0/frame_ps)
	pyglet.app.run()