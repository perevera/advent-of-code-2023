import copy
import random
import sys
import time
from typing import Tuple, List, Dict, Any


def find_longest_one(grid: Dict[Tuple[int, int], Tuple[chr, bool, str]],
                 original: Dict[Tuple[int, int], Tuple[chr, bool, str]],
                 init: Tuple[int, int],
                 end: Tuple[int, int]) -> int:
    """
    Recursive function to find the longest path from current position, never stepping into the same tile twice
    :param grid: a copy of the original grid to work on
    :param original: the original grid
    :param init: starting point for the path search
    :param end: ending point of the path
    :param pos: current position
    :return:
    """
    x, y = init[0], init[1]
    longest = 1
    path = list()
    color_code = random_color_code()

    print(f"find_longest_one starting at {init} -> {grid[init][0]}, ending at {end} -> {grid[end][0]}...")

    while True:

        # mark the tile as stepped onto
        grid[(x, y)] = ('O', True, color_code)
        path.append((x, y))

        # get the surrounding tiles
        surroundings = []

        try:
            up = grid[(x - 1, y)]
            if up[0] not in ['#', 'v'] and not up[1]:
                grid[(x - 1, y)] = (up[0], True, up[2])
                surroundings.append((x - 1, y))
        except KeyError:
            pass

        try:
            right = grid[(x, y + 1)]
            if right[0] not in ['#', '<'] and not right[1]:
                grid[(x, y + 1)] = (right[0], True, right[2])
                surroundings.append((x, y + 1))
        except KeyError:
            pass

        try:
            down = grid[(x + 1, y)]
            if down[0] not in ['#', '^'] and not down[1]:
                grid[(x + 1, y)] = (down[0], True, down[2])
                surroundings.append((x + 1, y))
        except KeyError:
            pass

        try:
            left = grid[(x, y - 1)]
            if left[0] not in ['#', '>'] and not left[1]:
                grid[(x, y - 1)] = (left[0], True, left[2])
                surroundings.append((x, y - 1))
        except KeyError:
            pass

        if len(surroundings) == 2:
            print(f"path is {longest} steps long")
            print(f"fork at ({x}, {y})")
            # path 1
            grid_1 = copy.deepcopy(grid)
            path_1 = find_longest_one(grid_1, original, surroundings[0], end)
            print(f"path 1 is {path_1} steps long")
            # path 2
            grid_2 = copy.deepcopy(grid)
            path_2 = find_longest_one(grid_2, original, surroundings[1], end)
            print(f"path 2 is {path_2} steps long")
            # longest
            longest += max([path_1, path_2])
            print(f"returning {longest} as max of several paths")
            return longest
        elif len(surroundings) == 1:
            (x, y) = surroundings[0]
            longest += 1
        else:
            if (x, y) == end:
                print(f"returning {longest} as final path")
                return longest
            else:
                # dead end: reset this path
                return 0


