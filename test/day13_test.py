from src.day13 import main as day13


def test_first_part_one():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['sample/sample-day13.txt']
    tot = day13(args)
    assert tot == 405


def test_first_part_two():
    """
    Assert the sample input gives the right value (part one, second sample file)
    :return:
    """
    args = ['sample/sample-day13-2.txt']
    tot = day13(args)
    assert tot == 709


def test_first_part_three():
    """
    Assert the sample input gives the right value (part one, third sample file)
    :return:
    """
    args = ['sample/sample-day13-3.txt']
    tot = day13(args)
    assert tot == 1


# def test_second_part_factor_ten():
#     """
#     Assert the sample input gives the right value (part two, expansion factor 10)
#     :return:
#     """
#     args = ['10', 'sample/sample-day13.txt']
#     sum_distances = day13(args)
#     assert sum_distances == 1030
#
#
# def test_second_part_factor_hundred():
#     """
#     Assert the sample input gives the right value (part two, expansion factor 100)
#     :return:
#     """
#     args = ['100', 'sample/sample-day13.txt']
#     sum_distances = day13(args)
#     assert sum_distances == 8410
