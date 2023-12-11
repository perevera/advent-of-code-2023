import sys
import time
# from shapely.geometry import Point, Polygon
import numpy as np
from typing import Union, Tuple, List

# 0 -> North
# 1 -> East
# 2 -> South
# 3 -> West
move = [
    {'|': (-1, 0), 'F': (0, 1), '7': (0, -1)},  # 0: north
    {'-': (0, 1), '7': (1, 0), 'J': (-1, 0)},  # 1: east
    {'|': (1, 0), 'J': (0, -1), 'L': (0, 1)},  # 2: south
    {'-': (0, -1), 'L': (-1, 0), 'F': (1, 0)}  # 3: west
]
change = [
    {'|': 0, 'F': 1, '7': 3},  # 0: north
    {'-': 1, '7': 2, 'J': 0},  # 1: east
    {'|': 2, 'J': 3, 'L': 1},  # 2: south
    {'-': 3, 'L': 0, 'F': 2}  # 3: west
]
# this dictionary is to replace the 'S' from the first tile, the keys are tuples (start_direction, end_direction)
start_tile = {
    (0, 0): '|',
    (0, 1): 'J',
    (0, 3): 'L',
    (1, 0): 'F',
    (1, 1): '-',
    (1, 2): 'L',
    (2, 1): '7',
    (2, 2): '|',
    (2, 3): 'F',
    (3, 0): '',
    (3, 2): 'J',
    (3, 3): '-',
}

# direction = {'F': 1, '7': 2, 'L': 0, 'J': 3}


def traverse_loop(grid: List[List[int]], start: Tuple[int, int]) -> Tuple[int, List[Tuple[int, int]], List[Tuple[int, int]]]:
    """
    Extrapolate values for all grid then sum up those values
    :param grid: list of grid (lists) of integers
    :param start:
    :return: sum of extrapolated values
    """
    print(f"Traversing the loop...")

    length = 0
    polygon_vertices = [start]
    next_tile = tuple()
    loop = list()   # list of points (tuples) that make up the loop

    # search the next tile from the start
    if grid[start[0] - 1][start[1]] in move[0]:
        d = 0
        next_tile = (start[0] - 1, start[1])
    elif grid[start[0]][start[1] + 1] in move[1]:
        d = 1
        next_tile = (start[0], start[1] + 1)
    elif grid[start[0] + 1][start[1]] in move[2]:
        d = 2
        next_tile = (start[0] + 1, start[1])
    elif grid[start[0] - 1][start[1] + 1] in move[3]:
        d = 3
        next_tile = (start[0], start[1] - 1)

    # store the initial point of the loop
    loop.append(start)

    # store the initial direction
    start_direction = d

    # print(next_tile)

    while True:
        length += 1
        symbol = grid[next_tile[0]][next_tile[1]]
        loop.append(next_tile)
        # print(symbol)
        if symbol == 'S':   # the loop ends here
            grid[next_tile[0]][next_tile[1]] = start_tile[(start_direction, d)]
            break
        new_tile = (next_tile[0] + move[d][symbol][0], next_tile[1] + move[d][symbol][1])
        new_d = change[d][symbol]
        if new_d != d:  # on every change of direction, store a new vertice of the enclosing polygon
            polygon_vertices.append(next_tile)
            d = new_d
        next_tile = new_tile

    farthest = length // 2

    print(f"Steps to the farthest tile of the loop: {farthest}")

    return farthest, polygon_vertices, loop


# def is_point_inside_polygon(x: int, y: int, polygon: List[Tuple[int, int]]) -> bool:
#     """
#     Check if a point is inside a polygon
#     :param x:
#     :param y:
#     :param polygon:
#     :return: True of False
#     """
#     # Ray Casting Algorithm
#     n = len(polygon)
#     inside = False
#     p1x, p1y = polygon[0]
#     for i in range(n + 1):
#         p2x, p2y = polygon[i % n]
#         if y > min(p1y, p2y):
#             if y <= max(p1y, p2y):
#                 if x <= max(p1x, p2x):
#                     if p1y != p2y:
#                         xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
#                     if p1x == p2x or x <= xints:
#                         inside = not inside
#         p1x, p1y = p2x, p2y
#
#     return inside

def count_points_by_row(row: List[chr], x: int, loop: List[Tuple[int, int]]) -> int:
    """
    Check if a point is inside the pipe
    :param row:
    :param x:
    :param loop:
    :return: number of points inside the pipe on this row
    """
    count = 0
    is_inside = False
    prev_curve = '*'

    for y in range(len(row)):
        if (x, y) not in loop:
            if is_inside:
                count += 1
        else:
            if row[y] == '|':
                is_inside = not is_inside
            if row[y] == 'F' or row[y] == 'L':
                prev_curve = row[y]
            if row[y] == '7' and prev_curve == 'F':
                prev_curve = '*'
            if row[y] == 'J' and prev_curve == 'L':
                prev_curve = '*'
            if row[y] == '7' and prev_curve == 'L':
                is_inside = not is_inside
            if row[y] == 'J' and prev_curve == 'F':
                is_inside = not is_inside

    return count


def count_points(loop: List[Tuple[int, int]], grid: List[List[int]]) -> int:
    """
    Count all points inside the polygon
    :param polygon:
    :param loop:
    :param grid:
    :return: Number of points inside the polygon
    """
    print(f"Counting points inside the polygon...")

    count_inside_polygon = 0

    for x in range(len(grid)):
        count_inside_polygon += count_points_by_row(grid[x], x, loop)

    print(f"Number of points inside the polygon: {count_inside_polygon}")

    return count_inside_polygon


def parse_input_file(input_file: str) -> List[List[chr]]:
    """
    Process all lines from the input file to extract data
    :param input_file: input file name with path
    :return:
    """
    grid = []
    galaxy_num = 1

    with open(input_file, 'r') as file:
        for line in file:
            row = [c for c in line]
            for i, c in enumerate(row):
                if c == '#':
                    row[i] = chr(galaxy_num)
                    galaxy_num += galaxy_num
            grid.append(row)

    return grid


def print_help_and_exit():
    """
    Print help and exit
    """
    print("Usage: python day11.py <input_file>")
    print("\twhere <input_file> is the input data file with path")
    sys.exit(1)


def main(args) -> int:
    """
    Main function
    :return: the total winnings
    """
    # record the start time
    start_time = time.time()

    if len(args) != 1:
        print_help_and_exit()

    grid = parse_input_file(args[0])

    # DEBUG
    print(grid)

    # farthest, polygon, loop = traverse_loop(grid, start)
    # count_points_inside = count_points(loop, grid)
    #
    # # DEBUG
    # print(f"The farthest point of the loop is at {farthest} steps")
    # print(f"The number of tiles enclosed by the loop is: {count_points_inside}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return -1

    # return farthest, count_points_inside


if __name__ == "__main__":
    main(sys.argv[1:])
