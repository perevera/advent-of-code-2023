import sys
import time
from typing import Union, Tuple, List
from enum import Enum


# Define an enumeration class
class HandTypes(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE = 4
    FULL_HOUSE = 5
    FOUR = 6
    FIVE = 7


card_strength = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


def is_lower_or_equal(hand_1, hand_2):
    """
    Compare if hand 1 is less or equal than hand 2
    :return:
    """
    if hand_1[0] < hand_2[0]:
        return True
    elif hand_1[0] > hand_2[0]:
        return False
    else:
        for i in range(5):
            if card_strength.index(hand_1[1][i]) < card_strength.index(hand_2[1][i]):
                return True
            elif card_strength.index(hand_1[1][i]) > card_strength.index(hand_2[1][i]):
                return False

    return True     # default value if hands are exactly equal


def is_lower_or_equal_two(hand_1, hand_2):
    """
    Compare if hand 1 is less or equal than hand 2
    :return:
    """
    if hand_1[0] < hand_2[0]:
        return True
    elif hand_1[0] > hand_2[0]:
        return False
    else:
        for i in range(5):
            if card_strength.index(hand_1[1][i]) < card_strength.index(hand_2[1][i]):
                return True
            elif card_strength.index(hand_1[1][i]) > card_strength.index(hand_2[1][i]):
                return False

    return True     # default value if hands are exactly equal


def quicksort_zipped(zipped_list, callback_function):
    """
    Quick sort of the list of hand types (recursive)
    :return: the two lists sorted by the values of the first one (hand types values)
    """
    if len(zipped_list) <= 1:
        return zipped_list
    else:
        pivot = zipped_list[0]

        # less_than_pivot = [x for x in zipped_list[1:] if x[0] <= pivot[0]]
        less_than_pivot = [x for x in zipped_list[1:] if callback_function(x, pivot)]
        # greater_than_pivot = [x for x in zipped_list[1:] if x[0] > pivot[0]]
        greater_than_pivot = [x for x in zipped_list[1:] if not callback_function(x, pivot)]

        return (quicksort_zipped(less_than_pivot, callback_function) +
                [pivot] +
                quicksort_zipped(greater_than_pivot, callback_function))


def compute_hand_types(hands: List[str]) -> List[int]:
    """
    Compute the types of hands (first method)
    :param hands: list of hands
    :return: list of hand types corresponding to the input hands
    """
    hand_types = list()

    for hand in hands:
        cards_possible = [0 for _ in range(14)]
        for h in hand:
            cards_possible[card_strength.index(h)] += 1
        cards_actual = [x for x in cards_possible if x > 0]

        # if 5 in cards_possible:
        if len(cards_actual) == 1:
            hand_types.append(HandTypes.FIVE)
        elif len(cards_actual) == 2:
            if 4 in cards_possible:
                hand_types.append(HandTypes.FOUR)
            else:
                hand_types.append(HandTypes.FULL_HOUSE)
        elif len(cards_actual) == 3:
            if 2 in cards_possible:
                hand_types.append(HandTypes.TWO_PAIR)
            else:
                hand_types.append(HandTypes.THREE)
        elif len(cards_actual) == 4:
            hand_types.append(HandTypes.ONE_PAIR)
        else:
            hand_types.append(HandTypes.HIGH_CARD)

    ret = [t.value for t in hand_types]

    return ret


def compute_hand_types_two(hands: List[str]) -> List[int]:
    """
    Compute the types of hands (second method)
    :param hands: list of hands
    :return: list of hand types corresponding to the input hands
    """
    hand_types = list()

    for hand in hands:
        cards_possible = [0 for _ in range(14)]
        num_jokers = 0
        for h in hand:
            cards_possible[card_strength.index(h)] += 1
            if h == 'J':
                num_jokers += 1

        cards_actual = [x for x in cards_possible if x > 0]

        if len(cards_actual) == 1:      # repoker
            hand_types.append(HandTypes.FIVE)
        elif len(cards_actual) == 2:    # maybe poker
            if 4 in cards_possible:
                if num_jokers == 1:
                    hand_types.append(HandTypes.FIVE)
                else:
                    hand_types.append(HandTypes.FOUR)
            else:
                if num_jokers == 2:
                    hand_types.append(HandTypes.FIVE)
                elif num_jokers == 1:
                    hand_types.append(HandTypes.FOUR)
                else:
                    hand_types.append(HandTypes.FULL_HOUSE)
        elif len(cards_actual) == 3:
            if 2 in cards_possible:
                if num_jokers == 2:
                    hand_types.append(HandTypes.FOUR)
                elif num_jokers == 1:
                    hand_types.append(HandTypes.FULL_HOUSE)
                else:
                    hand_types.append(HandTypes.TWO_PAIR)
            else:
                if num_jokers > 0:
                    hand_types.append(HandTypes.FOUR)
                else:
                    hand_types.append(HandTypes.THREE)
        elif len(cards_actual) == 4:
            if num_jokers > 0:
                hand_types.append(HandTypes.THREE)
            else:
                hand_types.append(HandTypes.ONE_PAIR)
        else:
            if num_jokers == 1:
                hand_types.append(HandTypes.ONE_PAIR)
            else:
                hand_types.append(HandTypes.HIGH_CARD)

    ret = [t.value for t in hand_types]

    return ret


def part_one(hands: List[str], bids: List[int]) -> int:
    """
    Main function for part one to calculate the total winnings
    :param hands
    :param bids
    :return: the total winnings
    """
    hand_types = compute_hand_types(hands)

    # DEBUG
    for h, t in zip(hands, hand_types):
        print(f"hand: {h} -> type: {t}")

    # zip the two lists together
    zipped_lists = list(zip(hand_types, hands, bids))
    # apply quicksort to the zipped list based on the values of the first list
    sorted_hand_types = quicksort_zipped(zipped_lists, is_lower_or_equal)
    print(sorted_hand_types)

    tot_wins = 0

    for i, val in enumerate(sorted_hand_types):
        tot_wins += (i+1) * val[2]

    print(tot_wins)
    return tot_wins


def part_two(hands: List[str], bids: List[int]) -> int:
    """
    Main function for part one to calculate the total winnings
    :param hands
    :param bids
    :return: the total winnings
    """
    hand_types = compute_hand_types_two(hands)

    # DEBUG
    for h, t in zip(hands, hand_types):
        print(f"hand: {h} -> type: {t}")

    # zip the two lists together
    zipped_lists = list(zip(hand_types, hands, bids))
    # apply quicksort to the zipped list based on the values of the first list
    sorted_hand_types = quicksort_zipped(zipped_lists, is_lower_or_equal_two)

    for h, i, b in sorted_hand_types:
        print(f"hand: {i}, bid: {b}")

    tot_wins = 0

    for i, val in enumerate(sorted_hand_types):
        tot_wins += (i+1) * val[2]

    print(tot_wins)
    return tot_wins


def parse_input_file(input_file: str) -> Tuple[List[str], List[int]]:
    """
    Process all lines from the input file to extract data
    :return:
    """
    hands = list()
    bids = list()

    # process lines from input file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Check if the last line is empty
    if lines and lines[-1].strip() == '':
        lines.pop()

    for line in lines:
        fields = line.strip().split()
        hands.append(fields[0])
        bids.append(int(fields[1]))

    return hands, bids


def print_help_and_exit():
    """
    Print help and exit
    """
    print("Usage: python day6.py <part_number> <input_file>")
    print("\twhere <part_number> is one of: 1, 2 and <input_file> is the input data file with path")
    sys.exit(1)


def main(args) -> int:
    """
    Main function
    :return: the total winnings
    """
    tot_wins = -1

    # record the start time
    start_time = time.time()

    if len(args) != 2:
        print_help_and_exit()

    part_number = int(args[0])

    hands, bids = parse_input_file(args[1])

    for hand, bid in zip(hands, bids):
        print(f"hand: {hand}, bid: {bid}")

    if part_number == 1:
        tot_wins = part_one(hands, bids)
    elif part_number == 2:
        tot_wins = part_two(hands, bids)

    # record the end time
    end_time = time.time()

    # calculate the duration
    duration = end_time - start_time

    # print the duration
    print(f"Script execution took {duration:.2f} seconds")

    return tot_wins


if __name__ == "__main__":
    main(sys.argv[1:])



