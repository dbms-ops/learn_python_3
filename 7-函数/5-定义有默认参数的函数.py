#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 21:49
# @user: Administrator
# @fileName: 定义有默认参数的函数
# @description: 想定义一个函数或者方法，它的一个或多个参数是可选的并且有一个默认值
# 在函数定义中给参数指定一个默认值，并放到参数列表最后
_no_value = object()


def spam(a, b, c=42):
    print(a, b, c)


def spam_example():
    spam(1, 2)
    spam(1, 2, 45)


def spam_1(a, b, d=None):
    """
        默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用 None 作为默认值
    :param a: 用来测试的参数，没有实际意义
    :param b: 用来测试的参数，没有实际意义
    :param d: 如果 d 为没有传递参数，默认为一个空列表，如果传递，应该传递一个列表，集合，字典
    :return:
    """
    if d is None:
        d = []
    print(a, b)
    print(d)


def spam_1_example():
    spam_1(1, 2, [3, 4, 5, 6, 7, 8, 9])


def spam_2(a, b, c=_no_value):
    """
        当不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来;
        默认参数的值应该是不可变的对象,应该是None，True，False，数字或字符串;
    :param a:
    :param b:
    :param c:
    :return:
    """
    if c is _no_value: print('No c value supplied')
    print(a, b)


def spam_2_example():
    spam_2(1, 2)
    spam_2(1, 2, 3)


def main():
    spam_2_example()


if __name__ == '__main__':
    main()
