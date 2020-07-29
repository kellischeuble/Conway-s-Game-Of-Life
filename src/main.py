import pyglet

from board import Board

def main():
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

	b = Board()
	b.set_beginning_board()

	@window.event
	def on_draw():
	    
		window.clear()
		b.draw()

	@window.event
	def on_key_press(symbol, modifiers):
		print(f"the {symbol} key was pressed")

	pyglet.app.run()

if __name__ == '__main__': 
	main()