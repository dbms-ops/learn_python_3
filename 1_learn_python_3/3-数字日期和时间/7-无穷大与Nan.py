#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 16:00 
# user: lixun
# filename: 无穷大与Nan
# description: 测试正无穷，负无穷，或者 Nan 的浮点数
#

import math


def create_float():
    a = float('inf')
    b = float('-inf')
    c = float('nan')
    print(a, b, c)


    print(math.isinf(a), math.isnan(c))


def main():
    create_float()


if __name__ == "__main__":
    main()
    