import unittest
from src.day5 import main as day5


def test_first_part():
    """
    Assert the sample input gives the right minimum location (first part)
    :return:
    """
    min_location, _ = day5('sample/sample-day5.txt')
    assert min_location == 35


def test_second_part():
    """
    Assert the sample input gives the right minimum location (second part)
    :return:
    """
    _, min_location = day5('sample/sample-day5.txt')
    assert min_location == 46


