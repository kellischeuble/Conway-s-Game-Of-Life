import pyglet

from board import Board

def main():
	# set up game window
	window = pyglet.window.Window(
		width=800,
		height=800,
		caption="Conway's Game of Life"
	)
	label = pyglet.text.Label('Hello, world',
	                          font_name='Times New Roman',
	                          font_size=36,
	                          x=window.width//2, y=window.height//2,
	                          anchor_x='center', anchor_y='center')

	@window.event
	def on_draw():
	    window.clear()
	    label.draw()

	@window.event
	def on_key_press(symbol, modifiers):
		print(f"the {symbol} key was pressed")


if __name__ == '__main__': 
	window = Window()
	pyglett.app.run()