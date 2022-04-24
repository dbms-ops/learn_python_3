#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/21 21:45
# @user: Administrator
# @fileName: 定义上下文管理器的简单方法
# @description: 
# 

import time

from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f'{label}: {end - start}')


def main():
    with timethis('counting'):
        n = 10000000
        while n > 0:
            n -= 1


if __name__ == '__main__':
    main()
