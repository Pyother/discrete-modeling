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
        self.total_time = 0.0
            
        for row in range(ROW_COUNT):
            
            self.cells.append([])
            for column in range(COLUMN_COUNT):
                self.cells[row].append(cll.Cell(row, column))
                self.cells[row][column].__str__() 

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

    def on_update(self, delta_time):
        
        self.total_time += delta_time
        seconds = int(self.total_time) % 60

class InstructionView(arcade.View):

    def on_draw(self):
        
        self.clear()
        arcade.draw_text("Cellular Automata", self.window.width / 2, self.window.height / 2,
                         arcade.color.WHITE, font_size=40, anchor_x="center")
        arcade.draw_text("Click to advance", self.window.width / 2, self.window.height / 2-75,
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