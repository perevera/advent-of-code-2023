from src.day23 import main as day23


def test_first_part_one():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['sample/sample-day23.txt', '1']
    num = day23(args)
    assert num == 94


def test_first_part_two():
    """
    Assert the sample input gives the right value (part one, file two)
    :return:
    """
    args = ['sample/sample-day23.txt', '2']
    num = day23(args)
    assert num == 154
