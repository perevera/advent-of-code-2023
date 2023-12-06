import sys
import time


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


def part_one(input_file: str):
    """
    Main function
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
    Main function
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
    else:
        print_help_and_exit()

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")
