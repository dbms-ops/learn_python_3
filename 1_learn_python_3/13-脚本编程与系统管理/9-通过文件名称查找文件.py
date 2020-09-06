#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 21:52
# @user: Administrator
# @fileName: 通过文件名称查找文件
# @description: 查找文件，可使用os.walk() 函数，传一个顶级目录名给它
# 
import os
import sys


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


def main():
    findfile(sys.argv[1], sys.argv[0])


if __name__ == '__main__':
    main()
