import re
import sys
import time
from typing import Union, Tuple, List


def get_sum_arrangements(info: list, patterns: list) -> int:
    """
    Test all arrangements and get the valid number of combinations
    :param info:
    :param patterns:
    :return: the total sum of possible arrangements
    """
    sum_arrangements = 0

    for i, row in enumerate(info):
        unknowns = [i for i, c in enumerate(row) if c == '?']
        num_combinations = 2 ** len(unknowns)
        total_ones = sum([1 for c in patterns[i] if c == '1'])
        current_ones = sum([1 for c in row if c == '1'])
        missing_ones = total_ones - current_ones
        this_arrangements = 0
        for j in range(num_combinations):
            # bnum = bin(j)
            binary_string = bin(j)[2:].zfill(len(unknowns))
            num_ones = sum([1 for c in binary_string if c == '1'])
            if num_ones != missing_ones:
                continue
            # Convert the string to a list of characters
            char_list = list(row)
            for k, l in enumerate(unknowns):
                char_list[l] = binary_string[k]
            # Join the characters back into a string
            new_row = ''.join(char_list)
            match = re.search(patterns[i], new_row)

            if match:
                this_arrangements += 1

        print(f"#{i} -> {this_arrangements} possible arrangements for row {row}")
        sum_arrangements += this_arrangements

    return sum_arrangements


def parse_input_file(input_file: str) -> Tuple[List[str], List[str]]:
    """
    Process all lines from the input file to extract data
    :param input_file: input file name with path
    :return: records
    """
    info = []
    # groups = []
    patterns = []

    with open(input_file, 'r') as file:
        for line in file:
            parts = line.split()
            part_one = parts[0].replace('#', '1').replace('.', '0')
            info.append(part_one)
            part_two = parts[1]
            groups = [int(n) * '1' for n in part_two.split(',')]
            regex = '^0*' + '0+'.join(g for g in groups) + '0*$'
            patterns.append(regex)

    return info, patterns


def print_help_and_exit():
    """
    Print help and exit
    """
    print("Usage: python day12.py <expansion_factor> <input_file>")
    print("\twhere <expansion_factor> is one of: 2, 10, 100 or 1000000 and <input_file> is the input data file with path")
    sys.exit(1)


def main(args) -> int:
    """
    Main function
    :return: the total winnings
    """

    # I will run a combination of regex and binary masks
    # The entries will be converted as follows, e.g.:
    # .#?#????##?# 1,1,1,4 -> 01?1????11?1 (# -> 1, . -> 0, ? -> 0)
    # Then from the numbers we will compose a regex, in this case: \.+\#\.+\#\.+\#\#\#\#
    # We will then generate all combinations for th ? characters (# or .) and check if they match the regex

    # record the start time
    start_time = time.time()

    if len(args) != 2:
        print_help_and_exit()

    # get the initial grid from the input file
    info, patterns = parse_input_file(args[1])

    # compose regex
    tot = get_sum_arrangements(info, patterns)
    print(f"Total number of possible arrangements is: {tot}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return tot

if __name__ == "__main__":
    main(sys.argv[1:])
