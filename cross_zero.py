import pygame
from enum import Enum

CELL_SIZE = 50
FPS = 60

class Cell(Enum):
    VOID = 0 #Empty cell
    CROSS = 1
    ZERO = 2

class Player:
    """Class player with type of icons and name"""
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type




class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID] * self.width for i in range(self.height)]

class GameFieldView:
    """Widget play of field and place on the screen"""

    def __init__(self, field):
        #load pictures and icons of cells
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coords_correct(self):
        return True #TODO: self._height add

    def get_coords(self, x, y):
        return x, y #TODO: decide cell

class GameRoundManager:
    """Manager of Game"""

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()


    def handle_click(self, i, j):
        player = self._players[self._current_player]
        print("click_handler", i, j)

class GameWindow:
    """Content widgets and manager of round"""
    def __init__(self):
        #initial pygame
        self._game_manager = None
        pygame.init()

        #Window
        self._width = 800
        self._height = 600
        self._title = "Crosses and Zeroes"
        self._screen = pygame.display.set_mode((self._width, self._height))
        pygame.display.set_caption(self._title)


        player1 = Player("Vasya", Cell.CROSS)
        player2 = Player("Petya", Cell.ZERO)

        self. _game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if self._field_widget.check_coords_correct():
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)

            pygame.display.flip()
            clock.tick(FPS)

def main():
    window = GameWindow()
    window.main_loop()
    print("Game Over")


if __name__ == "__main__":
    main()