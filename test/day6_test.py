import unittest
from src.day6 import part_one, part_two, part_two_recursive


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

def test_second_part_recursive():
    """
    Assert the sample input gives the right value (part two, recursive method)
    :return:
    """
    num_wins = part_two_recursive('sample/sample-day6.txt')
    assert num_wins == 71503
