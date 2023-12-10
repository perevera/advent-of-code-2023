import sys
import time
from typing import Union, Tuple, List

# 0 -> North
# 1 -> East
# 2 -> South
# 3 -> West
move = [
    {'|': (-1, 0), 'F': (0, 1), '7': (0, -1)},          # 0: north
    {'-': (0, 1), '7': (1, 0), 'J': (-1, 0)},            # 1: east
    {'|': (1, 0), 'J': (0, -1), 'L': (0, 1)},           # 2: south
    {'-': (0, -1), 'L': (-1, 0), 'F': (1, 0)}           # 3: west
]
change = [
    {'|': 0, 'F': 1, '7': 3},                           # 0: north
    {'-': 1, '7': 2, 'J': 0},                            # 1: east
    {'|': 2, 'J': 3, 'L': 1},                           # 2: south
    {'-': 3, 'L': 0, 'F': 2}                            # 3: west
]
# direction = {'F': 1, '7': 2, 'L': 0, 'J': 3}

def traverse_loop(grid, start, backwards=False) -> int:
    """
    Extrapolate values for all grid then sum up those values
    :param grid: list of grid (lists) of integers
    :return: sum of extrapolated values
    """
    print(f"Traversing the loop...")

    length = 0

    next_tile = tuple()

    # search the next tile from the start
    if grid[start[0] -1][start[1]] in move[0]:
        d = 0
        next_tile = (start[0] - 1,start[1])
    elif grid[start[0]][start[1] + 1] in move[1]:
        d = 1
        next_tile = (start[0], start[1] + 1)
    elif grid[start[0] + 1][start[1]] in move[2]:
        d = 2
        next_tile = (start[0] + 1, start[1])
    elif grid[start[0] - 1][start[1] + 1] in move[3]:
        d = 3
        next_tile = (start[0], start[1] - 1)

    print(next_tile)

    while True:
        length += 1
        symbol = grid[next_tile[0]][next_tile[1]]
        print(symbol)
        if symbol == 'S':
            break
        next_tile = (next_tile[0] + move[d][symbol][0], next_tile[1] + move[d][symbol][1])
        d = change[d][symbol]


    farthest = length // 2

    return farthest


def parse_input_file(input_file: str):
    """
    Process all lines from the input file to extract data
    :param input_file: input file name with path
    :return:
    """
    grid = []
    start = tuple()
    
    with open(input_file, 'r') as file:
        for i, line in enumerate(file):
            if 'S' in line:
                start = (i, line.index('S'))
            grid.append([s for s in line.strip()])

    return grid, start


def print_help_and_exit():
    """
    Print help and exit
    """
    print("Usage: python day10.py <part_number> <input_file>")
    print("\twhere <part_number> is one of: 1, 2 and <input_file> is the input data file with path")
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

    part_number = int(args[0])

    grid, start = parse_input_file(args[1])

    # DEBUG
    print(grid)

    if part_number == 1:
        farthest = traverse_loop(grid, start)
    # elif part_number == 2:
    #     sum_vals = traverse_loop(grid, backwards=True)
    # else:
    #     print_help_and_exit()

    # DEBUG
    print(f"The farthest point of the loop is at {farthest} steps")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return farthest


if __name__ == "__main__":
    main(sys.argv[1:])
