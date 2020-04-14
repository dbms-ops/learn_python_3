#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 21:26
# @user: Administrator
# @fileName: 只接受关键字参数的函数
# @description: 函数的某些参数强制使用关键字参数传递
# 

def recv(maxsize, *, block):
    """
        通过使用 *, 强制 * 之后的变量使用关键字参数, * 之前的变量可以使用位置参数,也可以使用关键字参数, 通过关键字可以使得位置参数的含义
        更加清晰,
    :param maxsize:
    :param block:
    :return:
    """
    'Receives a message'
    print(maxsize, block)


def recv_example():
    """
        调用 recv 验证结果是否满足需求
    :return:
    """
    recv(maxsize=134, block=13)
    # recv(1024,True)

def minimum(*value, clip=None):
    m = min(value)
    if clip is not None:
        m = clip if clip > m else m
    return m

def minimum_example():
    print(minimum(1, 5, 2, -5, 10))
    print(minimum(1, 5, 2, -5, 10, clip=0))



def main():
    minimum_example()


if __name__ == '__main__':
    main()
