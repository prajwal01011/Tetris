import pygame,sys
from grid import Grid
from shapes import *

pygame.init()
dark_blue=(44,44,127)

screen=pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris in Python")

clock = pygame.time.Clock()

game_grid=Grid()

block = LBlock()


game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #drawing
    screen.fill(dark_blue)
    game_grid.draw(screen)
    block.draw(screen)

    pygame.display.update()
    clock.tick(60)
