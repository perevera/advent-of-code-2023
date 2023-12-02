import unittest
from src.day2 import main as day2


def test_first_sample():
    """
    Assert the second sample input gives the right total
    :return:
    """
    sum_ids, _ = day2('sample/sample-day2.txt')
    assert sum_ids == 8


def test_second_sample():
    """
    Assert the second sample input gives the right total
    :return:
    """
    _, sum_powers = day2('sample/sample-day2.txt')
    assert sum_powers == 2286
