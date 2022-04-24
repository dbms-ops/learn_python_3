#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 21:49
# @user: Administrator
# @fileName: 使用延迟计算属性
# @description: 将一个只读属性定义成一个property，并且只在访问的时候才会计算结果,一旦被访问后，你希望结果值被缓存起来，不用每次都去计算
#

import math

class lazyproperty:
    """
        通过类定义一个延迟属性
    """
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = self.func(instance)
        setattr(instance, self.func.__name__, value)
        return value

class Circle:

    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self, radius):
        print("Computing ares")
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('computing perimeter')
        return 2 ** math.pi * self.radius



def main():
    c = Circle(4.0)
    print(c.radius, c.area)
    print(c.perimeter)
    print(c.perimeter)



if __name__ == '__main__':
    main()
    