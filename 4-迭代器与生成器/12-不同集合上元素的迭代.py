#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-08 22:51 
# user: lixun
# filename: 不同集合上元素的迭代
# description: 对于多个不同容器中的对象执行相同的操作，避免在代码的重复性循环
#   itertools.chain() 可以用来简化任务，接受一个可迭代对象列表作为输入，返回一个迭代器；
#
# ；

from itertools import chain


def chain_example():
    # 循环首先遍历a，其次遍历b
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']
    for x in chain(a, b):
        print(x)
    # 对于不同集合中的所有元素执行某些操作
    print('\n')
    active_item = {1, 2, 3, 4}
    inactive_item = {'a', 'b', 'c', 'd'}
    for item in chain(active_item, inactive_item):
        print(item)


"""
itertools.chain() 接受一个或多个可迭代对象作为输入参数，然后创建一个迭 代器，依次连续的返回每个可迭代对象中的元素；
比先将序列合并再迭代要 高效的多；

# Inefficent：a + b 操作会创建一个全新的序列并要求 a 和 b 的类型一致
for x in a + b: ...
# Better：输入序列非常大的时候会很省内存；适合于迭代对象类型不一样的时候
for x in chain(a, b): ...
"""


def main():
    chain_example()


if __name__ == "__main__":
    main()
