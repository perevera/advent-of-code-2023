from typing import Union

dict_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }
dict_numbers_reversed = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9}


def read_lines_from_file(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read all lines into a list
        lines = file.readlines()

    return lines


def get_calibration_value(line: str) -> int:
    """
    Get the calibration value for a line
    :param line: input line
    :return: calibration value
    """
    val = None

    line = line.strip()

    for i, c in enumerate(line):
        try:
            v1 = int(c)
            break
        except ValueError:       # not a digit
            v1 = check_digit(line, i)
            if v1 is not None:
                break

    for i, c in enumerate(line[::-1]):
        try:
            v2 = int(c)
            break
        except ValueError:       # not a digit
            v2 = check_digit(line[::-1], i, reversed=True)
            if v2 is not None:
                break

    val = v1 * 10 + v2

    return val


def check_digit(line: str, i: int, reversed: bool = False) -> Union[int, None]:
    """
    Check if a digit with letters exist starting at the given index
    :param line: line
    :param i: index
    :param reversed: flag to indicate if the input line is reversed to look up from the end
    :return: digit
    """
    if reversed:
        the_numbers = dict_numbers_reversed
    else:
        the_numbers = dict_numbers

    try:
        # digits with 3 letters
        key = line[i:i + 3]
        ret = the_numbers[key]
    except KeyError:
        try:
            # digits with 4 letters
            key = line[i:i + 4]
            ret = the_numbers[key]
        except KeyError:
            try:
                # digits with 5 letters
                key = line[i:i + 5]
                ret = the_numbers[key]
            except KeyError:
                ret = None

    return ret


def main():
    # input file path
    # file_path = '../sample/sample-day1-2.txt'
    file_path = '../input/input-day1.txt'

    # read lines from the file
    lines = read_lines_from_file(file_path)

    # read calibration values and compute the total
    total = 0

    for line in lines:
        print(get_calibration_value(line))
        total += get_calibration_value(line)

    print(f"All the calibration values sum: {total}")


if __name__ == "__main__":
    main()
