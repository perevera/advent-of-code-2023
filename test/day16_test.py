from src.day16 import main as day16


def test_first_part_one():
    """
    Assert the sample input gives the right value (part one)
    :return:
    """
    args = ['sample/sample-day16.txt']
    num = day16(args)
    assert num == 46
