import unittest
from src.day3 import main as day3


def test_first_sample():
    """
    Assert the second sample input gives the right total
    :return:
    """
    sum_parts = day3('sample/sample-day3.txt')
    assert sum_parts == 4361


# def test_second_sample():
#     """
#     Assert the second sample input gives the right total
#     :return:
#     """
#     _, sum_powers = day2('sample/sample-day2.txt')
#     assert sum_powers == 2286
