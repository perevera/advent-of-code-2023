import sys


def best(input, maps):
    """
    Recursive function to return the lowest value
    :param input: range of source values we want to look the least destination linked
    :param maps: list of maps
    :return:
    """
    # this is the end of the recursion, we just return the lowest value in the range as this is the destination
    if not maps:
        return input[0]

    # d is destination range start, s is source range start, r is range length
    for d, s, r in maps[0]:     # looking into first map

        # case 1: input range maps entirely inside a mapping so we map and move to next mapping
        if s <= input[0] < s + r and s <= input[1] < s + r:
            r1 = (d + input[0] - s, d + input[1] - s)
            return best(r1, maps[1:])       # next recursion

        # case 2: range starts inside a mapping but ends outside -> 2 sections
        elif s <= input[0] < s + r < input[1]:
            r1 = (d + input[0] - s, d + r)
            r2 = (s + r, input[1])
            return min(best(r1, maps[1:]), best(r2, maps))

        # case 3: range starts below a mapping but ends inside mapping -> 2 sections
        elif input[0] < s <= input[1] < s + r:
            r1 = (input[0], s - 1)
            r2 = (d, d + input[1] - s)
            return min(best(r1, maps), best(r2, maps[1:]))

        # case 4: range begins below and ends above a mapping -> 3 sections
        elif input[0] < s and input[1] > s + r:
            r1 = (input[0], s - 1)
            r2 = (d, d + r)
            r3 = (s + r, input[1])
            return min(best(r1, maps), best(r2, maps[1:]), best(r3, maps))

    # No maps matched this range. Preserve values and move on.
    return best(input, maps[1:])


def main(input_file: str):
    """
    Main function
    :param input_file
    :return: the sum of all part numbers
    """
    # process lines from input file
    with open(input_file, 'r') as file:
        text_content = file.read()
        sections = text_content.split("\n\n")
        seeds = [int(n) for n in sections[0].split()[1:]]
        maps = []
        for section in sections[1:]:
            maps.append([])
            for line in section.split("\n")[1:]:
                if line != '':
                    maps[-1].append(tuple(int(i) for i in line.split()))

    # part 1, just create a "range" for each seed. It works out the same
    inputs_1 = [(i, i) for i in seeds]      # list of ranges for seeds
    print(min((best(input, maps) for input in inputs_1)))

    # part 2, note the -1 for the second number since we use inclusive ranges
    inputs_2 = [(seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1] - 1) for i in range(len(seeds) // 2)]
    print(min((best(input, maps) for input in inputs_2)))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day5.py <input_file>")
        sys.exit(1)

    main(sys.argv[1])
