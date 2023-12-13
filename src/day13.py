import sys
import time
from typing import Union, Tuple, List

# 1. part - What is the sum of possible arrangements?
# def recursive_arrangement(p, g, springs, groups):
#     """
#     Recursive function to count all different arrangements of groups of damaged springs that match the requirement
#     :param spring_i: position where to start the search in the array of springs
#     :param group_i: index of the group we are trying to arrange
#     :param springs: array of springs
#     :param groups: list of sizes of groups of damaged spring
#     :return:
#     """
#     if g >= len(groups):  # no more groups
#         if p < len(springs) and '#' in springs[p:]:
#             # eg: .##?????#.. 4,1
#             return 0  # not a solution - there are still damaged springs in the record
#         return 1
#
#     if p >= len(springs):
#         return 0  # we ran out of springs but there are still groups to arrange
#
#     res = None
#     gs = groups[g]  # damaged group size
#
#     if springs[p] == '?':
#         # if we can start group of damaged springs here
#         # eg: '??#...... 3' we can place 3 '#' and there is '?' or '.' after the group
#         # eg: '??##...... 3' we cannot place 3 '#' here
#         if '.' not in springs[p:p + gs] and springs[p + gs] != '#':
#             # start damaged group here + this spring is operational ('.')
#             res = recursive_arrangement(p + gs + 1, g + 1, springs, groups) + recursive_arrangement(p + 1, g, springs, groups)
#         else:
#             # this spring is operational ('.')
#             res = recursive_arrangement(p + 1, g, springs, groups)
#     elif springs[p] == '#':
#         # if we can start damaged group here
#         if '.' not in springs[p:p + gs] and springs[p + gs] != '#':
#             res = recursive_arrangement(p + gs + 1, g + 1, springs, groups)
#         else:
#             res = 0  # not a solution - we must always start damaged group here
#     elif springs[p] == '.':
#         res = recursive_arrangement(p + 1, g, springs, groups)  # operational spring -> go to the next spring
#
#     return res


def recurse_find(row: list, i_1, i_2):
    """

    :param rows:
    :return:
    """
    # try:
    if i_1 < 0 or i_2 >= len(row):
        return True
    else:
        if row[i_1] == row[i_2]:
            if i_1 == 0 or i_2 == len(row) - 1:
                return True
            else:
                return recurse_find(row, i_1 - 1, i_2 + 1)
        else:
            return False


def find_reflection(grid: List[List[str]], i: int) -> int:
    """
    Process all grids to get the final result
    :param grid:
    :param i:
    :return:
    """
    print(f"Looking for reflections on grid #{i}...")

    tot = 0

    # look for vertical reflection
    for j in range(len(grid) - 1):
        if grid[j] == grid[j + 1]:
            print(f"rows {j} and {j+1} are alike...")
            if recurse_find(grid, j - 1, j + 2):
                print("and there is perfect reflection")
                # return (j + 1) * 100
                tot += (j + 1) * 100
                break
            else:
                print("but there is no perfect reflection")

    # look for horizontal reflection
    zipped_data = list(zip(*grid))

    for j in range(len(zipped_data) - 1):
        if zipped_data[j] == zipped_data[j + 1]:
            print(f"columns {j} and {j+1} are alike...")
            if recurse_find(zipped_data, j - 1, j + 2):
                print("and there is perfect reflection")
                # return j + 1
                tot += j + 1
                break
            else:
                print("but there is no perfect reflection")

    # print("no reflections found")
    return tot


def parse_input_file(input_file: str) -> List[List[List[str]]]:
    """
    Parse the input file to extract data
    :param input_file:
    :return:
    """
    grids = []

    # process lines from input file
    with open(input_file, 'r') as file:
        text_content = file.read()
        sections = text_content.split('\n\n')

    for section in sections:
        lines = section.split('\n')
        # Create a grid as a list of lists
        grid = [list(line.strip()) for line in lines]
        grids.append(grid)

    # print(grids)
    return grids


def main(args) -> int:
    """
    Main function
    :return: the total winnings
    """
    # record the start time
    start_time = time.time()

    if len(args) != 1:
        sys.exit(1)
        # print_help_and_exit()

    grids = parse_input_file(args[0])

    tot = 0
    for i, grid in enumerate(grids):
        tot += find_reflection(grid, i)
    print(f"Total points: {tot}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return tot


if __name__ == "__main__":
    main(sys.argv[1:])
