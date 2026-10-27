from grid import Grid
from shapes import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.shapes =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_shape = self.get_random_shape()
        self.next_shape = self.get_random_shape()
        self.Game_Over = False
        self.score = 0

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
        self.update_score(rows_cleared,0)
        if self.shape_fits() == False:
            self.Game_Over = True
    
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

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_shape.draw(screen)