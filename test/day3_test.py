import unittest
from src.day3 import main as day3


def test_first_part():
    """
    Assert the sample input gives the right total (first part)
    :return:
    """
    sum_parts, _ = day3('sample/sample-day3.txt')
    assert sum_parts == 4361


def test_second_part():
    """
    Assert the sample input gives the right total (second part)
    :return:
    """
    _, sum_gear_ratios = day3('sample/sample-day3.txt')
    assert sum_gear_ratios == 467835

# def test_second_sample():
#     """
#     Assert the second sample input gives the right total
#     :return:
#     """
#     _, sum_powers = day2('sample/sample-day2.txt')
#     assert sum_powers == 2286
