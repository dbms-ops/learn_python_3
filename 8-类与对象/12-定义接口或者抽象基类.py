#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/18 10:23
# @user: Administrator
# @fileName: 定义接口或者抽象基类
# @description: 定义一个接口或者抽象类, 通过执行例行检查来确保子类实现了某些特定的方法
#

from abc import ABCMeta, abstractmethod

class IStream(metaclass=ABCMeta):
    """
        顶一个一个抽象类,抽象类不能够被直接初始化,可以让别的类继承,并且实现特定的继承方法
    """
    @abstractmethod
    def read(self,maxbytes=1):
        pass

    @abstractmethod
    def write(self, data):
        pass





def main():
    pass


if __name__ == '__main__':
    main()
    