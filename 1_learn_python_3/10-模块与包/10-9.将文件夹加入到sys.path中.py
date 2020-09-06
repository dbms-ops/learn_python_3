#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 16:10
# @user: Administrator
# @fileName: 将文件夹加入到sys.path中
# @description: 无法导入你的Python 代码因为它所在的目录不在sys.path 里,
# 你想将添加新目录到Python 路径，但是不想硬链接到你的代码

import sys
from os.path import abspath,join,dirname

sys.path.insert(0,abspath(dirname(__file__)),'src')



def main():
    pass


if __name__ == '__main__':
    main()
    