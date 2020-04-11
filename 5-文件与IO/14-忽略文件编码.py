#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 21:09 
# user: lixun
# filename: 忽略文件编码
# description:  使用原始文件名执行文件 I/O 操作，文件名并没有经过系统默认编码去解码或者编码过；
#   ；
#
import sys
import os


def file_read_write():
    """

    :return:
    """
    with open("/tmp/data", 'w') as f:
        f.write('Spicy')
    print(os.listdir('.'))

    print(os.listdir(b'.'))  # Note: byte string
    with open(b'jalapen\xcc\x83o.txt') as f:
        print(f.read())


def main():
    print(sys.getfilesystemencoding())


if __name__ == "__main__":
    main()
