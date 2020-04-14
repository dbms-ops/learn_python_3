#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-14 23:20 
# user: lixun
# filename: 匿名函数捕获变量值
# description:
# 


def main():
    """
        变量 X 在运行时绑定，底下两个函数输出都是 30，在运行时绑定值，而不 是定义时就绑定，这跟函数的默认值参数定义是不同的；
    :return:
    """
    x = 10
    a = lambda y: x + y
    x = 20
    b = lambda y: x + y
    print(a(10))
    print(b(10))


if __name__ == "__main__":
    main()
