#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/18 10:50
# @user: Administrator
# @fileName: 实现自定义容器
# @description: 实现一个自定义的类来模拟内置的容器类功能，比如列表和字典
#   collections 定义了很多抽象基类, collections.Iterable

import collections
import bisect


class SortedItems(collections.Sequence):
    """
        collections.Sequence 继承队列 需要自己实现某些函数
    """
    def __init__(self, initial=None):
        self.__items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, item):
        return self.__items[item]

    def __len__(self):
        return len(self.__items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self.__items, item)


def SortedItems_example():
    """
        调用 SortedItems 用于实现验证自定义实现调用
    :return:
    """
    items = SortedItems([5, 1, 3])
    print(list(items))
    print(list(items))
    print(items[0], items[-1])
    items.add(8)
    print(list(items))


def main():
    SortedItems_example()


if __name__ == '__main__':
    main()
