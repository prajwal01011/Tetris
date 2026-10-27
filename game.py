from grid import Grid
from shapes import *
import random
import pygame

class Game:
    def __init__(self):
        self.grid = Grid()
        self.shapes =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_shape = self.get_random_shape()
        self.next_shape = self.get_random_shape()
        self.Game_Over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound("sounds/clear.ogg")
        self.Game_Over_sound = pygame.mixer.Sound("sounds/game_over.ogg")
        
        pygame.mixer.music.load("sounds/music.ogg")
        pygame.mixer.music.play(-1)

    def update_score(self,lines_cleared,move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared >= 3:
            self.score += 500
        self.score += move_down_points

    def get_random_shape(self):
        if len (self.shapes) == 0:
            self.shapes =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        shape=random.choice(self.shapes)
        self.shapes.remove(shape)
        return shape

    def move_left(self):
        self.current_shape.move(0, -1)
        if self.shape_inside()== False or self.shape_fits() == False:
            self.current_shape.move(0, 1)

    def move_right(self):
        self.current_shape.move(0, 1)
        if self.shape_inside()== False or self.shape_fits() == False:
            self.current_shape.move(0, -1)


    def move_down(self):
        self.current_shape.move(1, 0)
        if self.shape_inside()== False or self.shape_fits() == False:
            self.current_shape.move(-1, 0)
            self.lock_shape()

    def lock_shape(self):
        tiles = self.current_shape.get_cell_position()
        for position in tiles:
            self.grid.grid[position.row] [position.column] = self.current_shape.id
        self.current_shape = self.next_shape
        self.next_shape = self.get_random_shape()
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared,0)
        if self.shape_fits() == False:
            self.Game_Over = True
            self.Game_Over_sound.play()
    
    def reset(self):
        self.grid.reset()
        self.shapes =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_shape = self.get_random_shape()
        self.next_shape = self.get_random_shape()
        self.score = 0

    def shape_fits(self):
        tiles = self.current_shape.get_cell_position()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True




    def shape_inside(self):
        tiles = self.current_shape.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_shape.rotate()
        if self.shape_inside() == False or self.shape_fits() == False:
            self.current_shape.undo_rotation()
        else:
            self.rotate_sound.play()

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_shape.draw(screen, 11, 11)
        if self.next_shape.id == 3:
            self.next_shape.draw(screen, 255, 290)
        elif self.next_shape.id ==4:
            self.next_shape.draw(screen, 255, 280)
        else:
            self.next_shape.draw(screen, 270, 270)