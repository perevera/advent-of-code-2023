import unittest
from src.day2 import main as day2


def test_first_part():
    """
    Assert we get the right sum of ids with the sample data
    :return:
    """
    sum_ids, _ = day2('sample/sample-day2.txt')
    assert sum_ids == 8


def test_second_part():
    """
    Assert we get the right sum of powers with the sample data
    :return:
    """
    _, sum_powers = day2('sample/sample-day2.txt')
    assert sum_powers == 2286
