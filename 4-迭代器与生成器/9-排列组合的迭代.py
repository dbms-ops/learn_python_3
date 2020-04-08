#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-06 21:57 
# user: lixun
# filename: 排列组合的迭代
# description:
#   迭代遍历一个集合中的所有可能的排列或者组合
#   利用itertools 模块提供的三个函数来解决这类问题;
#       itertools.permutations(): 接受一个集合,并且产生一个元组序列,每个元素未一个可能的排列;
#       ；

from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement


def itertools_permutations():
    # 计算序列中元素的所有排列
    items = ['a', 'b', 'c']
    # 得到序列的所有排列
    for p in permutations(items):
        print(p)
    # 得到指定长度的序列
    for p in permutations(items, 2):
        print(p)

def itertools_combinations():
    # 计算一个序列里面可能的所有组合
    items = ['a', 'b', 'c']
    for c in combinations(items,2):
        print(c)
    # 排列中的元素允许重复出现多次
    for c in combinations_with_replacement(items, 3):
        print(c)


def main():
    itertools_combinations()


if __name__ == "__main__":
    main()
    