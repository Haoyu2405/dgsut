def func(x):
    """
    被测函数
    :param x:
    :return:
    """
    return x + 1


def test_answer():
    actual = func(3)
    assert actual == 4


class TestFunc:

    def test_answer(self):
        actual = func(3)
        assert actual == 4

    def test_answer1(self):
        actual = func(6)
        assert actual == 8
