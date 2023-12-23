from src.day18 import main as day18


def test_first_part_one():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['sample/sample-day18.txt']
    num, _ = day18(args)
    assert num == 62


def test_first_part_two():
    """
    Assert the sample input gives the right value (part one, file two)
    :return:
    """
    args = ['sample/sample-day18-2.txt']
    num, _ = day18(args)
    assert num == 25


def test_first_part_three():
    """
    Assert the sample input gives the right value (part one, file three)
    :return:
    """
    args = ['sample/sample-day18-3.txt']
    num, _ = day18(args)
    assert num == 23


def test_first_part_four():
    """
    Assert the sample input gives the right value (part one, file four)
    :return:
    """
    args = ['sample/sample-day18-4.txt']
    num, _ = day18(args)
    assert num == 62
