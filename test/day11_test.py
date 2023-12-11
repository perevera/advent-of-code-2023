from src.day11 import main as day11


def test_first_part_factor_two():
    """
    Assert the sample input gives the right value (part one, expansion factor 2)
    :return:
    """
    args = ['2', 'sample/sample-day11.txt']
    sum_distances = day11(args)
    assert sum_distances == 374


def test_second_part_factor_ten():
    """
    Assert the sample input gives the right value (part two, expansion factor 10)
    :return:
    """
    args = ['10', 'sample/sample-day11.txt']
    sum_distances = day11(args)
    assert sum_distances == 1030


def test_second_part_factor_hundred():
    """
    Assert the sample input gives the right value (part two, expansion factor 100)
    :return:
    """
    args = ['100', 'sample/sample-day11.txt']
    sum_distances = day11(args)
    assert sum_distances == 8410
