#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/20 20:03
# @user: Administrator
# @fileName: 捕获类的属性定义顺序
# @description: 自动记录的一个类中属性和方法定义的顺序,然后执行序列化,映射到数据库等操作
# 利用元类可以很容易的捕获类的定义信息, Ordered-Dict 来记录描述器的定义顺序;

from collections import OrderedDict

# A set of descriptors for various types
class Typed:
    _expected_type = type(None)
    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value,self._expected_type):
            raise TypeError('Excepted ' + str(self._expected_type))
        instance.__dict__[self._name] = value

class Integer(Typed):
    _expected_type = int

class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

# Metaclass that uses an OrderedDict for class body
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            value._name = name
            order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)
    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()






def main():
    pass


if __name__ == '__main__':
    main()
    