from pytest_study.test_simple import func


def setup_module():
    print("我的module级别的初始化")


def teardown_module():
    print("我的module级别的清理")


def setup_function():
    print("我的function级别的初始化")


def teardown_function():
    print("我的function级别的清理")


def test_answer():
    actual = func(3)
    print(f"得到的实际结果为{actual}")
    assert actual == 4


def test_answer2():
    actual = func(6)
    print(f"得到的实际结果为{actual}")
    assert actual == 9


class TestFunc:

    def setup_class(self):
        print("我的class级别的初始化")

    def teardown_class(self):
        print("我的class级别的清理")

    def setup(self):
        print("我的方法级别的初始化")

    def teardown(self):
        print("我的方法级别的清理")

    def test_answer(self):
        actual = func(3)
        print(f"得到的实际结果为{actual}")
        assert actual == 4

    def test_answer1(self):
        actual = func(6)
        print(f"得到的实际结果为{actual}")
        assert actual == 8

    def test_answer3(self):
        actual = func(7)
        print(f"得到的实际结果为{actual}")
        assert actual == 8
