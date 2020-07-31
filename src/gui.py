import pyglet
from board import Board
import os

def create_window(board_type, cell_size, frame_ps):
    
    window = pyglet.window.Window(
        width=800,
        height=800,
        caption="Conway's Game of Life"
    )

    label = pyglet.text.Label(f"{round}",
                          font_name='Times New Roman',
                          font_size=36,
                          x=10, y=10)

    board = Board(cell_size)

    if board_type == "penta-decathlon":
        board.set_penta()
    elif board_type == "pulsar":
        board.set_pulsar()
    else:
        board.set_beginning_board()

    @window.event
    def on_draw():
        window.clear()
        board.draw()
        label.draw()

    @window.event
    def update(dt):
        board.update_board(Board(cell_size))

    @window.event
    def on_key_press(symbol, modifiers):
        print(f"the {symbol} key was pressed")

    sound = pyglet.media.load("/Users/kellischeuble/Desktop/classes/lambda-material/CS/unit1/Conway-s-Game-Of-Life/src/music/Analog-synth-loop-110-bpm.wav")
    sound.play()

    pyglet.clock.schedule_interval(update, 1.0/frame_ps)
    pyglet.app.run()