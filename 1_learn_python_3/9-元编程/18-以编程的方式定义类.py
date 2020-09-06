#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/21 20:28
# @user: Administrator
# @fileName: 以编程的方式定义类
# @description:
# 

import types


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}


def main():
    Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
    Stock.__module__ = __name__
    s = Stock('ACME', 50, 91.1)
    print(s.name)
    print(type(Stock))


if __name__ == '__main__':
    main()
