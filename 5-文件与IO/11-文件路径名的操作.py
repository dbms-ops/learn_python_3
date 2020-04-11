#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 20:24 
# user: lixun
# filename: 文件路径名的操作
# description: 使用路径名来获取文件名，目录名，绝对路径等等
#   使用os.path模块中的函数来操作路径名
import os


def os_path_example():
    path = "/tmp/lixun/data.csv"
    print(os.path.basename(path))

    print(os.path.dirname(path))

    print(os.path.join("root", 'data', os.path.basename(path)))

    path = "~/Data/data.csv"
    print(os.path.expanduser(path))

    print(os.path.splitext(path))


def main():
    os_path_example()


if __name__ == "__main__":
    main()
