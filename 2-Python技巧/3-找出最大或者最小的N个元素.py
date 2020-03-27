#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/27 17:14
# @user: Administrator
# @fileName: 找出最大或者最小的N个元素.py
# @description: 通过 heapq 模块的函数找出最大或者最小的 N 个元素
# 
import heapq


def find_n_max():
    nums = [1, 2, 3, 4, 5, 7, 12, 32, 4, 1, 56, 7, 67]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(4, nums))


def find_n_key_pattern():
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    # lambda s: s['price'] 用于返回 {'name': 'ACME', 'shares': 75, 'price': 115.65} 的 price 字段
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)


def main():
    find_n_key_pattern()


if __name__ == '__main__':
    main()
