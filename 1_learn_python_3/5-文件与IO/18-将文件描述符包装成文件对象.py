#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 22:02 
# user: lixun
# filename: 将文件描述符包装成文件对象
# description: 对应于操作系统上一个已经打开的 I/O 通道，比如文件，管道，套接字的整型文件描述符，包装成一个更高层的Python文件对象；
#   一个文件描述符和一个打开的普通文件是不一样的。文件描述符仅仅是一个由操 作系统指定的整数，用来指代某个系统的 I/O 通道。
#   如果你碰巧有这么一个文件描述 符，你可以通过使用 open() 函数来将其包装为一个 Python 的文件对象。
#   你仅仅只需要使用这个整数值的文件描述符作为第一个参数来代替文件名即可；
#   ；
# 

import os


def os_open(filename='/tmp/filename.txt'):
    """
        文件一共被打开了两次，当高层的文件对象被关闭或者被破坏时，底层的文件描述符也会被关闭。可以给 open 函数传递一个 closefd=False
    :param filename:
    :return:
    """
    # open a low-level file descriptor
    fd = os.open(filename, os.O_WRONLY | os.O_CREAT)
    with open(fd, 'wt', closefd=False) as f:
        f.write('Hello world\n')


def main():
    os_open()


if __name__ == "__main__":
    main()
