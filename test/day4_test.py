import unittest
from src.day4 import main as day4


def test_first_part():
    """
    Assert the sample input gives the right total (first part)
    :return:
    """
    total_wins, _ = day4('sample/sample-day4.txt')
    assert total_wins == 13


def test_second_part():
    """
    Assert the sample input gives the right total (first part)
    :return:
    """
    _, total_cards = day4('sample/sample-day4.txt')
    assert total_cards == 30


