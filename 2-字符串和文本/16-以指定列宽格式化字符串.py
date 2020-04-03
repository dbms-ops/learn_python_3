#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/3 15:20
# @user: Administrator
# @fileName: 以指定列宽格式化字符串
# @description: 对于以下长字符串使用指定的列宽重新进行格式化
# 

import os
import textwrap


def string_textwrap():
    s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
    the eyes, not around the eyes, don't look around the eyes, \
    look into my eyes, you're under."

    print(textwrap.fill(s,60))
    print(textwrap.fill(s,40))
    print('\n\n')
    print(textwrap.fill(s,os.get_terminal_size().columns/2,initial_indent=' '))


def main():
    string_textwrap()
    print(os.get_terminal_size().columns)


if __name__ == '__main__':
    main()
    