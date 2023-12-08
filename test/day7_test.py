import unittest
from src.day7 import main as day7


def test_first_part():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['1', 'sample/sample-day7.txt']
    num_wins = day7(args)
    assert num_wins == 6440


def test_second_part():
    """
    Assert the sample input gives the right value (part two)
    :return:
    """
    args = ['2', 'sample/sample-day7.txt']
    num_wins = day7(args)
    assert num_wins == 5905
