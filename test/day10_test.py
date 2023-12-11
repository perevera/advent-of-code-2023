from src.day10 import main as day10


def test_first_part():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['sample/sample-day10-1.txt']
    farthest, _ = day10(args)
    assert farthest == 8


def test_second_part_one():
    """
    Assert the sample input gives the right value (part two, file one)
    :return:
    """
    args = ['sample/sample-day10-2-1.txt']
    _, num_points = day10(args)
    assert num_points == 4


def test_second_part_two():
    """
    Assert the sample input gives the right value (part two, file two)
    :return:
    """
    args = ['sample/sample-day10-2-2.txt']
    _, num_points = day10(args)
    assert num_points == 8


def test_second_part_three():
    """
    Assert the sample input gives the right value (part two, file three)
    :return:
    """
    args = ['sample/sample-day10-2-3.txt']
    _, num_points = day10(args)
    assert num_points == 10
