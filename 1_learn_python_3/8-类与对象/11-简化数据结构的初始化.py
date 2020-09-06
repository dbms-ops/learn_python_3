#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/17 18:07
# @user: Administrator
# @fileName: 简化数据结构的初始化
# @description: 一个基类中写一个公用的__init__() 函数
# 

import math


class Structure1:
    # Class variable that specifies expected fields
    # 定义基类用于支持位置参数
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments'".format(len(self._fields)))
        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Points(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


def point_args():
    s = Stock('ACME', 50, 91.1)
    print(s.name, s.shares, s.price)
    p = Points(2, 3)
    print(p.x, p.y)

    c = Circle(4.5)
    # s2 = Stock('ACME', 50)


class Structure2:
    """
        定义关键字参数, 用于将关键字参数设置为实例属性
    """
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError("Except {} arguments".format(self._fields))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name in self._fields[len(args)]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError("Invalid argument(s): {}".format(','.join(kwargs)))


def structure2_example():
    class Stock(Structure2):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 91.1)
    print(s1.name, s1.price, s1.shares)
    s2 = Stock('ACME', shares=50, price=91.1)
    print(s2.name, s2.price, s2.shares)
    s3 = Stock('ACME', shares=50, price=91.1, aa=1)
    print(s3.name, s2.shares, s3.price)

class Structure3:
    # Class variable that specifies expected fields
    """
        该类可以手动的添加一些额外的属性
    """
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError("Excepted {} arguments ".format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError("Duplicate values for {}".format(','.join(kwargs)))

def structure3_example():
    class Stock(Structure3):
        _fields = ['name','shares','price']

        s1 = Stock('ACME', 50, 91.1)
        s2 = Stock('ACME', 50, 91.1, date='8/2/2012')





def main():
    pass


if __name__ == '__main__':
    main()
