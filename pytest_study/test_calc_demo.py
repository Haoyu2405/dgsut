import sys

import pytest


class Calc:

    def add(self, a, b):
        """
        计算两个数相加
        :param a:
        :param b:
        :return:
        """
        print(f"计算的结果为: {a + b}")
        return a + b

    def div(self, a, b):
        """
        计算两个数相除
        :param a:
        :param b:
        :return:
        """
        if b != 0:
            print(f"计算的结果为: {a / b}")
            return a / b
        else:
            print("计算的发生错误")
            raise ZeroDivisionError


class TestCalc:

    def setup_class(self):
        """
        类初始化
        :return:
        """
        self.calc = Calc()

    @pytest.mark.add
    def test_add1(self):
        a = 10
        b = 20
        actual = self.calc.add(a, b)
        assert actual == 30

    @pytest.mark.add
    def test_add2(self):
        a = 1
        b = 2
        actual = self.calc.add(a, b)
        assert actual == 3

    @pytest.mark.add
    def test_add3(self):
        a = 0.1
        b = 0.9
        actual = self.calc.add(a, b)
        assert actual == 1

    @pytest.mark.div
    def test_div1(self):
        a = 10
        b = 20
        actual = self.calc.div(a, b)
        assert actual == 0.5

    @pytest.mark.div
    def test_div2(self):
        a = 1
        b = 2
        actual = self.calc.div(a, b)
        assert actual == 0.5

    @pytest.mark.div
    def test_div3(self):
        a = 0.1
        b = 0.4
        actual = self.calc.div(a, b)
        assert actual == 0.25

    @pytest.mark.skip
    def test_mul(self):
        a = 0.1
        b = 0.4
        actual = self.calc.mul(a, b)
        assert actual == 0.04

    @pytest.mark.skipif(sys.platform != "win32", reason="该用例只能在win上运行")
    def test_demo1(self):
        print("system is windows")

    @pytest.mark.skipif(sys.platform == "win32", reason="该用例不能在win上运行")
    def test_demo2(self):
        print("this case can not run in Windows")
