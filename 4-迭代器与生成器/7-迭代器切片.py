#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-06 16:52 
# user: lixun
# filename: 迭代器切片
# description:
#       得到一个由迭代器生成的切片对象，但是标准的切片操作无法做到
#       函数 itertools.islice() 是用于迭代器和生成器进行切片操作;
#   迭代器和生成器不能够使用标准的切片操作，因为长度未知，无法实现索引，函数 islice() 返回生成指定元素的迭代器，
#   通过遍 历并丢弃直到切片开始索引位置的所有元素，然后才开始一个个的返回元素，并直到切片结束索引位置;
#   islice() 会消耗掉传入的迭代器中的数据，迭代器是不可逆的；

import itertools


def count(n):
    while True:
        yield n
        n += 1


def count_slice():
    c = count(0)
    print(c[10:20])


def main():
    c = count(0)
    for x in itertools.islice(c, 10, 20):
        print(x)


if __name__ == "__main__":
    main()
