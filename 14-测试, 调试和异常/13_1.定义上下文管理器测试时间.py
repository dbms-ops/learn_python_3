#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/24 17:51
# @user: Administrator
# @fileName: 13_1.定义上下文管理器测试时间.py
# @description: 
#

from contextlib import contextmanager
import time


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{}: {}'.format(label, end - start))


def main():
    with timeblock('counting'):
        n = 1000000
        while n > 0:
            n -= 1


if __name__ == '__main__':
    main()
