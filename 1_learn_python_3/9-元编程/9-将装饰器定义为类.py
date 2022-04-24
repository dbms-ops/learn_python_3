#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/20 17:19
# @user: Administrator
# @fileName: 将装饰器定义为类
# @description: 使用一个装饰器去包装函数，但是希望返回一个可调用的实例;
#   为了将装饰器定义成一个实例，你需要确保它实现了__call__() 和__get__() 方法
# ;

import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        return self if instance is None else types.MethodType(self, instance)


def example():
    @Profiled
    def add(x, y):
        return x + y

    class Spam:
        @Profiled
        def bar(self, x):
            print(self, x)

    print(add(2, 3))
    print(add(4, 5))
    print(add.ncalls)


def main():
    example()

if __name__ == '__main__':
    main()
