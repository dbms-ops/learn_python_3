#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/18 11:08
# @user: Administrator
# @fileName: 在类中定义多个构造器
# @description: 通过 __init__() 之外的方法初始化函数
# 

import time


class Date:
    """
        方法一：使用类方法
        # Primary constructor
    """

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


def class_date_example():
    """

    :return:
    """
    # Primary
    a = Date(2012, 12, 21)
    print(a.year, a.month, a.day)
    print(a.today)


def main():
    class_date_example()


if __name__ == '__main__':
    main()
