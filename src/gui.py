import pyglet
from board import Board
import os

def create_window(board_type, cell_size, frame_ps):
    
    window = pyglet.window.Window(
        width=800,
        height=800,
        caption="Conway's Game of Life"
    )

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

    @window.event
    def update(dt):
        board.update_board(Board(cell_size))

    sound = pyglet.media.load("/Users/kellischeuble/Desktop/classes/lambda-material/CS/unit1/Conway-s-Game-Of-Life/src/music/Infected_Mushroom_Walking_On_The_Moon_Monsterca.wav")
    sound.play()

    pyglet.clock.schedule_interval(update, 1.0/frame_ps)
    pyglet.app.run()