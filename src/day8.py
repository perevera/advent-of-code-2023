import math
import sys
import time
from typing import Union, Tuple, List


# class Node:
#     def __init__(self, name: str, next_nodes: tuple):
#         self.name = name
#         self.next = {'L': next_nodes[0], 'R': next_nodes[1]}
#
#     def __repr__(self):
#         return f"Node -> name: {self.name}, next left: {self.next['L']}, next_right: {self.next['R']}"
#
#     # def __str__(self):
#     #     return f"Node -> name: {self.name}, next left:{self.next['L']}, next_right: {self.next['R']}"


network = dict()


def get_num_steps_first(network: dict, directions: str) -> int:
    """
    Calculate the steps needed to reach final node 'ZZZ' from the starting node 'AAA'
    :param network: dictionary that depicts the network
    :param directions: sequence of directions to take
    :return: number of steps needed to reach final node 'ZZZ'
    """
    print(f"Starting the route...")

    i = 0
    num_steps = 0
    current_node = 'AAA'

    while True:
        if i == len(directions):
            i = 0
        current_node = network[current_node][directions[i]]
        print(f"current: {current_node}")
        i += 1
        num_steps += 1
        if current_node == 'ZZZ':
            break

    # while not finished:
    #     print(f"number of steps: {num_steps}...")
    #     for direction in directions:
    #         num_steps += 1
    #         this_node = network[next_node_name]
    #         next_node_name = this_node.next[direction]
    #         if next_node_name == 'ZZZ':
    #             finished = True
    #             break

    print(f"Finished, number of steps: {num_steps}")

    return num_steps


def get_num_steps_second(network: dict, directions: str) -> int:
    """
    Calculate the steps needed to reach all final nodes '**Z' from the starting nodes '**A'.
    This uses a trick that I borrowed from the Reddit forum: getting the lowest common multiple (LCM) of the number of
    steps for every path.
    I initially didn't understand why the search is cyclic, i.e.: if you find '**Z' in n steps and you go on moving
    along the network following directions you would reach another '**Z' in n steps, and over and over again.
    However, the pattern of the LCM becomes visible if you pay attention to the explanation and the bold parts:
        Step 0: You are at 11A and 22A.
        Step 1: You choose all of the left paths, leading you to 11B and 22B.
        Step 2: You choose all of the right paths, leading you to 11Z and 22C.
        Step 3: You choose all of the left paths, leading you to 11B and 22Z.
        Step 4: You choose all of the right paths, leading you to 11Z and 22B.
        Step 5: You choose all of the left paths, leading you to 11B and 22C.
        Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
    :param network: dictionary that depicts the network
    :param directions: sequence of directions to take
    :return: number of steps needed to reach all final nodes '**Z'
    """
    print(f"Starting the route...")

    current_nodes = [k for k in network if k.endswith('A')]
    multiples = []

    for n in current_nodes:
        i = 0
        num_steps = 0
        while True:
            if i == len(directions):
                i = 0
            n = network[n][directions[i]]
            i += 1
            num_steps += 1
            if n.endswith('Z'):
                break
        print(f"number of steps: {num_steps}")
        multiples.append(num_steps)

    lcm = math.lcm(*multiples)
    print(f"Finished, number of steps (LCM): {lcm}")

    return lcm


def parse_input_file(input_file: str) -> Tuple[dict, str]:
    """
    Process all lines from the input file to extract data
    :param input_file: input file name with path
    :return:
    """
    with open(input_file, 'r') as file:
        contents = file.read()
        sections = contents.split("\n\n")

        directions = sections[0]

        print(f"directions: {directions}")

        num_nodes = 0
        first_node = ''

        for line in sections[1].split("\n"):
            if line == '':
                continue
            parts = line.split('=')
            node_name = parts[0].strip()
            if first_node == '':
                first_node = node_name
            # next_nodes = tuple(i.strip() for i in parts[1].strip().strip('()').split(','))
            next = parts[1].strip().strip('()').split(',')
            num_nodes += 1
            # network[node_name] = Node(node_name, next_nodes)
            network[node_name] = {"L": next[0].strip(), "R": next[1].strip()}
            print(f"node #{num_nodes}, name: {node_name}, next: {next}")

    print(network)
    # for node in network.values():
    #     print(node)

    return network, directions


def print_help_and_exit():
    """
    Print help and exit
    """
    print("Usage: python day8.py <part_number> <input_file>")
    print("\twhere <part_number> is one of: 1, 2 and <input_file> is the input data file with path")
    sys.exit(1)


def main(args) -> int:
    """
    Main function
    :return: the total winnings
    """
    # record the start time
    start_time = time.time()

    # reset the network dictionary
    global network
    network = {}

    if len(args) != 2:
        print_help_and_exit()

    part_number = int(args[0])

    network, directions = parse_input_file(args[1])

    if part_number == 1:
        num_steps = get_num_steps_first(network, directions)
    elif part_number == 2:
        num_steps = get_num_steps_second(network, directions)

    # DEBUG
    print(f"Steps required to reach the destination: {num_steps}")

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return num_steps


if __name__ == "__main__":
    main(sys.argv[1:])



