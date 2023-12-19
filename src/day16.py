import sys
import time
from typing import Union, Tuple, List
from enum import Enum


def recurse_find_one(row: list, i_1, i_2):
    """
    Recursive function to assert all rows/columns are mirrored (but one last at the end, maybe)
    :param row:
    :param i_1:
    :param i_2:
    :return:
    """
    if i_1 < 0 or i_2 >= len(row):
        return True
    else:
        if row[i_1] == row[i_2]:
            if i_1 == 0 or i_2 == len(row) - 1:
                return True
            else:
                return recurse_find_one(row, i_1 - 1, i_2 + 1)
        else:
            return False


def recurse_find_two(row: list, i_1, i_2):
    """
    Recursive function to assert all rows/columns are mirrored (but one last at the end, maybe)
    :param row:
    :param i_1:
    :param i_2:
    :return:
    """
    if i_1 < 0 or i_2 >= len(row):
        return True
    else:
        # if row[i_1] == row[i_2]:
        diffs = [(i, one, another) for i, (one, another) in enumerate(zip(row[i_1], row[i_2]))
                 if one != another]
        if len(diffs) <= 1:
            if i_1 == 0 or i_2 == len(row) - 1:
                return True
            else:
                return recurse_find_two(row, i_1 - 1, i_2 + 1)
        else:
            return False


def find_reflection_one(grid: List[List[str]], i: int) -> int:
    """
    Process all grids to get the final result
    :param grid:
    :param i:
    :return:
    """
    # print(f"Looking for reflections on grid #{i}...")

    zipped_data = list(zip(*grid))

    # look for vertical reflection
    for j in range(len(grid) - 1):
        if grid[j] == grid[j + 1]:
            # print(f"rows {j} and {j+1} are alike...")
            if recurse_find_one(grid, j - 1, j + 2):
                # print("and there is perfect reflection")
                return (j + 1) * 100
            # else:
            #     print("but there is no perfect reflection")

    # look for horizontal reflection
    for j in range(len(zipped_data) - 1):
        if zipped_data[j] == zipped_data[j + 1]:
            # print(f"columns {j} and {j+1} are alike...")
            if recurse_find_one(zipped_data, j - 1, j + 2):
                # print("and there is perfect reflection")
                return j + 1
            # else:
            #     print("but there is no perfect reflection")


def find_reflection_two(grid: List[List[str]], i: int) -> int:
    """
    Process all grids to get the final result
    :param grid:
    :param i:
    :return:
    """
    # print(f"Looking for reflections on grid #{i}...")

    zipped_data = list(zip(*grid))

    # # first pass looking for vertical reflection
    # for j in range(len(grid) - 1):
    #     if grid[j] == grid[j + 1]:
    #         if recurse_find_two(grid,  j - 1, j + 2):
    #             return (j + 1) * 100

    # second pass looking for vertical reflection
    # for j in range(len(grid) - 1):
    for j in range(len(grid) - 1, -1, -1):
        diffs = [(i, one, another) for i, (one, another) in enumerate(zip(grid[j-1], grid[j])) if one != another]
        if len(diffs) == 0:
            if recurse_find_two(grid, j - 2, j + 1):
                return (j + 1) * 100
        elif len(diffs) == 1:
            if recurse_find_one(grid, j - 2, j + 1):
                return (j + 1) * 100

        # if len(diffs) <= 1:
        #     if recurse_find_two(grid, j - 1, j + 2):
        #         return (j + 1) * 100

    # # first pass looking for horizontal reflection
    # for j in range(len(zipped_data) - 1):
    #     if zipped_data[j] == zipped_data[j + 1]:
    #         if recurse_find_two(zipped_data, j - 1, j + 2):
    #             return j + 1

    # second pass looking for horizontal reflection
    # for j in range(len(zipped_data) - 1):
    for j in range(len(zipped_data) - 1, -1, -1):
        diffs = [(i, one, another) for i, (one, another) in enumerate(zip(zipped_data[j-1], zipped_data[j]))
                 if one != another]
        if len(diffs) == 0:
            if recurse_find_two(zipped_data, j - 2, j + 1):
                return j + 1
        elif len(diffs) == 1:
            if recurse_find_one(zipped_data, j - 2, j + 1):
                return j + 1
        # if len(diffs) <= 1:
        #     if recurse_find_two(zipped_data, j - 1, j + 2):
        #         return j + 1


