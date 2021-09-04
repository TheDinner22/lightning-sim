# use pygame to show the board on a window

# dependencies
import pygame, random

class Window:
    def __init__(self, board):
        # init py game
        pygame.init()

        # width height
        self.WIDTH = 600
        self.HEIGHT = 600

        # diffenet display modes
        self.display_one = False
        self.display_all = False

        # place holder
        self.solution = []
        self.display_all_c = 0

        # the board to display on the window
        self.board = board

        # define the dimensions of the cells of the board
        self.cell_width = self.WIDTH // self.board.width

        # define the left padding for the grid
        total_width = self.cell_width * self.board.width
        self.left_padding = (self.WIDTH - total_width) // 2


        # colors
        self.COLORS = {
            "BLACK" : (255, 255, 255),
            "GREY" : (230, 230, 230),
            "BLUE" : (0, 0, 255),
            "RED" : (255, 0, 0),
            "YELLOW" : (212, 175, 55) 
        }

    def create_random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def create_window(self):
        # define window
        self.WIN = pygame.display.set_mode( (self.WIDTH, self.HEIGHT) )

        # name window
        pygame.display.set_caption("LIGHT NING")

        # logo/icon for window
        logo = pygame.image.load("images/logo.png")
        pygame.display.set_icon(logo)

    def get_BFS(self):
        solved = False
        while not solved:
            self.board.create_random_grid()
            paths, index = self.board.BFS()

            if paths != False and index != False:            
                self.solution = paths[index]
                solved = True

                self.paths = paths
                self.solution_i = index

    def draw_grid_solution(self):
        fflag = True
        for i in range(self.board.width * self.board.height):
            if not i in self.solution: continue

            # might not work
            col_num = i % self.board.width
            row_num = i // self.board.width

            x_pos = self.left_padding + (col_num * self.cell_width)
            y_pos = row_num * self.cell_width

            # define rect
            r = pygame.Rect(x_pos, y_pos, self.cell_width, self.cell_width)

            # draw the rectangle
            pygame.draw.rect(self.WIN, self.COLORS["YELLOW"], r)

    def draw_BFS(self):
        if self.display_all_c >= len(self.paths):
            self.display_all_c = 0

        # generate a color for each path
        path_colors = []
        for path in self.paths:
            path_colors.append(self.create_random_color())
        path_colors[-1] = (0, 0 ,0)

        temp = self.paths.pop(self.display_all_c)
        self.paths.append(temp)

        for path in self.paths:
            for i in path:
                # might not work
                col_num = i % self.board.width
                row_num = i // self.board.width

                x_pos = self.left_padding + (col_num * self.cell_width)
                y_pos = row_num * self.cell_width

                # define rect
                r = pygame.Rect(x_pos, y_pos, self.cell_width, self.cell_width)

                # draw the rectangle
                pygame.draw.rect(self.WIN, path_colors[self.paths.index(path)], r)

        self.display_all_c += 1
        
                
    def draw_window(self):
        self.WIN.fill(self.COLORS["GREY"])

        if self.display_one:
            self.draw_grid_solution()
        elif self.display_all:
            self.draw_BFS()

        pygame.display.update()

    def main(self):
        # create window
        self.create_window()

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.get_BFS()
                    elif event.key == pygame.K_1:
                        # toggle display one
                        self.display_one = not self.display_one
                        if self.display_one:
                            self.display_all = False
                    elif event.key == pygame.K_2:
                        # toggle display all
                        self.display_all = not self.display_all
                        if self.display_all:
                            self.display_all_c = 0
                            self.display_one = False
            
            self.draw_window()

if __name__ == "__main__":
    win = Window()

    win.main()