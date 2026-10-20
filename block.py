from colors import Colors
class Block:
    def __init__(self,id):
        self.id=id
        self.cells={}
        self.cell_size=30
        self.rotation_state=0
        self.colors=Colors.get_cell_colors()

    def draw(self,screen):
        
