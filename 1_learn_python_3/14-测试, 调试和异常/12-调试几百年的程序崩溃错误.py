#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/24 17:37
# @user: Administrator
# @fileName: 调试基本的程序崩溃错误
# @description: 你的程序因为某个异常而崩溃，运行python3 -i someprogram.py 可执行简单的调试
#

import sys
import traceback


def func(n):
    return n + 10

def func_example():
    try:
        func('hello')
    except:
        print('**** AN ERROR OCCURRED ****')
        traceback.print_exc(file=sys.stderr)

def sample(n):
    if n > 0:
        sample(n-1)
    else:
        traceback.print_stack(file=sys.stderr)


def main():
   sample(5)

if __name__ == '__main__':
    main()
    