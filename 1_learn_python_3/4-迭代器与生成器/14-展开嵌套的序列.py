#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/9 15:43
# @user: Administrator
# @fileName: 展开嵌套的序列
# @description: 将一个多层嵌套的序列,展开为一个单层列表
#   可以通过 yield from 语句递归生成器来解决这个问题
# ;;

from collections import Iterable


def flatten_better(items, ignore_types=(str, bytes)):
    """
    :param items:isinstance(x, Iterable) 检查某个元素是否是可迭代,yield from 就会返回所有子例程的值,最终返回一个不可迭代的对象
    :param ignore_types: ignore_types 和检测语句isinstance(x, ignore_types) 用来将字符串和字节排除在可迭代对象外，
    防止将它们再展开成单个的字符
    :return: 序列中的元素
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten_better(x)
        else:
            yield x


def flatten_ugly(items, ignore_bytes=(str, bytes)):
    """

    :param items: isinstance(x, Iterable) 检查某个元素是否是可迭代,yield from 就会返回所有子例程的值,最终返回一个不可迭代的对象
    :param ignore_bytes: ignore_types 和检测语句isinstance(x, ignore_types) 用来将字符串和字节排除在可迭代对象外,
        防止将它们再展开成单个的字符
    :return: 序列中的元素
    """
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_bytes):
            yield from flatten_ugly(x)
        else:
            yield x


def flatten_example():
    items = [1, 2, [3, 4, [5,(1,2,3,(5,6,(7,8))), 6], 7], 8]
    for x in flatten_better(items):
        print(x)
    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten_better(items):
        print(x)


def main():
    flatten_example()


if __name__ == '__main__':
    main()
