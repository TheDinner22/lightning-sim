# represent the "board" in code

# dependencies
import random

class Board:
    def __init__(self, width=10):
        self.width = width
        self.height = width * 2

        self.WALL_CHANCE = .25
        self.FLOOR_CHANCE = .15

        # create the grid
        self.create_random_grid()

    def create_random_grid(self):
        # reset old grid
        self.grid = []

        # generate cells for new grid
        for i in range(self.width * self.height):
            # is the cell at the left, right, top, or bottom?
            is_left = True if i % self.width == 0 else False
            is_right = True if i % self.width == self.width-1 else False
            is_top = True if i < self.width else False
            is_bottom = True if i > (self.width * self.height - self.width) else False

            # create the cell
            cell = {
                "left" : is_left,
                "right" : is_right,
                "roof" : is_top,
                "floor" : is_bottom,
                "ID" : i
            }

            # append to grid
            self.grid.append(cell)

        # randomly generate walls
        total = self.width * self.height 
        horizontal_amount = int(total * self.FLOOR_CHANCE)
        verticle_amount = int(total * self.WALL_CHANCE)

        # generate the walls
        for _i in range(verticle_amount):
            random_index = random.randrange(0, total)

            adding_num = -1 if random_index == total - 1 else 1
            first = "right" if adding_num == 1 else "left"
            second = "right" if first == "left" else "left"
            
            self.grid[random_index][first] = True
            self.grid[random_index + adding_num][second] = True

        # generate the floors
        for _i in range(horizontal_amount):
            random_index = random.randrange(0, total)

            adding_num = self.width * -1 if random_index > (total - self.width) else self.width
            first = "floor" if adding_num == self.width else "roof"
            second = "floor" if first == "roof" else "roof"

            self.grid[random_index][first] = True
            self.grid[random_index + adding_num - 1][second] = True


    def can_move_from(self, cell_index):
        # TODO this works but its a lot of repeated code. Can it be made better?

        # can you move left
        can_move_left = False
        is_left = True if cell_index % self.width == 0 else False
        if not is_left and self.grid[cell_index]["left"] == False:
            left_cell = self.grid[cell_index - 1]
            is_wall_left = True if left_cell["right"] == True else False
            can_move_left = True if not is_wall_left else False

        # can you move right
        can_move_right = False
        is_right = True if cell_index % self.width == self.width-1 else False
        if not is_right and self.grid[cell_index]["right"] == False:
            right_cell = self.grid[cell_index + 1]
            is_wall_right = True if right_cell["left"] == True else False
            can_move_right = True if not is_wall_right else False
 
        # can you move up
        can_move_up = False
        is_top = True if cell_index < self.width else False
        if not is_top and self.grid[cell_index]["roof"] == False:
            top_cell = self.grid[cell_index - self.width]
            is_wall_top = True if top_cell["floor"] == True else False
            can_move_up = True if not is_wall_top else False

        # can you move down
        can_move_down = False
        is_bottom = True if cell_index > (self.width * self.height - self.width) else False
        if not is_bottom and self.grid[cell_index]["floor"] == False:
            bottom_cell = self.grid[cell_index + self.width]
            is_wall_bottom = True if bottom_cell["roof"] == True else False
            can_move_down = True if not is_wall_bottom else False

        # return the results
        return can_move_left, can_move_right, can_move_up, can_move_down

    def BFS(self):
        """breadth first search to find the quickest way to the bottom"""
        start_i = random.randrange(0,self.width)
        paths = [ [start_i] ]
        solved = False
        dead_ends = []

        while not solved:
            for path in paths:
                # find all possibles moves from path
                if len(dead_ends) >= len(paths) or len(paths) > 10000: # TODO this solution sucks
                    return False, False

                # NOTE order is left right up down
                if path[-1] >= (self.width * self.height - self.width):
                    solved = True
                    return paths, paths.index(path)

                possible_moves = self.can_move_from(path[-1])

                if True in possible_moves:
                    move_order = [-1, 1, (self.width) * -1, self.width]
                    first_append_flag = False
                    origonal_path = path.copy()
                    for i in range(4):
                        possible_move = possible_moves[i]
                        if possible_move:
                            move = move_order[i]

                            next_index = origonal_path[-1] + move
                            if not next_index in origonal_path:

                                if not first_append_flag:
                                    path.append(next_index)
                                    first_append_flag = True
                                else:
                                    new_path = origonal_path.copy()
                                    new_path.append(next_index)
                                    paths.append(new_path)
                    if not first_append_flag:
                        dead_ends.append(paths.index(path))
                else:
                    dead_ends.append(paths.index(path))



    def pretty_print_BFS(self, path):
        for i in range(self.width * self.height):
            cell = self.grid[i]
            in_path = True if cell["ID"] in path else False

            number_str = str(i)

            if len(number_str) == 1:
                number_str += "  "
            elif len(number_str) == 2:
                number_str += " "
            
            end_str = "\n" if i % self.width == self.width-1 else " "

            if in_path:
                print('\033[92m' + number_str + '\033[0m', end=end_str)
            else:
                print(number_str, end=end_str)
        print(path)




if __name__ == "__main__":
    b = Board(10)

    paths, index = b.BFS()

    if paths and index:
        b.pretty_print_BFS(paths[index])
    else:
        print('ljfdsakfdl')

    # can_move_left, can_move_right, can_move_up, can_move_down = b.can_move_from(0)

    # print("can_move_left ", can_move_left)
    # print("can_move_right ", can_move_right)
    # print("can_move_up ", can_move_up)
    # print("can_move_down ", can_move_down)
