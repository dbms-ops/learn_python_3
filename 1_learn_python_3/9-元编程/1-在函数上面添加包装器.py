#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/18 11:40
# @user: Administrator
# @fileName: 在函数上面添加包装器
# @description: 函数上添加一个包装器，增加额外的操作操作处理
# 

import time
from functools import wraps


def timethis(func):
    """
        Decorator that reports the execution time.
        一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, "The time is: ", end - start)
        return result

    return wrapper


def timethis_example():
    """
        @timethis 类似于: countdown = timethis(countdown)
    :return:
    """
    @timethis
    def count_down(n):
        """

        :return:
        """
        while n > 0:
            n -= 1

    count_down(10000000)


def main():
    timethis_example()


if __name__ == '__main__':
    main()
