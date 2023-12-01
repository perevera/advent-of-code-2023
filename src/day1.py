import sys
from typing import Union, Tuple


dict_numbers = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }
dict_numbers_reversed = {'eno': 1, 'owt': 2, 'eerht': 3, 'ruof': 4, 'evif': 5, 'xis': 6, 'neves': 7, 'thgie': 8, 'enin': 9}


class LineParser:
    def __init__(self, line: str):
        self.line = line
        self.first_digit = self.get_first_digit()
        self.last_digit = self.get_last_digit()
        print(f"first: {self.first_digit}, last: {self.last_digit}")

    def get_first_digit(self) -> int:
        """
        Get first digit
        :return: digit that first occurs
        """
        i1, val1 = self.search_first_digit()
        i2, val2 = self.search_first_word()

        if val1:
            if val2:
                if i1 < i2:
                    return val1
                else:
                    return dict_numbers[val2]
            else:
                return val1
        else:
            return dict_numbers[val2]

    def get_last_digit(self) -> int:
        """
        Get last digit
        :return: digit that first occurs
        """
        i1, val1 = self.search_first_digit(reverse=True)
        i2, val2 = self.search_first_word(reverse=True)

        if val1:
            if val2:
                if i1 < i2:
                    return val1
                else:
                    return dict_numbers_reversed[val2]
            else:
                return val1
        else:
            return dict_numbers_reversed[val2]

    def search_first_digit(self, reverse: bool = False) -> Tuple[Union[int, None], Union[int, None]]:
        """
        Search the first occurrence of a digit
        :param reverse:
        :return:
        """
        line = self.line

        if reverse:
            line = self.line[::-1]

        for i, char in enumerate(line):
            try:
                digit = int(line[i])
                return i, digit
            except ValueError:  # not a digit
                continue

        return None, None

    def search_first_word(self, reverse: bool = False) -> Tuple[Union[int, None], Union[str, None]]:
        """
        Search the first occurrence of a word that corresponds to a digit
        :param reverse
        :return:
        """
        found = dict()

        if reverse:
            line = self.line[::-1]
            numbers = dict_numbers_reversed
        else:
            line = self.line
            numbers = dict_numbers

        for k in numbers.keys():
            # Using find() method
            i = line.find(k)
            # Check if the substring is found
            if i != -1:
                found[k] = i

        if found.values():
            i = min(found.values())
            word = min(found, key=lambda k: found[k])
            return i, word
        else:
            return None, None

    @property
    def calibration_value(self) -> int:
        try:
            val = self.first_digit * 10 + self.last_digit
            return val
        except TypeError:
            return None


def main(input_file: str) -> int:
    """
    Main function
    :param input_file
    :return: the sum of all calibration values
    """
    total = 0

    with open(input_file, 'r') as file:
        for line in file:
            line_parser = LineParser(line.strip())
            total += line_parser.calibration_value

    print(f"All the calibration values sum: {total}")

    return total


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day1.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])
