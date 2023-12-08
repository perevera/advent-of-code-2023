import unittest
from src.day8 import main as day8


def test_first_part_first_sample():
    """
    Assert the sample input gives the right value (part one, first sample file)
    :return:
    """
    args = ['1', 'sample/sample-day8-1-1.txt']
    num_steps = day8(args)
    assert num_steps == 2


def test_first_part_second_sample():
    """
    Assert the sample input gives the right value (part one, second sample file)
    :return:
    """
    args = ['1', 'sample/sample-day8-1-2.txt']
    num_steps = day8(args)
    assert num_steps == 6


def test_second_part():
    """
    Assert the sample input gives the right value (part two)
    :return:
    """
    args = ['2', 'sample/sample-day8-2.txt']
    num_steps = day8(args)
    assert num_steps == 6


# def test_second_part():
#     """
#     Assert the sample input gives the right value (part two)
#     :return:
#     """
#     args = ['2', 'sample/sample-day8-1-1.txt']
#     num_wins = day8(args)
#     assert num_wins == 5905
