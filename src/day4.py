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

    pattern_line = r"Card\s+\d+: (.*$)"
    pattern_number = r"(\d{1,2})"

    def __init__(self, line: str):
        self._line = line
        self._wins = 0
        self._data = list()  # list of dictionaries RGB
        self.process_line()

    def process_line(self) -> int:
        """
        Extract all data from a line
        :return: digit that first occurs
        """
        match = re.search(self.pattern_line, self._line)

        if match:
            payload = match.group(1)
            print(payload)
        else:
            print("No match")
            return 0

        halves = payload.split('|')

        # extract winning numbers
        winning_numbers = set()

        matches = re.finditer(self.pattern_number, halves[0])
        for match in matches:
            winning_numbers.add(int(match.group(1)))

        # extract my numbers
        my_numbers = set()

        matches = re.finditer(self.pattern_number, halves[1])
        for match in matches:
            my_numbers.add(int(match.group(1)))

        # get number of wins
        self._wins = sum(1 for n in my_numbers if n in winning_numbers)

        print(f"This card contains {self._wins} wins")

    @property
    def wins(self) -> int:
        """
        Get the number of wins in the card
        :return:
        """
        return self._wins

    @property
    def points(self) -> int:
        """
        Get the points the card is worth
        :return:
        """
        return 2**(self._wins-1) if self._wins > 0 else 0


def main(input_file: str) -> Tuple[int, int]:
    """
    Main function
    :param input_file
    :return: the sum of all part numbers
    """
    total_wins = 0
    total_cards = 0
    cards = []

    # read and process all lines from the input file
    with open(input_file, 'r') as file:
        for i, line in enumerate(file):
            line_parser = LineParser(line.strip())
            print(line_parser.points)
            total_wins += line_parser.points
            try:
                cards[i] += 1
            except IndexError:
                cards.append(1)
            for j in range(cards[i]):
                for k in range(line_parser.wins):
                    try:
                        cards[i+k+1] += 1
                    except IndexError:
                        cards.append(1)

    # get total number of cards
    total_cards = sum(n for n in cards)

    print(f"The total number of wins is: {total_wins}")
    print(f"The total number of cards is: {total_cards}")

    return total_wins, total_cards


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day4.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])
