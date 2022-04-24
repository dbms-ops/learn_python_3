#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/21 20:41
# @user: Administrator
# @fileName: 在定义的时候初始化类的成员
# @description: 在类被定义的时候就初始化一部分类的成员，而不是要等到实例被创建;
# ;
# 

import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args, **kwargs):
        if len(args) != len(cls._fields):
            raise ValueError(f'{len(cls._fields)} argumens required')
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']


def main():
    s = Stock('ACME', 50, 91.1)
    print(s)
    print(s[0])
    print(s.shares)


if __name__ == '__main__':
    main()
