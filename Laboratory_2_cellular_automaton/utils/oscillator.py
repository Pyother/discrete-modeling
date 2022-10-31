from .cell import Cell

class Oscilliator:

    def __init__(self, x, y):
        
        self.center = Cell(x, y)
        self.up = Cell(x, y+1)
        self.down = Cell(x, y-1)

    def __str__(self) -> str:
        print(f"Oscilliator grid coordinates: ({self.center.x}, {self.center.y})")

