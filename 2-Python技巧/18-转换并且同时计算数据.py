#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/31 17:48
# @user: Administrator
# @fileName: 转换并且同时计算数据
# @description: 对于数据首先进行转换,过滤之后在执行 聚集 函数[sum min max]
#   可以通过生成器表达式来进行计算;;
import os


def square_sum():
    nums = [1, 2, 3, 4, 5, 6]
    s = sum(x * x for x in nums)
    print(s)


def find_py_file(dirs):
    files = os.listdir(dirs)
    if any(name.endswith('.py') for name in files):
        print('There be python!')
    else:
        print('Sorry, no python.')

    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))


def main():
    find_py_file('/data/')


if __name__ == '__main__':
    main()
