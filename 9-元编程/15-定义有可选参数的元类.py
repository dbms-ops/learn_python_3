#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/21 20:01
# @user: Administrator
# @fileName: 定义有可选参数的元类
# @description: 定义各个袁磊,允许类定义是提供可选参数,控制或者配置类型的创建过程
#

from abc import ABCMeta, abstractmethod
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass





def main():
    pass


if __name__ == '__main__':
    main()
    