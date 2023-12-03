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
            if (self.ini - 1) <= x <= (self.end + 1):
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


class LineParser:

    pattern_l = r"Game \d+: (.*$)"
    pattern_data = r"(\d{1,2}) (red|green|blue)"

    def __init__(self, line: str, y: int):
        self.line = line
        self.y = y
        self.numbers = list()
        self.symbols = list()       # list of indexes where a symbol exists
        # self.symbols = list()
        self.process_line()
        # print(self.numbers)

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
        matches = re.finditer(r"[^\d.]", self.line)
        for match in matches:
            self.symbols.append(match.span(0)[0])

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


def main(input_file: str) -> int:
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
            matrix.append({'symbols': line_parser.get_symbols, 'numbers': line_parser.get_numbers})

    # sum of all part numbers
    sum_parts = 0
    # unique_numbers = set()

    # evaluate part numbers
    for i, element in enumerate(matrix):
        for number in element['numbers']:
            if number.check_adjacent(matrix[i]['symbols']):
                # if number.get_value not in unique_numbers:
                #     unique_numbers.add(number.get_value)
                sum_parts += number.get_value
                print(f"line: {i+1}, part number: {number.get_value}")
            else:
                if i > 0 and number.check_adjacent(matrix[i-1]['symbols']):
                    # if number.get_value not in unique_numbers:
                    #     unique_numbers.add(number.get_value)
                    sum_parts += number.get_value
                    print(f"line: {i + 1}, part number: {number.get_value}")
                else:
                    try:
                        if number.check_adjacent(matrix[i+1]['symbols']):
                            # if number.get_value not in unique_numbers:
                            #     unique_numbers.add(number.get_value)
                            sum_parts += number.get_value
                            print(f"line: {i + 1}, part number: {number.get_value}")
                    except IndexError:  # this will be the last line
                        pass

    print(f"Sum of all parts: {sum_parts}")

    return sum_parts


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day3.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])
