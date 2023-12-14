from src.day13 import main as day13


def test_first_part_one():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['sample/sample-day13.txt']
    tot, _ = day13(args)
    assert tot == 405


def test_first_part_two():
    """
    Assert the sample input gives the right value (part one, second sample file)
    :return:
    """
    args = ['sample/sample-day13-2.txt']
    tot, _ = day13(args)
    assert tot == 709


def test_first_part_three():
    """
    Assert the sample input gives the right value (part one, third sample file)
    :return:
    """
    args = ['sample/sample-day13-3.txt']
    tot, _ = day13(args)
    assert tot == 1


def test_second_part_one():
    """
    Assert the sample input gives the right value (part two)
    :return:
    """
    args = ['sample/sample-day13.txt']
    _, tot = day13(args)
    assert tot == 400
