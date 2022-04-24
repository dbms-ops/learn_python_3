#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/9 18:01
# @user: Administrator
# @fileName: 读取文本数据
# @description: 文件内容读取是要给很常见的操作
# 

import sys

def read_file(filename):
    """
        Read the entire file as a single string
    :param filename:
    :return:
    """
    with open(filename, 'rt') as f:
        f.read()

    """
        Iterate over the lines of the file
    """
    with open(filename, 'rt') as f:
        pass

def write_file(filename):
    """
        向文件中写入内容,会清空之前的数据, 如果是文件中追加内容使用 at 模式
    :param filename:
    :return:
    """
    with open(filename, 'wt') as f:
        f.write('1112344')
        f.write('1334124')

    """
        将 print 语句重定向到文件中
    """
    with open(filename, 'wt', encoding='utf-8', errors='ignore', newline='\n') as f:
        # 获取操作系统的编码方式
        print(sys.getdefaultencoding(), file=f)
        print('line2', file=f)



def main():
    print(sys.getdefaultencoding())


if __name__ == '__main__':
    main()
    