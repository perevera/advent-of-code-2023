import unittest
from src.day1 import main as day1


def test_first_sample():
    """
    Assert the second sample input gives the right total
    :return:
    """
    tot = day1('sample/sample-day1-1.txt')
    assert tot == 142


def test_second_sample():
    """
    Assert the second sample input gives the right total
    :return:
    """
    tot = day1('sample/sample-day1-2.txt')
    assert tot == 281
