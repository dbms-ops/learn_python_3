#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/21 20:06
# @user: Administrator
# @fileName: args和kwargs的强制参数签名
# @description: 一个函数或方法，它使用*args 和**kwargs 作为参数，这样使得它比较通用， 但有时候你想检查传递进来的参数是不是某个你想要的类型
# 对任何涉及到操作函数调用签名的问题，你都应该使用inspect 模块中的签名特性, Signature Parameter
#

from inspect import Signature, Parameter
import inspect


def parms_example():
    parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
             Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=24),
             Parameter('z', Parameter.POSITIONAL_OR_KEYWORD, default=None)
             ]

    sig = Signature(parms)
    print(sig)


def func(*args, **kwargs):
    parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
             Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=24),
             Parameter('z', Parameter.POSITIONAL_OR_KEYWORD, default=None)
             ]

    sig = Signature(parms)
    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


# Example use
class Stock(Signature):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


def stock_example():
    print(inspect.signature(Stock))
    s_1 = Stock('ACME', 100, 490.1)


def main():
    stock_example()


if __name__ == '__main__':
    main()
