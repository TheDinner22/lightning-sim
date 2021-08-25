# represent the "board" in code

# dependencies
import random

class Board:
    def __init__(self, width=10):
        self.width = width
        self.height = width * 2

        self.WALL_CHANCE = .45
        self.FLOOR_CHANCE = .2

        # create the grid
        self.grid = []
        self.create_random_grid()


    def create_random_grid(self):
        # reset old grid
        self.grid = []

        # generate new grid
        for i in range(self.width * self.height):
            # randomly generat cell walls/floors
            rand_val = random.randint(1,100)/100
            left = True if rand_val <= self.WALL_CHANCE else False

            rand_val = random.randint(1,100)/100
            right = True if rand_val <= self.WALL_CHANCE else False

            rand_val = random.randint(1,100)/100
            floor = True if rand_val <= self.FlOOR_CHANCE else False

            rand_val = random.randint(1,100)/100
            roof = True if rand_val <= self.FlOOR_CHANCE else False

            # assign walls and floors to cell
            cell = {
                "left" : left,
                "right" : right,
                "floor" : floor,
                "roof" : roof
            }

            # if cell needs wall to make grid closed, add it
            # this way there are no holes on the edges of the grid

            #
            #
            #
            #

            # add cell to grid
            self.grid.append(cell)



