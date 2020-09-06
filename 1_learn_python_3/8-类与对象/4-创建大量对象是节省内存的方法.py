#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 17:17
# @user: Administrator
# @fileName: 创建大量对象是节省内存的方法
# @description: 程序创建数百万对象用来节省内存
#

class Date:
    """
        定义__slots__ 后, Python 就会为实例使用一种更加紧凑的内部表示. 实例通过一个很小的固定大小的数组来构建，
        而不是为每个实例定义一个字典，这跟元组或列表很类似。
        它可以作为一个封装工具来防止用户给实例增加新的属性, __slots__更多的是用来作为一个内存优化工具;
    """
    __slots__ = ['year','month','day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day =day




def main():
    pass


if __name__ == '__main__':
    main()
    