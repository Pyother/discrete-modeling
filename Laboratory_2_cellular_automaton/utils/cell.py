class Cell:

    def __init__(self, x, y):
        
        self.value = 0
        self.x = x
        self.y = y
    
    def empty(self):

        self.value = 0

    def fill(self):

        self.value = 1


    def __str__(self) -> str:
        print(f"Cell coordinates: ({self.x}, {self.y}) | Cell value: ({self.value})")

