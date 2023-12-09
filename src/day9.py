import math
import sys
import time
from typing import Union, Tuple, List


def extrapolation(series: List[List[int]], backwards: bool = False) -> int:
    """
    Extrapolate values for all series then sum up those values
    :param series: list of series (lists) of integers
    :return: sum of extrapolated values
    """
    print(f"Starting the extrapolation...")

    sum_vals = 0

    for s in series:
        new_series = []
        t = s
        while True:
            t = [t[i]-t[i-1] for i in range(1, len(t))]
            new_series.append(t)
            if all(v == 0 for v in t):
                break
        print(new_series)        # DEBUG

        diff = 0

        if backwards:
            for n in new_series[-2::-1]:
                diff = n[0] - diff
            new_val = s[0] - diff
            sum_vals += new_val
        else:
            for n in new_series[-2::-1]:
                diff += n[-1]
            sum_vals += diff + s[-1]

    print(f"Finished, sum of extrapolated values: {sum_vals}")

    return sum_vals


def parse_input_file(input_file: str) -> List[List[int]]:
    """
    Process all lines from the input file to extract data
    :param input_file: input file name with path
    :return:
    """
    series = []
    
    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        series.append([int(num) for num in line.strip().split()])

    return series


def print_help_and_exit():
    """
    Print help and exit
    """
    print("Usage: python day9.py <part_number> <input_file>")
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

    series = parse_input_file(args[1])

    # DEBUG
    print(series)

    if part_number == 1:
        sum_vals = extrapolation(series)
    elif part_number == 2:
        sum_vals = extrapolation(series, backwards=True)
    else:
        print_help_and_exit()

    # DEBUG
    print(f"Sum of extrapolated values: {sum_vals}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return sum_vals


if __name__ == "__main__":
    main(sys.argv[1:])



