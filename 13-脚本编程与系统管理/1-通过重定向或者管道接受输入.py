#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 20:48
# @user: Administrator
# @fileName: 通过重定向或者管道接受输入
# @description: 脚本接受任何用户认为最简单的输入方式,将命令行的输出通过管道传递给该脚本、重定向文件到该脚本，或在命令行中传递一个文件名
# 或文件名列表给该脚本,
# 

import fileinput

def file_input():
    with fileinput.input() as f_input:
        for line in f_input:
            print(line, end='')


def main():
    file_input()


if __name__ == '__main__':
    main()
    