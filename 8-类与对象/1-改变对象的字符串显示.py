#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 15:56
# @user: Administrator
# @fileName: 改变对象的字符串显示
# @description: 要改变一个实例的字符串表示，可重新定义它的__str__() 和__repr__() 方法
# 

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        """
            直接调用实例返回这个结果
        :return:
        """
        return 'return Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        """
            print 函数输出下列结果
        :return:
        """
        return '({0.x!s}, {0.y!s})'.format(self)

def pair_example():
    p = Pair(3, 4)
    p
    print(p)



def main():
    pair_example()


if __name__ == '__main__':
    main()
    