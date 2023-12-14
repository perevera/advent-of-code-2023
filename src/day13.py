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
    print(f"Looking for reflections on grid #{i}...")

    zipped_data = list(zip(*grid))

    # look for vertical reflection
    for j in range(len(grid) - 1):
        if grid[j] == grid[j + 1]:
            print(f"rows {j} and {j+1} are alike...")
            if recurse_find_one(grid, j - 1, j + 2):
                print("and there is perfect reflection")
                return (j + 1) * 100
            else:
                print("but there is no perfect reflection")

    # look for horizontal reflection
    for j in range(len(zipped_data) - 1):
        if zipped_data[j] == zipped_data[j + 1]:
            print(f"columns {j} and {j+1} are alike...")
            if recurse_find_one(zipped_data, j - 1, j + 2):
                print("and there is perfect reflection")
                return j + 1
            else:
                print("but there is no perfect reflection")


def find_reflection_two(grid: List[List[str]], i: int) -> int:
    """
    Process all grids to get the final result
    :param grid:
    :param i:
    :return:
    """
    print(f"Looking for reflections on grid #{i}...")

    zipped_data = list(zip(*grid))

    # first pass looking for vertical reflection
    for j in range(len(grid) - 1):
        diffs = [(i, one, another) for i, (one, another) in enumerate(zip(grid[j], grid[j + 1])) if one != another]
        if len(diffs) <= 1:
            print(f"rows {j} and {j-1} differ by one...")
            if recurse_find_one(grid, j - 1, j + 2):
                print("and there is perfect reflection")
                return (j + 1) * 100
            else:
                print("but there is no perfect reflection")

    # second pass looking for vertical reflection
    for j in range(len(grid) - 1):
        if grid[j] == grid[j + 1]:
            print(f"rows {j} and {j-1} are alike...")
            if recurse_find_two(grid,  j - 1, j + 2):
                print("and there is perfect reflection")
                return (j + 1) * 100
            else:
                print("but there is no perfect reflection")

    # second pass looking for horizontal reflection
    for j in range(len(zipped_data) - 1):
        diffs = [(i, one, another) for i, (one, another) in enumerate(zip(zipped_data[j], zipped_data[j + 1]))
                 if one != another]
        if len(diffs) <= 1:
            print(f"columns {j} and {j-1} differ by one...")
            if recurse_find_one(zipped_data, j - 1, j + 2):
                print("and there is perfect reflection")
                return j + 1
            else:
                print("but there is no perfect reflection")

    # first pass looking for horizontal reflection
    for j in range(len(zipped_data) - 1):
        if zipped_data[j] == zipped_data[j + 1]:
            print(f"columns {j} and {j-1} are alike...")
            if recurse_find_two(zipped_data, j - 1, j + 2):
                print("and there is perfect reflection")
                return j + 1
            else:
                print("but there is no perfect reflection")


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


def main(args) -> Tuple[int, int]:
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

    tot_1 = 0
    tot_2 = 0
    for i, grid in enumerate(grids):
        tot_1 += find_reflection_one(grid, i)
        tot_2 += find_reflection_two(grid, i)
    print(f"Total points: {tot_1} and {tot_2}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return tot_1, tot_2


if __name__ == "__main__":
    main(sys.argv[1:])