def count_recursive(grid: dict(), coord_1: Tuple[int, int], vector: Tuple[int, int]) -> int:
    """
    Follow a beam within the grid and count all newly energized tiles
    :param grid: the grid
    :param coord_1: the coordinates of the initial tile
    :param vector: the vector giving the moving direction, these are
        (0, 1) -> right
        (1, 0) -> down
        (0, -1) -> left
        (-1, 0) -> up
    :return: the num of new tiles energized
    """
    print(f"Executing function: {id(count_recursive)} for coord {coord_1} - vector {vector}")

    num = 0     # to sum up all energized tiles
    coord_ini = coord_1  # store the initial coordinates
    # coord_n = tuple(x + y for x, y in zip(coord_1, vector))         # move to the next tile
    coord_n = coord_1

    while coord_n:

        try:
            print(f"coord: {coord_n}, symbol: {grid[coord_n][0]}, energized?: {grid[coord_n][1]}")

            # end recursion here as the loop is closed
            if grid[coord_n][0] == 'X':
                return num

            # energize the tile if not yet done and increment the sum
            if not grid[coord_n][1]:
                grid[coord_n] = (grid[coord_n][0], True)
                num += 1

            # move to the next tile
            if grid[coord_n][0] == '.':                       # keep direction
                pass
            elif grid[coord_n][0] == '-' and vector[0] == 0:     # keep direction
                pass
            elif grid[coord_n][0] == '|' and vector[1] == 0:     # keep direction
                pass
            elif grid[coord_n][0] == '/' and vector == (-1, 0):    # going up, turn right
                vector = (0, 1)
            elif grid[coord_n][0] == '\\' and vector == (-1, 0):   # going up, turn left
                vector = (0, -1)
            elif grid[coord_n][0] == '/' and vector == (1, 0):     # going down, turn left
                vector = (0, -1)
            elif grid[coord_n][0] == '\\' and vector == (1, 0):    # going down, turn right
                vector = (0, 1)
            elif grid[coord_n][0] == '/' and vector == (0, -1):    # going left, turn down
                vector = (1, 0)
            elif grid[coord_n][0] == '\\' and vector == (0, -1):   # going left, turn up
                vector = (-1, 0)
            elif grid[coord_n][0] == '/' and vector == (0, 1):  # going right, turn up
                vector = (-1, 0)
            elif grid[coord_n][0] == '\\' and vector == (0, 1):  # going right, turn down
                vector = (1, 0)
            elif grid[coord_n][0] == '-' and vector[1] == 0:     # split in two beams
                print("split in two beams...")
                # mark the tile for avoiding infinite splits
                grid[coord_n] = ('X', grid[coord_n][1])
                # n_1 = count_recursive(grid, coord_n, (0, -1))
                # n_2 = count_recursive(grid, coord_n, (0, 1))
                num += (count_recursive(grid, (coord_n[0], coord_n[1] - 1), (0, -1)) +
                        count_recursive(grid, (coord_n[0], coord_n[1] + 1), (0, 1)))
                return num
            elif grid[coord_n][0] == '|' and vector[0] == 0:     # split in two beams
                print("split in two beams...")
                # mark the tile for avoiding infinite splits
                grid[coord_n] = ('X', grid[coord_n][1])
                # n_1 = count_recursive(grid, coord_n, (1, 0))
                # n_2 = count_recursive(grid, coord_n,  (-1, 0))
                num += (count_recursive(grid, (coord_n[0] + 1, coord_n[1]), (1, 0)) +
                        count_recursive(grid, (coord_n[0] - 1, coord_n[1]),  (-1, 0)))
                return num

        except KeyError:      # the beam goes out of bounds, return current sum
            return num

        coord_n = tuple(x + y for x, y in zip(coord_n, vector))     # move to the next tile


def parse_input_file(input_file: str) -> dict:
    """
    Parse the input file to extract data
    :param input_file:
    :return:
    """
    grid = dict()

    # Open the file in read mode
    with open(input_file, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    characters_list = [list(line.strip()) for line in lines]

    for x, chars in enumerate(characters_list):
        for y, char in enumerate(chars):
            grid[(x, y)] = (char, False)

    # Map lines to a list of characters
    # for x, line in enumerate(lines):
    #     for y in list(map(chr, line)):
    #         grid.append((x, y, False))

    # print(grids)
    return grid


def main(args) -> int:
    """
    Main function
    :return: the number of tiles that end up being energized
    """
    # record the start time
    start_time = time.time()

    if len(args) != 1:
        sys.exit(1)
        # print_help_and_exit()

    grid = parse_input_file(args[0])

    # part one ********************************************************

    # determine the initial vector of movement
    # vector = (1, 0) if grid[(0, 0)][0] == '\\' else (0, 1)
    vector = (0, 1)
    # call the recursive function, sum up one for the initial tile
    num = count_recursive(grid, (0, 0), vector)
    print(f"The number of tiles that end up being energized is {num}")

    # part two ********************************************************

    # starting on the left side
    # for x in range(len(grid)):


    # starting on the top side

    # starting on the right side

    # starting on the bottom side


    # tuple_range = list(zip(range(start, end), range(start + 1, end + 1)))


    # tot_1 = 0
    # tot_2 = 0
    # for i, grid in enumerate(grids):
    #     tot_1 += find_reflection_one(grid, i)
    #     # DEBUG
    #     r_2 = find_reflection_two(grid, i)
    #     print(f"grid #{i}, value = {r_2}")
    #     tot_2 += r_2
    # print(f"Total points: {tot_1} and {tot_2}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return num


if __name__ == "__main__":
    main(sys.argv[1:])
