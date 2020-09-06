#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 21:08
# @user: Administrator
# @fileName: 获取终端的大小
# @description: 当前终端的大小以便正确的格式化输出
# 
import os


def get_size():
    sz = os.get_terminal_size()
    print(sz)
    print(sz.columns, sz.lines)


def main():
    get_size()


if __name__ == '__main__':
    main()
