from grid import Grid
from shapes import *
import random

class Game:
    def __init__(self):
        self.grid = Grid()
        self.shapes =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        self.current_shape = self.get_random_shape()
        self.next_shape = self.get_random_shape()

    def get_random_shape(self):
        if len (self.shapes) == 0:
            self.shapes =[IBlock(),JBlock(),LBlock(),OBlock(),SBlock(),TBlock(),ZBlock()]
        shape=random.choice(self.shapes)
        self.shapes.remove(shape)
        return shape

    def move_left(self):
        self.current_shape.move(0, -1)
        if self.shape_inside()== False:
            self.current_shape.move(0, 1)

    def move_right(self):
        self.current_shape.move(0, 1)
        if self.shape_inside()== False:
            self.current_shape.move(0, -1)


    def move_down(self):
        self.current_shape.move(1, 0)
        if self.shape_inside()== False:
            self.current_shape.move(-1, 0)



    def shape_inside(self):
        tiles = self.current_shape.get_cell_position()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True


    def draw(self, screen):
        self.grid.draw(screen)
        self.current_shape.draw(screen)