from src.day12 import main as day12


def test_first_part():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['1', 'sample/sample-day12.txt']
    tot = day12(args)
    assert tot == 21


# def test_second_part_factor_ten():
#     """
#     Assert the sample input gives the right value (part two, expansion factor 10)
#     :return:
#     """
#     args = ['10', 'sample/sample-day12.txt']
#     sum_distances = day12(args)
#     assert sum_distances == 1030
#
#
# def test_second_part_factor_hundred():
#     """
#     Assert the sample input gives the right value (part two, expansion factor 100)
#     :return:
#     """
#     args = ['100', 'sample/sample-day12.txt']
#     sum_distances = day12(args)
#     assert sum_distances == 8410
