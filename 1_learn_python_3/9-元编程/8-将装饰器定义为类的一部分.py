#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/20 17:11
# @user: Administrator
# @fileName: 将装饰器定义为类的一部分
# @description: 在类中定义装饰器,并且将其定义子其他函数或者方法上面
#
# ;
from functools import wraps


class A:
    # Decorator as an instance method
    def decorator_1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)

        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator_2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 2")
            return func(*args, **kwargs)

        return wrapper


def instance_method_example():
    a = A()

    @a.decorator_1
    def spam():
        pass


def class_method_example():
    @A.decorator_2
    def grok():
        pass


def main():
    instance_method_example()
    class_method_example()


if __name__ == '__main__':
    main()
