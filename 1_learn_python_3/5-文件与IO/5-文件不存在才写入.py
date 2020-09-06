#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 12:23 
# user: lixun
# filename: 文件不存在才写入
# description: 向一个文件中写入数据，前提是这个文件必须不存在，不允许覆盖已有文件的内容；
#     使用 open 函数中的 x 模式来解决这个问题；
# 

import os


def open_file_not_exists():
    with open('/tmp/somefile.txt', 'wt') as f:
        f.write('Hello \n')

    with open("/tmp/somefile.txt", 'xt') as f:
        f.write('Hello, \n')


def open_if_file_exists():
    if not os.path.exists("/tmp/somefile.txt"):
        with open("/tmp/somefile.txt", "wt") as f:
            f.write("Hello world\n")
    else:
        print('File already exists')


def main():
    open_file_not_exists()


if __name__ == "__main__":
    main()
