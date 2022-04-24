#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 21:30
# @user: Administrator
# @fileName: 创建新的类或者实例属性
# @description: 创建一个新的拥有一些额外功能的实例属性类型
#   描述器是Python一个很高级的功能,可以实现Python的大多数底层特性,描述器只能够在类级别被定义,不能够为每个实例单独定义

# Descriptor attribute for an integer type-checked attribute
class Integer:
    """
        一个描述器就是一个实现了三个核心的属性访问操作(get, set, delete) 的类，
        分别为__get__() 、__set__() 和__delete__() 这三个特殊的方法
    """

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return self if instance is None else instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not instance(value, int):
            raise TypeError("Except an int")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    """
        使用一个描述器，需将这个描述器的实例作为类属性放到一个类的定义中,，所有对描述器属性(比如x 或y) 的访问会被__get__() 、__set__()
        和__delete__() 方法捕获到。
    """
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def point_example():
    p = Point(2, 3)

    # Calls Point.x.__get__(p,Point)
    print(p.x)
    # Calls Point.y.__set__(p, 5)
    p.y = 5
    # Calls Point.x.__set__(p, 2.3)
    p.x = 2.3


def main():
    point_example()


if __name__ == '__main__':
    main()
