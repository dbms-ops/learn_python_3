#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/15 20:29
# @user: Administrator
# @fileName: 减少可调用对象的参数个数
# @description: 减少某个函数的参数个数, 可以使用functools.partial(),函数允许你给一个或多个参数设置固定的值，减少接下来被调用时的参数个数
# 

from functools import partial
import math


def spam(a, b, c, d):
    print(a, b, c, d)


def use_spam_partial():
    """
        通过 partial 将第一个参数固定为 1
    :return:
    """
    spam_example_1 = partial(spam, 1)
    spam_example_1(2, 3, 4)

    # 通过关键字参数 固定 d 的值为43
    spam_example_2 = partial(spam, d=43)
    spam_example_2(1, 2, 3)

    spam_example_3 = partial(spam, 5, 6, d=43)
    spam_example_3(13)


def distance(p1, p2):
    """
        计算两个坐标点之间的距离,
    :param p1: 第一个点的坐标
    :param p2: 第二个点的坐标
    :return: 防护两个点之间的距离差
    """
    x_1, y_1 = p1
    x_2, y_2 = p2

    return math.hypot(x_2 - x_1, y_2 - y_1)


def point_sorted():
    """
        计算 点和基点的距离,并且将这些点进行排序
    :return:
    """
    pt = (4, 3)
    points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    points.sort(key=partial(distance, pt))
    print(points)


def main():
    point_sorted()


if __name__ == '__main__':
    main()
