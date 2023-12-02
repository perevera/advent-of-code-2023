from pathlib import Path
import re
import sys
from typing import Union, Tuple

# the bag contains 12 red cubes, 13 green cubes, and 14 blue cubes
bag_load = {'red': 12, 'green': 13, 'blue': 14}
home_dir = 'C:\\Users\\veradelarochap\\PycharmProjects\\advent-of-code-2023'


class LineParser:

    pattern_line = r"Game \d+: (.*$)"
    pattern_data = r"(\d{1,2}) (red|green|blue)"

    def __init__(self, line: str):
        self.line = line
        self.data = list()  # list of dictionaries RGB
        self.process_line()

    def process_line(self) -> int:
        """
        Extract all data from a line
        :return: digit that first occurs
        """
        match = re.search(self.pattern_line, self.line)

        if match:
            payload = match.group(1)
            print(payload)
        else:
            print("No match")

        elements = payload.split(';')
        
        for element in elements:
            dict_rgb = {'red': 0, 'green': 0, 'blue': 0}
            matches = re.finditer(self.pattern_data, element)
            for match in matches:
                number = int(match.group(1))
                color = match.group(2)
                dict_rgb[color] = number
            self.data.append(dict_rgb)

    @staticmethod
    def set_is_possible(dict_rgb: dict) -> bool:
        """
        Determine if a set of values RGB is possible
        """
        ret = (dict_rgb['red'] <= bag_load['red'] and
               dict_rgb['green'] <= bag_load['green'] and
               dict_rgb['blue'] <= bag_load['blue'])

        return ret

    @property
    def is_possible(self) -> bool:
        """
        Get the sum of the IDs of the possible games
        :return:
        """
        all_true = all(self.set_is_possible(x) for x in self.data)
        return all_true

    @property
    def power_min(self) -> int:
        """
        Get the power of the min values for making this game possible
        :return:
        """
        min_rgb = {'red': 0, 'green': 0, 'blue': 0}

        for dict_rgb in self.data:
            for k in dict_rgb:
                min_rgb[k] = max(min_rgb[k], dict_rgb[k])

        return min_rgb['red'] * min_rgb['green'] * min_rgb['blue']


def main(input_file: str) -> Tuple[int, int]:
    """
    Main function
    :param input_file
    :return: the sum of all calibration values
    """
    sum_ids = 0
    sum_power_min = 0

    home_path = Path(home_dir)
    file_path = home_path / input_file

    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            game_num = i + 1
            line_parser = LineParser(line.strip())
            if line_parser.is_possible:
                print(f"Game {game_num} is possible")
                sum_ids += game_num
            else:
                print(f"Game {game_num} is not possible")
            print(f"Game {game_num} power minimum is: {line_parser.power_min}")
            sum_power_min += line_parser.power_min

    print(f"The sum of IDs of the possible games is: {sum_ids}")
    print(f"The sum of the power of these sets is: {sum_power_min}")

    return sum_ids, sum_power_min


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day1.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])
