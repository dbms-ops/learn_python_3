#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/18 11:50
# @user: Administrator
# @fileName: 创建装饰器时保留函数元信息
# @description: 一个装饰器作用在某个函数上，但是这个函数的重要的元信息比如名字、文档字符串、注解和参数签名都丢失了
# 任何时候你定义装饰器的时候，都应该使用functools 库中的@wraps 装饰器来注解底层包装函数
#

import time
from functools import wraps


def timethis(func):
    """
        Decorator that reports the execution time.
        复制元信息是一个非常重要的部分,使用 @wraps，那么你会发现被装饰函数丢失了所有有用的信息
        @wraps 有一个重要特征是它能让你通过属性__wrapped__ 直接访问被包装函数
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


def main():
    pass


if __name__ == '__main__':
    main()
