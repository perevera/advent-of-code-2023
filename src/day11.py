import sys
import time
from typing import Union, Tuple, List


def get_min_distance(grid: List[List[chr]], empty_x: List[int], empty_y: List[int], factor: int) -> int:
    """
    Get the sum of minimum distances among all galaxies
    :param grid: grid of the universe
    :param empty_x: list of empty rows (need to be expanded)
    :param empty_y: list of empty columns (need to be expanded)
    :param factor: expansion factor
    :return: sum of minimum distances among all pairs of galaxies
    """
    sum_distances = 0
    
    # get coordinates of all galaxies
    galaxies = list()   # list of coordinates for galaxies

    for x, row in enumerate(grid):
        for y, tile in enumerate(row):
            if tile == '#':
                galaxies.append((x, y))

    # for i in range(len(galaxies)):
    for i, g in enumerate(galaxies):
        g_1 = g
        for j in galaxies[i+1:]:
            g_2 = j
            # x
            if g_1[0] <= g_2[0]:
                x_1 = g_1[0]
                x_2 = g_2[0]
            else:
                x_1 = g_2[0]
                x_2 = g_1[0]
            x_extra_diff = sum(factor -1 for k in range(x_1, x_2) if k in empty_x)
            dist_x = x_2 - x_1 + x_extra_diff
            # y
            if g_1[1] <= g_2[1]:
                y_1 = g_1[1]
                y_2 = g_2[1]
            else:
                y_1 = g_2[1]
                y_2 = g_1[1]
            y_extra_diff = sum(factor - 1 for l in range(y_1, y_2) if l in empty_y)
            dist_y = y_2 - y_1 + y_extra_diff

            sum_distances += dist_x + dist_y

    return sum_distances


def get_empty(grid: List[List[chr]]) -> Tuple[List[int], List[int]]:
    """
    Get all rows and columns that are empty and will need to be expanded
    :param grid: grid of the universe
    :return: list of rows and list of columns empty
    """
    rows = list()
    columns = list()

    # get empty rows
    for i, row in enumerate(grid):
        if all(c == '.' for c in row):
            rows.append(i)

    # get empty columns
    for j, column in enumerate(zip(*grid)):
        if all(c == '.' for c in column):
            columns.append(j)

    return rows, columns


def parse_input_file(input_file: str) -> List[List[chr]]:
    """
    Process all lines from the input file to extract data
    :param input_file: input file name with path
    :return: grid of the universe
    """
    grid = []

    with open(input_file, 'r') as file:
        for line in file:
            row = [c for c in line.strip()]
            grid.append(row)

    return grid


def print_help_and_exit():
    """
    Print help and exit
    """
    print("Usage: python day11.py <expansion_factor> <input_file>")
    print("\twhere <expansion_factor> is one of: 2, 10, 100 or 1000000 and <input_file> is the input data file with path")
    sys.exit(1)


def main(args) -> int:
    """
    Main function
    :return: the total winnings
    """
    # record the start time
    start_time = time.time()

    if len(args) != 2:
        print_help_and_exit()

    # get the expansion factor
    expansion_factor = int(args[0])

    if expansion_factor not in [2, 10, 100, 1000000]:
        print_help_and_exit()

    # get the initial grid from the input file
    grid = parse_input_file(args[1])

    # get the lists of empty rows and columns
    empty_x, empty_y = get_empty(grid)

    # get the sum of minimum distances
    sum_distances = get_min_distance(grid, empty_x, empty_y, expansion_factor)
    print(f"The sum of minimum distances is: {sum_distances}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return sum_distances


if __name__ == "__main__":
    main(sys.argv[1:])
