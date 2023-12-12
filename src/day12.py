import sys
import time


# 1. part - What is the sum of possible arrangements?
def recursive_arrangement(p, g, springs, groups):
    """
    Recursive function to count all different arrangements of groups of damaged springs that match the requirement
    :param spring_i: position where to start the search in the array of springs
    :param group_i: index of the group we are trying to arrange
    :param springs: array of springs
    :param groups: list of sizes of groups of damaged spring
    :return:
    """
    if g >= len(groups):  # no more groups
        if p < len(springs) and '#' in springs[p:]:
            # eg: .##?????#.. 4,1
            return 0  # not a solution - there are still damaged springs in the record
        return 1

    if p >= len(springs):
        return 0  # we ran out of springs but there are still groups to arrange

    res = None
    gs = groups[g]  # damaged group size

    if springs[p] == '?':
        # if we can start group of damaged springs here
        # eg: '??#...... 3' we can place 3 '#' and there is '?' or '.' after the group
        # eg: '??##...... 3' we cannot place 3 '#' here
        if '.' not in springs[p:p + gs] and springs[p + gs] != '#':
            # start damaged group here + this spring is operational ('.')
            res = recursive_arrangement(p + gs + 1, g + 1, springs, groups) + recursive_arrangement(p + 1, g, springs, groups)
        else:
            # this spring is operational ('.')
            res = recursive_arrangement(p + 1, g, springs, groups)
    elif springs[p] == '#':
        # if we can start damaged group here
        if '.' not in springs[p:p + gs] and springs[p + gs] != '#':
            res = recursive_arrangement(p + gs + 1, g + 1, springs, groups)
        else:
            res = 0  # not a solution - we must always start damaged group here
    elif springs[p] == '.':
        res = recursive_arrangement(p + 1, g, springs, groups)  # operational spring -> go to the next spring

    return res


def parse_input_file(input_file: str):
    with open(input_file) as f:
        sum_of_arrangements = 0

        for line in f.readlines():
            springs, groups = line.split()

            groups = list(map(int, groups.split(',')))
            springs = springs + '.'  # make sure there is operational spring after each damaged group

            sum_of_arrangements += recursive_arrangement(0, 0, springs, groups)

    return sum_of_arrangements


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

    tot = parse_input_file(args[0])

    print(f"Total number of arrangements: {tot}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return tot


if __name__ == "__main__":
    main(sys.argv[1:])