def find_longest_two(grid: Dict[Tuple[int, int], Tuple[chr, bool, str]],
                     original: Dict[Tuple[int, int], Tuple[chr, bool, str]],
                     init: Tuple[int, int],
                     end: Tuple[int, int]) -> int:
    """
    Recursive function to find the longest path from current position, never stepping into the same tile twice.
    No slippery tiles now.
    :param grid: a copy of the original grid to work on
    :param original: the original grid
    :param init: starting point for the path search
    :param end: ending point of the path
    :param pos: current position
    :return:
    """
    x, y = init[0], init[1]
    longest = 1
    path = list()
    color_code = random_color_code()

    print(f"find_longest_one starting at {init} -> {grid[init][0]}, ending at {end} -> {grid[end][0]}...")

    while True:

        # mark the tile as stepped onto
        grid[(x, y)] = ('O', True, color_code)
        path.append((x, y))

        # get the surrounding tiles
        surroundings = []

        try:
            up = grid[(x - 1, y)]
            if up[0] != '#' and not up[1]:
                grid[(x - 1, y)] = (up[0], True, up[2])
                surroundings.append((x - 1, y))
        except KeyError:
            pass

        try:
            right = grid[(x, y + 1)]
            if right[0] != '#' and not right[1]:
                grid[(x, y + 1)] = (right[0], True, right[2])
                surroundings.append((x, y + 1))
        except KeyError:
            pass

        try:
            down = grid[(x + 1, y)]
            if down[0] != '#' and not down[1]:
                grid[(x + 1, y)] = (down[0], True, down[2])
                surroundings.append((x + 1, y))
        except KeyError:
            pass

        try:
            left = grid[(x, y - 1)]
            if left[0] != '#' and not left[1]:
                grid[(x, y - 1)] = (left[0], True, left[2])
                surroundings.append((x, y - 1))
        except KeyError:
            pass

        if len(surroundings) > 1:
            longest += max ([find_longest_two(copy.deepcopy(grid), original, s, end) for s in surroundings])
            print(f"longest path is: {longest}")
            return longest
        elif len(surroundings) == 1:
            (x, y) = surroundings[0]
            longest += 1
        else:
            if (x, y) == end:
                print(f"returning {longest} as final path")
                return longest
            else:
                # dead end: reset this path
                return 0


def parse_input_file(input_file: str) -> Tuple[Dict[Tuple[int, int], Tuple[chr, bool, str]], Tuple[int, int], Tuple[int, int]]:
    """
    Parse the input file to extract data. The returning grid will contain for each tiel the character indicating:
    paths (.), forest (#), and steep slopes (^, >, v, and <), and a flag to indicate if that tile has been stepped in
    before
    :param input_file:
    :return: the grid and the starting and ending points
    """
    grid = dict()
    init = (0, 0)
    end = (-1, -1)

    # Open the file in read mode
    with open(input_file, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    characters_list = [list(line.strip()) for line in lines]

    for x, chars in enumerate(characters_list):
        for y, char in enumerate(chars):
            if x == 0 and char == '.':
                init = (0, y)
            if x == len(lines) - 1 and char == '.':
                end = (len(lines) - 1, y)
            grid[(x, y)] = (char, False, '92')    # default to False and color green

    # print(grids)
    return grid, init, end


def random_color_code() -> str:
    return f'38;2;{random.randint(0, 255)};{random.randint(0, 255)};{random.randint(0, 255)}'


def print_grid(grid):
    """
    Highlight all paths tried
    :param grid:
    :return:
    """
    for x in range(max(x for x, _ in grid) + 1):
        for y in range(max(y for _, y in grid) + 1):
            cell = (x, y)
            # if grid[cell][1]:
                # print('\033[91mX', end=' ')  # Red color for True
                # print(f'\033[91m{grid[cell][0]}', end=' ')  # Red color for True
                # color_code = random_color_code()
            print(f'\033[{grid[cell][2]}m{grid[cell][0]}', end=' ')
            # else:
                # print('\033[92mX', end=' ')  # Green color for False
                # print(f'\033[92m{grid[cell][0]}', end=' ')  # Green color for False
        print('\033[0m')  # Reset color at the end of each row


def main(args) -> Tuple[int, int]:
    """
    Main function
    :return: the number of tiles that end up being energized
    """
    # record the start time
    start_time = time.time()

    if len(args) != 2:
        sys.exit(1)
        # print_help_and_exit()
    else:
        fname = args[0]
        option = int(args[1])

    # parse file
    grid, init, end = parse_input_file(fname)

    # part one ********************************************************
    # create a deep copy of the original grid
    grid_copy = copy.deepcopy(grid)
    if option == 1:
        num = find_longest_one(grid_copy, grid, init, end) - 1       # we need to remove the starting point
    elif option == 2:
        num = find_longest_two(grid_copy, grid, init, end) - 1       # we need to remove the starting point
    else:
        sys.exit(1)
    print_grid(grid)
    print(f"The longest path is: {num}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return num


if __name__ == "__main__":
    main(sys.argv[1:])
