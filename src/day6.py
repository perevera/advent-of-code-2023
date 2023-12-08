import sys
import time
from typing import Union


def get_num_wins(ttime: int, ddistance: int) -> int:
    """
    Determine the number of ways you can beat the record in this race
    :param ttime: race time
    :param ddistance: record distance
    :return:
    """
    num_wins = 0
    # r is the recharge time, the formula for the distance reached is: d = (ttime - r) * r
    for r in range(ttime):
        d = (ttime - r) * r
        if d > ddistance:
            num_wins += 1

    return num_wins


def get_lower(t1: int, t2: int, ttime: int, ddistance: int) -> Union[int, None]:
    """
    Determine the lower time needed to beat that distance, with recursion
    :param t1:
    :param t2:
    :param distance:
    :return:
    """
    print(f"Executing get_lower with t1 = {t1}, t2 = {t2}")
    if ((ttime - t1) * t1) > ddistance:
        return t1

    if ((ttime - t2) * t2) <= ddistance:
        return None     # it means no button holding time inside this range would beat the record

    # split in two halves
    span = t2 - t1
    tt1 = t1
    tt2 = span // 2 + tt1
    tt3 = tt2 + 1
    tt4 = t2

    l1 = get_lower(tt1, tt2, ttime, ddistance)
    l2 = get_lower(tt3, tt4, ttime, ddistance)

    return l2 if l1 is None else l1


def get_upper(t1: int, t2: int, ttime: int, ddistance: int) -> Union[int, None]:
    """
    Determine the upper time needed to beat that distance, with recursion
    :param t1:
    :param t2:
    :param distance:
    :return:
    """
    if ((ttime - t2) * t2) > ddistance:
        return t2

    if ((ttime - t1) * t1) <= ddistance:
        return None     # it means no button holding time inside this range would beat the recordsample-day6.txt

    # split in two halves
    span = t2 - t1
    tt1 = t1
    tt2 = span // 2 + tt1
    tt3 = tt2 + 1
    tt4 = t2

    l1 = get_upper(tt1, tt2, ttime, ddistance)
    l2 = get_upper(tt3, tt4, ttime, ddistance)

    return l1 if l2 is None else l2


def get_num_wins_recursive(ttime: int, ddistance: int) -> int:
    """
    Determine the number of ways you can beat the record in this race
    :param ttime: race time
    :param ddistance: record distance
    :return:
    """
    # split in two halves
    t1 = 1
    t2 = ttime // 2
    t3 = t2 + 1
    t4 = ttime

    # start the recursive method
    lower_limit = get_lower(t1, t2, ttime, ddistance)
    upper_limit = get_upper(t3, t4, ttime, ddistance)

    # results
    print(f"You could hold the button anywhere from {lower_limit} to {upper_limit} milliseconds and beat the record")
    num_wins = upper_limit - lower_limit + 1
    return num_wins


def part_one(input_file: str):
    """
    Main function for part one
    :param input_file
    :return: the sum of all part numbers
    """
    records = dict()

    # process lines from input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Check if the last line is empty
    if lines and lines[-1].strip() == '':
        lines.pop()

    for line in lines:
        fields = line.split(':')
        records[fields[0]] = [int(n) for n in fields[1].split()]

    # DEBUG
    print(records)

    num_wins = 0

    for t, d in zip(records['Time'], records['Distance']):
        # print(t, d)
        if num_wins == 0:
            num_wins = get_num_wins(t, d)
        else:
            num_wins *= get_num_wins(t, d)

    print(f"The number of ways to win multiplied give: {num_wins}")

    return num_wins


def part_two(input_file: str):
    """
    Main function for part 2
    :param input_file
    :return: the sum of all part numbers
    """
    record = dict()

    # process lines from input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Check if the last line is empty
    if lines and lines[-1].strip() == '':
        lines.pop()

    for line in lines:
        fields = line.split(':')
        value = ''
        for n in fields[1].split():
            value += n
        record[fields[0]] = int(value)

    # DEBUG
    print(record)

    num_wins = get_num_wins(record['Time'], record['Distance'])

    print(f"The number of ways to win is: {num_wins}")

    return num_wins


def part_two_recursive(input_file: str):
    """
    Main function for part 2 (recursion)
    :param input_file
    :return: the sum of all part numbers
    """
    record = dict()

    # process lines from input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Check if the last line is empty
    if lines and lines[-1].strip() == '':
        lines.pop()

    for line in lines:
        fields = line.split(':')
        value = ''
        for n in fields[1].split():
            value += n
        record[fields[0]] = int(value)

    # DEBUG
    print(record)

    num_wins = get_num_wins_recursive(record['Time'], record['Distance'])

    print(f"The number of ways to win is: {num_wins}")

    return num_wins


def print_help_and_exit():
    """

    :return:
    """
    print("Usage: python day6.py <part_number> <input_file>")
    print("\twhere <part_number> is one of: 1, 2 and <input_file> is the input data file with path")
    sys.exit(1)


if __name__ == "__main__":

    # record the start time
    start_time = time.time()

    if len(sys.argv) != 3:
        print_help_and_exit()

    part_number = int(sys.argv[1])

    if part_number == 1:
        part_one(sys.argv[2])
    elif part_number == 2:
        part_two(sys.argv[2])
    elif part_number == 3:
        part_two_recursive(sys.argv[2])
    else:
        print_help_and_exit()

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")
