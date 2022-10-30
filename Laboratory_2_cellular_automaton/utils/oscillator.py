from .cell import Cell

class Oscilliator:

    def __init__(self, x, y):
        
        self.center = Cell(x, y)
        self.up = self.center.y + 1
        self.down = self.center.y - 1

    def __str__(self) -> str:
        print(f"Oscilliator grid coordinates: ({self.center.x}, {self.center.y})")

