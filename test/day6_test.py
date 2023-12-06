import unittest
from src.day6 import part_one, part_two


def test_first_part():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    num_wins = part_one('sample/sample-day6.txt')
    assert num_wins == 288


def test_second_part():
    """
    Assert the sample input gives the right value (part two)
    :return:
    """
    num_wins = part_two('sample/sample-day6.txt')
    assert num_wins == 71503
