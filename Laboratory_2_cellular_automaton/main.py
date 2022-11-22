import arcade
import time
import utils.oscillator as osc
import utils.cell as cll

ROW_COUNT = 25
COLUMN_COUNT = 25
WIDTH = 25
HEIGHT = 25
MARGIN = 1
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Cellular Automata"
TYPE = "oscilliator"

class GameView(arcade.View):

    def __init__(self):

        super().__init__()

        self.cells = []
        self.new_cells= []
        self.total_time = 0.0
            
        for row in range(ROW_COUNT):
            self.cells.append([])
            self.new_cells.append([])
            for column in range(COLUMN_COUNT):
                self.cells[row].append(cll.Cell(row, column))
                self.new_cells[row].append(cll.Cell(row, column))

    def on_draw(self):

        self.clear()

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                
                if self.cells[row][column].value == 1:
                    color = arcade.color.CAROLINA_BLUE
                else:
                    color = arcade.color.BLACK

                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
            
    def on_mouse_press(self, x, y, button, modifiers):

        column = int(x // (WIDTH + MARGIN))
        row = int(y // (HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({column}, {row})")

        if row < ROW_COUNT and column < COLUMN_COUNT:

            if TYPE == "oscilliator":

                if self.cells[row][column].value == 0:

                    self.cells[row][column].fill()
                    self.cells[row-1][column].fill()    
                    self.cells[row+1][column].fill()
        
                else:
                    self.cells[row][column].empty()

    def cell_check(cell, row, column):

        position = []
        if row-1 >= 0 and column-1 >= 0: position.append(cell[row-1][column-1])
        if row-1 >= 0: position.append(cell[row-1][column])
        if row-1 >= 0 and column+1 <= 24: position.append(cell[row-1][column+1])
        if column+1 <= 24:position.append(cell[row][column+1])
        if row+1 <= 24 and column <= 24: position.append(cell[row+1][column+1])
        if row+1 <= 24: position.append(cell[row+1][column])
        if row+1 <= 24 and column-1 >= 0: position.append(cell[row+1][column-1])
        if column-1 >=0: position.append(cell[row][column-1])
        
        counter = 0
        for i in len(position):
            if position[i].value == 1:
                counter += counter
                
        if cell[row][column].value == 0:
            if counter <= 2: 
                return(0)
            else: 
                return(1) 
        else:
            if counter <= 1: return(0)
            elif counter == 2 or counter == 3: return(1)
            else: return(0)
        
    def on_key_press(self, key, modifiers):

        if key == arcade.key.SPACE:
            for rows in range(ROW_COUNT):
                for columns in range(COLUMN_COUNT):
                    self.cells[rows][columns].empty()
        
        if key == arcade.key.ESCAPE:
            arcade.exit()

class InstructionView(arcade.View):

    def on_draw(self):
        
        self.clear()
        arcade.draw_text("Cellular Automata", self.window.width / 2, self.window.height / 2+70,
                         arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-50,
                         arcade.color.WHITE, font_size=15, anchor_x="center")
        arcade.draw_text("Press SPACE to do next move", self.window.width / 2, self.window.height / 2-100,
                         arcade.color.WHITE, font_size=15, anchor_x="center")
        arcade.draw_text("Press ESCAPE to exit", self.window.width / 2, self.window.height / 2-150,
                         arcade.color.WHITE, font_size=15, anchor_x="center")

    def on_show_view(self):

        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)
        arcade.set_viewport(0, self.window.width, 0, self.window.height)
            
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        
        game_view = GameView()
        self.window.show_view(game_view)
    
def main():

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()