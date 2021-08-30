# use pygame to show the board on a window

# dependencies
import pygame, os, sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # adds project dir to places it looks for the modules
sys.path.append(BASE_PATH)


class Window:
    def __init__(self):
        # init py game
        pygame.init()

        # width height
        self.WIDTH = 600
        self.HEIGHT = 600

        # colors
        self.COLORS = {}

    def create_window(self):
        # define window
        self.WIN = pygame.display.set_mode( (self.WIDTH, self.HEIGHT) )

        # name window
        pygame.display.set_caption("LIGHT NING")

        # logo/icon for window
        logo = pygame.image.load("images/logo.png")
        pygame.display.set_icon(logo)

    def main(self):
        # create window
        self.create_window()

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

if __name__ == "__main__":
    win = Window()

    win.main()