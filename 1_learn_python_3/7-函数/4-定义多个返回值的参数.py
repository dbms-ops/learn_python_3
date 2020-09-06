#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 21:46
# @user: Administrator
# @fileName: 定义多个返回值的参数
# @description: 构造一个可以返回多个值的函数
#  最简单的方式直接返回一个元组

def myfunc():
    """
        myfun() 看上去返回了多个值，实际上是先创建了一个元组然后返回;
        实际上我们使用的是逗号来生成一个元组
    :return:
    """
    return 1, 2, 3


def main():
    a, b, c = myfunc()
    print(a, b, c)


if __name__ == '__main__':
    main()
