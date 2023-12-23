import sys
import time
from typing import Tuple, List

from shapely.geometry import Point, Polygon


def parse_input_file_get_perimeter(input_file: str) -> int:
    """
    Parse the input file
    :param input_file:
    :return: the length of the trench
    """
    num = 0

    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split()
        direction = parts[0]
        steps = parts[1]
        color = parts[2]

        # move as indicated
        if direction == 'R':
            num += int(steps)
        elif direction == 'D':
            num += int(steps)
        elif direction == 'L':
            num += int(steps)
        elif direction == 'U':
            num += int(steps)

    return num


def parse_input_file_get_vertices(input_file: str) -> List[Tuple[int, int]]:
    """
    Parse the input file to obtain the vertices of the polygon
    :param input_file:
    :return:
    """
    vertices = []
    x = y = 0

    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split()
        direction = parts[0]
        steps = parts[1]
        color = parts[2]

        # move as indicated
        if direction == 'R':
            y += int(steps)
        elif direction == 'D':
            x += int(steps)
        elif direction == 'L':
            y -= (int(steps))
        elif direction == 'U':
            x -= (int(steps))

        # store the vertice
        vertices.append((x, y))

    return vertices


def parse_input_file_get_edges(input_file: str) -> List[Tuple[int, int]]:
    """
    Parse the input file to obtain all the vertical edges by lines
    :param input_file:
    :return:
    """
    vertices = []
    x = y = 0

    with open(input_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split()
        direction = parts[0]
        steps = parts[1]
        color = parts[2]

        # move as indicated
        if direction == 'R':
            y += int(steps) + 1
        elif direction == 'D':
            x += int(steps) + 1
        elif direction == 'L':
            y -= (int(steps) + 1)
        elif direction == 'U':
            x -= (int(steps) + 1)

        # store the vertice
        vertices.append((x, y))

    return vertices


def get_result(vertices: List[Tuple[int, int]]) -> int:
    """

    :param vertices:
    :return:
    """
    # get the enclosing rectangle
    x_min = min([x for (x, y) in vertices])
    x_max = max([x for (x, y) in vertices])
    y_min = min([y for (x, y) in vertices])
    y_max = max([y for (x, y) in vertices])

    trench = Polygon(vertices)
    enclosing = Polygon([(x_min, y_min), (x_min, y_max), (x_max, y_max), (x_max, y_min)])

    perimeter = trench.length

    inner = 0

    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            point = Point((x, y))
            # check if the point is inside the polygon
            inner += 1 if point.within(trench) else 0

    area_t = trench.area
    area_e = enclosing.area
    diff = area_e - area_t

    return int(perimeter) + inner


def main(args) -> Tuple[int, int]:
    """
    Main function
    :return: the number of tiles that end up being energized
    """
    # record the start time
    start_time = time.time()

    if len(args) != 1:
        sys.exit(1)
        # print_help_and_exit()

    # part one ********************************************************

    vertices = parse_input_file_get_vertices(args[0])
    sum = get_result(vertices)
    print(f"The value we are looking for is: {sum}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return sum, -1


if __name__ == "__main__":
    main(sys.argv[1:])
