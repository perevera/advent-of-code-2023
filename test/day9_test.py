from src.day9 import main as day9


def test_first_part():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['1', 'sample/sample-day9.txt']
    sum_values = day9(args)
    assert sum_values == 114


def test_second_part():
    """
    Assert the sample input gives the right value (part two)
    :return:
    """
    args = ['2', 'sample/sample-day9.txt']
    num_steps = day9(args)
    assert num_steps == 2

