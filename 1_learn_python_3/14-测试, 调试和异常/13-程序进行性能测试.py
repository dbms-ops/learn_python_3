#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/24 17:42
# @user: Administrator
# @fileName: 程序进行性能测试
# @description: 你的程序运行所花费的时间并做性能测试
#
# time python3 someprogram.py 测试程序执行的时间
# python3 -m cProfile someprogram.py 测试程序运行机器时间

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.perf_counter()
        r = func(*args,**kwargs)
        end = time.perf_counter()
        print('{}.{}:{}'.format(func.__module__, func.__name__,end-start))
        return r
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1



def main():
    countdown(1000000)


if __name__ == '__main__':
    main()
    