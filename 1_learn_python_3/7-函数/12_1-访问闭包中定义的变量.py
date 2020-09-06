#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 15:25
# @user: Administrator
# @fileName: 访问闭包中定义的变量
# @description: 通过闭包模拟类的实现
#

import sys


class ClosureInstance():
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


def stack_example():
    s = Stack()
    s.push(10)
    s.push(20)
    s.push('hello')
    print(len(s))

    print(s.pop())
    print(s.pop())

def main():
    stack_example()


if __name__ == '__main__':
    main()
