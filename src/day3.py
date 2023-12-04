from pathlib import Path
import re
import sys
from typing import Union, Tuple, List

# the bag contains 12 red cubes, 13 green cubes, and 14 blue cubes
bag_load = {'red': 12, 'green': 13, 'blue': 14}
home_dir = 'C:\\Users\\veradelarochap\\PycharmProjects\\advent-of-code-2023'


class Number:

    def __init__(self, value: int, x: Tuple[int, int], y: int):
        self.value = value
        self.ini = x[0]
        self.end = x[1]
        self.y = y

    def __repr__(self):
        return f"Number(value: {self.value}, x1:{self.ini}, x2: {self.end}, y: {self.y})"

    def __str__(self):
        return f"Number(value: {self.value}, x1:{self.ini}, x2: {self.end}, y: {self.y})"

    @property
    def get_value(self):
        """

        :return:
        """
        return self.value

    def check_adjacent(self, coords: list) -> bool:
        """
        Check if this number is adjacent to any of the symbols whose coordinates are received
        :param coords:
        :return:
        """
        for x in coords:
            if (self.ini - 1) <= x <= self.end:
                return True     # adjacent symbol found

        return False    # no adjacent symbol found


class Symbol:

    def __init__(self, symbol: chr, x: int, y: int):
        self.symbol = symbol
        self.x = x
        self.y = y

    @property
    def get_x(self):
        """
        Get the x coordinate of the symbol
        :return:
        """
        return self.x

    def __repr__(self):
        return f"Symbol(value: {self.symbol}, x:{self.x}, y: {self.y})"

    def __str__(self):
        return f"Symbol(value: {self.symbol}, x:{self.x}, y: {self.y})"

    def get_gear_ratio(self, matrix: list) -> int:
        """
        Compute the gear ratio assuming this symbol is an asterisk
        :return:
        """
        gear_numbers = list()

        for i in range(-1, 2, 1):
            print(i)
            for number in matrix[self.y-i]['numbers']:
                if number.check_adjacent([self.x]):
                    gear_numbers.append(number.get_value)

        if len(gear_numbers) == 2:
            return gear_numbers[0] * gear_numbers[1]
        else:
            return 0


class LineParser:

    pattern_l = r"Game \d+: (.*$)"
    pattern_data = r"(\d{1,2}) (red|green|blue)"

    def __init__(self, line: str, y: int):
        self.line = line
        self.y = y
        self.numbers = list()
        self.symbols = list()       # list of indexes where a symbol exists
        self.asterisks = list()     # list of indexes where an asterisk exists
        self.process_line()

    def process_line(self):
        """
        Extract all relevant data from a line
        :return: digit that first occurs
        """
        # find all numbers
        matches = re.finditer(r"\d+", self.line)
        for match in matches:
            number = int(match.group(0))
            coords = match.span(0)
            # print(f"Match found, number: {number}, coords: {coords}")
            self.numbers.append(Number(number, coords, self.y))

        # find all symbols
        matches = re.finditer(r"[^\d\\.]", self.line)
        for match in matches:
            self.symbols.append(match.span(0)[0])

        # find all asterisks
        matches = re.finditer(r'\*', self.line)
        for match in matches:
            # self.asterisks.append(match.span(0)[0])
            self.asterisks.append(Symbol('*', match.span(0)[0], self.y))

    @property
    def get_numbers(self) -> List[Number]:
        """
        Get the list of numbers for current line
        :return: list of objects of class Number
        """
        return self.numbers

    @property
    def get_symbols(self) -> List[Symbol]:
        """
        Get the list of symbols for current line
        :return: list of objects of class Number
        """
        return self.symbols

    @property
    def get_asterisks(self) -> List[Symbol]:
        """
        Get the list of symbols for current line
        :return: list of objects of class Number
        """
        return self.asterisks


def main(input_file: str) -> Tuple[int, int]:
    """
    Main function
    :param input_file
    :return: the sum of all part numbers
    """
    home_path = Path(home_dir)
    file_path = home_path / input_file

    matrix = []

    # read and process all lines from the input file
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            line_parser = LineParser(line.strip(), i)
            matrix.append({'asterisks': line_parser.get_asterisks,
                           'symbols': line_parser.get_symbols,
                           'numbers': line_parser.get_numbers})

    # sum of all part numbers
    sum_parts = 0
    sum_gear_ratios = 0

    # evaluate part numbers and gears
    for i, element in enumerate(matrix):
        # part 1
        for number in element['numbers']:
            if number.check_adjacent(matrix[i]['symbols']):
                sum_parts += number.get_value
                print(f"line: {i+1}, number: {number.get_value}")
            else:
                if i > 0 and number.check_adjacent(matrix[i-1]['symbols']):
                    sum_parts += number.get_value
                    print(f"line: {i + 1}, number: {number.get_value}")
                else:
                    try:
                        if number.check_adjacent(matrix[i+1]['symbols']):
                            sum_parts += number.get_value
                            print(f"line: {i + 1}, number: {number.get_value}")
                    except IndexError:  # this will be the last line
                        pass
        # part 2
        for asterisk in element['asterisks']:
            sum_gear_ratios += asterisk.get_gear_ratio(matrix)

    print(f"\nSum of all parts: {sum_parts}")
    print(f"\nSum of all gear ratios: {sum_gear_ratios}")

    return sum_parts, sum_gear_ratios


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day3.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])
