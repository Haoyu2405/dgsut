import pytest

from pytest_study.calc import Calculator


class TestCalculator:

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print("结束测试")

    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.add
    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", [(1, 1, 2)])
    def test_add_int(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    # @pytest.mark.add
    @pytest.mark.P0
    @pytest.mark.parametrize("a,b,expect", [(-0.01, 0.02, 0.01), (10, 0.02, 10.02)])
    def test_add_float(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.add
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", [(1, 1, 2), (1, 99, 100)])
    def test_add_int_p1(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    # @pytest.mark.add
    @pytest.mark.P1
    @pytest.mark.parametrize("a,b,expect", [
        (98.99, 99, 197.99),
        (99, 98.99, 197.99),
        (-98.99, -99, -197.99),
        (99.01, 0, "参数大小超出范围"),
        (-99.01, -1, "参数大小超出范围"),
        (2, 99.01, "参数大小超出范围"),
    ])
    def test_add_float_p1(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect
