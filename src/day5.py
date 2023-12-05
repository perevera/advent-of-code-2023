# import asyncio
import multiprocessing
# from pathlib import Path
import re
import sys
from typing import Union, Tuple, List, Dict

# the bag contains 12 red cubes, 13 green cubes, and 14 blue cubes
bag_load = {'red': 12, 'green': 13, 'blue': 14}
home_dir = 'C:\\Users\\veradelarochap\\PycharmProjects\\advent-of-code-2023'


maps = {}


class Map:

    def __init__(self, name: str, data: list):
        self.name = name
        self.mapping = list()
        self.create_mapping(data)

    def __repr__(self):
        return f"Map(name: {self.name}, mapping:{self.mapping})"

    def __str__(self):
        return f"Map(name: {self.name}, mapping:{self.mapping})"

    def map(self, i: int) -> int:
        """
        Get the mapping
        :return:
        """
        for map in self.mapping:
            if map['lower'] <= i < map['upper']:
                return i + map['diff']

        return i

    def create_mapping(self, data: list):
        """
        Populate the mapping from the data received
        :param data:
        :return:
        """
        for line in data:
            dest = line[0]
            source = line[1]
            range_ = line[2]
            diff = dest - source
            lower = source
            upper = source + range_
            self.mapping.append({'lower': lower, 'upper': upper, 'diff': diff})


def get_location(seed: int) -> int:
    """
    Get the location corresponding to a seed
    :param seed:
    :param maps:
    :return:
    """
    # DEBUG
    print(f"Running get_location for seed: {seed}")

    global maps

    soil = maps['seed-to-soil'].map(seed)
    fertilizer = maps['soil-to-fertilizer'].map(soil)
    water = maps['fertilizer-to-water'].map(fertilizer)
    light = maps['water-to-light'].map(water)
    temperature = maps['light-to-temperature'].map(light)
    humidity = maps['temperature-to-humidity'].map(temperature)
    location = maps['humidity-to-location'].map(humidity)

    # DEBUG
    print(f"seed {seed} -> soil {soil} -> fertilizer {fertilizer} -> water {water} -> light {light} "
          f"-> temperature {temperature} -> humidity {humidity} -> location {location}")

    return location


def get_location_in_range(start: int, range_: int) -> int:
    """
    Get the location corresponding to a range of seeds
    :param start:
    :param range_:
    :return:
    """
    # DEBUG
    print(f"Running get_location_in_range for start: {start}, end: {range_}")

    seeds = [seed for seed in range(start, start + range_)]

    # Run the async functions in parallel and collect results
    with multiprocessing.Pool(processes=4) as pool:
        # Use pool.map to apply the function to each element in parallel
        results = pool.map(get_location, seeds)

    # results = [await get_location(seed) for seed in range(start, start+range_)]

    return min(list(results))


def main(input_file: str) -> Tuple[int, int]:
    """
    Main function
    :param input_file
    :return: the sum of all part numbers
    """
    pattern_seeds = r"seeds: \d+(\s+\d+)*"
    pattern_number = r"(\d+)"
    pattern_map = r"([\w-]+(\s+[\w-]+)*) map:"

    list_seeds = []
    mappings = dict()

    # read and process all lines from the input file
    current_map = None

    # process lines from input file
    with open(input_file, 'r') as file:
        for line in file:
            sline = line.strip()
            # create list of seed numbers
            seeds = re.match(pattern_seeds, sline)
            if seeds:
                numbers = re.finditer(pattern_number, sline)
                for number in numbers:
                    list_seeds.append(int(number.group(1)))
                continue

            # extracting data from a mapping
            if current_map:
                if sline:
                    mappings[current_map].append([int(n) for n in line.split(' ')])
                else:
                    print("Line is blank")
                    current_map = None

            # allocating space for a new mapping
            map_name = re.match(pattern_map, sline)
            if map_name:
                current_map = map_name.group(1)
                mappings[current_map] = list()

    # create mapping objects
    global maps
    for name in mappings:
        maps[name] = Map(name, mappings[name])
        print(maps[name])

    # find locations (firt part)
    locations = []
    for seed in list_seeds:
        locations.append(get_location(seed))

    # min location
    min_1 = min(locations)
    print(f"The lowest location number (first part) is {min_1}")

    # find locations (seconds part)
    # locations = []

    # Create an event loop
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)

    # List of async functions to run
    async_functions = []
    # async_functions = [async_function(1), async_function(2), async_function(3)]

    min_2 = None
    params = []

    for i in range(0, len(list_seeds), 2):
        start = list_seeds[i]
        range_ = list_seeds[i+1]
        params.append((start, range_))
        # async_functions.append(get_location_in_range(start, range_))

    # Run the async functions in the event loop and collect results
    # results = loop.run_until_complete(asyncio.gather(*async_functions))

    # Create a multiprocessing pool with 4 processes
    with multiprocessing.Pool(processes=4) as pool:
        # Use pool.map to apply the function to each element in parallel
        results = pool.starmap(get_location_in_range, params)

    # Close the event loop
    # loop.close()

    # min location
    min_2 = min(list(results))
    print(f"The lowest location number (second part) is {min_2}")

    return min_1, min_2


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day5.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])
