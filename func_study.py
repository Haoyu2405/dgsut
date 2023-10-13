from __future__ import annotations


def blank_func():
    """
    这是一个空函数
    :return:
    """


blank_func()


def print_func():
    """
    这是一个打印的函数，打印固定的值
    :return:
    """
    print("Hogwarts")


print_func()

print("*" * 30)


def demo_func(a, b, c):
    print(a, b, c)


demo_func(b=2, a=1, c=3)

print("*" * 30)


def demo_func1(a, b, c, d: str = "123"):
    print(a, b, c, d)


demo_func1(b=2, a=1, c=3, d="abc")

print("*" * 30)


def calc_add(x: int | float, y: int | float) -> (int | float, bool):
    """
    加法运算
    :param x:
    :param y:
    :return: x+y
    """
    flag = True
    return x + y, flag


print(calc_add(1, 2))

print("*" * 30)


def print_demo(a, b, c, *args, **kwargs):
    print(a, b, c, args, kwargs)
    print()
    print(args)
    print()
    print(kwargs.get("e"))


print_demo(1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, e="abc")
