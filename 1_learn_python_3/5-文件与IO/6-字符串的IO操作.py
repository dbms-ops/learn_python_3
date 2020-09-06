#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 12:34 
# user: lixun
# filename: 字符串的IO操作
# description: 操作类文件对象的程序来操作文本或二进制字符串；
#   io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据；；
# 

import io


def string_IO():
    """
        使用 io.StringIO() 类创建类文件对象操作字符串数据
    :return:
    """
    s = io.StringIO()
    s.write('Hello, world\n')
    print('This is a test file', file=s)
    print(s.getvalue())

    s = io.StringIO('Hello World\n')
    print(s.read(4))

    print(s.read())


def string_bytes():
    """
        io.BytesIO() 类创建类文件对象操作字符串数据
    :return:
    """
    s = io.BytesIO()
    s.write(b'binary data')
    print(s.getvalue())


def main():
    string_bytes()


if __name__ == "__main__":
    main()
