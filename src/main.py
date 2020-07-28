import pygame
from game import create_board

width, height =  1000, 700
size = (width, height)

pygame.init()
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
FPS = 60 

# set screen size
screen = pygame.display.set_mode(size)

# colors
black = (0,0,0)
white = (255,255,255)

create_board(width, height)

# create event loop
run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        # if press window close button
        # without this it doesn't stop the game
        if event.type == pygame.QUIT:
            run = False
        
    screen.fill(white)
    pygame.display.update()


pygame.quit()