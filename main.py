import pygame,sys
from game import Game


pygame.init()
dark_blue=(44,44,127)

screen=pygame.display.set_mode((300,600))
pygame.display.set_caption("Tetris in Python")

clock = pygame.time.Clock()

game = Game()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.Game_Over == True:
                game.Game_Over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.Game_Over == False :
                game.move_left()
            if event.key == pygame.K_RIGHT and game.Game_Over == False :
                game.move_right()
            if event.key == pygame.K_DOWN and game.Game_Over == False :
                game.move_down()
            if event.key == pygame.K_UP and game.Game_Over == False :
                game.rotate()
        if event.type == GAME_UPDATE and game.Game_Over == False :
            game.move_down()

    #drawing
    screen.fill(dark_blue)
    game.draw(screen)
    


    pygame.display.update()
    clock.tick(60)
