from src.day10 import main as day10


def test_first_part():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['1', 'sample/sample-day10.txt']
    farthest = day10(args)
    assert farthest == 8


# def test_second_part():
#     """
#     Assert the sample input gives the right value (part two)
#     :return:
#     """
#     args = ['2', 'sample/sample-day10.txt']
#     num_steps = day10(args)
#     assert num_steps == 2

