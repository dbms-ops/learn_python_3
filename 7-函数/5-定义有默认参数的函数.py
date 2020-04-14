#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 21:49
# @user: Administrator
# @fileName: 定义有默认参数的函数
# @description: 想定义一个函数或者方法，它的一个或多个参数是可选的并且有一个默认值
# 在函数定义中给参数指定一个默认值，并放到参数列表最后


def spam(a, b, c=42):
    print(a, b, c)


def spam_1(a, b, d=None):
    """
        默认参数是一个可修改的容器比如一个列表、集合或者字典，可以使用 None 作为默认值
    :param a:
    :param b:
    :param d:
    :return:
    """
    if b is None:
        b = []


def spam_2(a, b, c='_no_value'):
    """
        你并不想提供一个默认值，而是想仅仅测试下某个默认参数是不是有传递进来,参考
    :param a:
    :param b:
    :param c:
    :return:
    """
    if c is '_no_value':
        print('No c value supplied')


def main():
    spam_2(11, 2)


if __name__ == '__main__':
    main()
