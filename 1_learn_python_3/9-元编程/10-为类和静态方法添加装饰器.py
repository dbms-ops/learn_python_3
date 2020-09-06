#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/20 17:32
# @user: Administrator
# @fileName: 为类和静态方法添加装饰器
# @description: 给类或静态方法提供装饰器是很简单的，不过要确保装饰器在@classmethod 或 @staticmethod 之前
# 
import time
from functools import wraps


# A simple decorator
def time_this(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r

    return wrapper


# Class illustrating application of the decorator to different kinds of methods

class Spam:
    @time_this
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @time_this
    def class_method(cls, n):
        print(n)
        while n > 0:
            n -= 1

    @staticmethod
    @time_this
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


def example():
    s = Spam()
    print(s.instance_method(100000))
    print(Spam.class_method(10000))
    print(Spam.static_method(10000))


def main():
    example()


if __name__ == '__main__':
    main()
