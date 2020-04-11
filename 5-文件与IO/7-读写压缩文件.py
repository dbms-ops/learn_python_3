#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 13:01 
# user: lixun
# filename: 读写压缩文件
# description: 读写一个 gzip 或者 bz2 格式的压缩文件
#   gzip() 和 bz2() 模块可以比较方便的处理这些文件
# ；；

import gzip
import bz2


def open_gzip_read():
    """
        打开 gzip 格式的文件
    :return:
    """
    with gzip.open('somefile.gz', 'rt') as f:
        text = f.read()


def open_bz2_read():
    """
        打开 gzip 格式的文件
    :return:
    """
    with bz2.open('somefile.bz2', 'rt') as f:
        text = f.read()


def open_gzip_write():
    """
        打开一个 gzip 格式的文件用于写入数据
    :return:
    """
    with gzip.open('somefile.gz', 'wt', compresslevel=9) as f:
        f.write('text')


def open_bz2_write():
    """
        打开一个 bz2 格式的文件用于写入数据, 对于二进制数据的操纵使用 rb 或者 wb， 在读写数据时，需要指定对应的模式，默认使用二进制
        格式打开，
    :return:
    """
    with bz2.open('somefile.bz2', 'wt') as f:
        f.write('text')

def open_file_has_open():
    """
        函数 bz2 和 gzip 可以用于在一个已经存在的，并且以二进制模式打开的文件上面
    :return:
    """
    f = open('somefile.gz', 'rb')
    with gzip.open(f, 'rt') as g:
        text = g.read()



def main():
    pass


if __name__ == "__main__":
    main()
