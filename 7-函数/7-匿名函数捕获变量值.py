#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-14 23:20 
# user: lixun
# filename: 匿名函数捕获变量值
# description:
#


def runing_binding():
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


def definition_bind():
    """
        使用 lambda 在声明时进行绑定,可以将参数定义设置为默认参数
    :return:
    """
    x = 10
    a = lambda y, x=x: x + y
    x = 20
    b = lambda y, x=x: x + y
    print(a(10))
    print(b(10))


def lambda_list_error():
    """
        lambda 使用不恰当,n 迭代的时最后一次输出的值,不是需要的么此从 0 开始迭代
    :return:
    """
    funcs = [lambda x: x + n for n in range(5)]
    for f in funcs:
        print(f(0))


def lambda_list_correct():
    """
        在 lambda 函数中指定默认参数输出迭代的最后一个值
    :return:
    """
    funcs = [lambda x, n=n: x + n for n in range(5)]
    for f in funcs:
        print(f(0))


def main():
    lambda_list_error()
    lambda_list_correct()


if __name__ == "__main__":
    main()
