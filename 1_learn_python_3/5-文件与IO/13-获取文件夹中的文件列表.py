#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 20:42 
# user: lixun
# filename: 获取文件夹中的文件列表
# description: 获取文件系统中某个目录的所有文件列表
# 使用 函数 os.listdir() 获取某个目录中的文件列表

import os
import glob
from fnmatch import fnmatch


def os_listdir(dirname):
    """
        函数返回目录中的所有文件列表，包括所有文件，子目录，符号连接。可以使用函数来进行列表推导
    :return:
    """
    file_name = [name for name in os.listdir(dirname)
                 if os.path.isfile(os.path.join(dirname, name))]
    dirnames = [name for name in os.listdir(dirname)
                if os.path.isdir(os.path.join(dirname, name))]
    pyfiles = [name for name in os.listdir(dirname)
               if name.endswith('.py')]
    pyfiles = glob.glob(f'{dirname}/*.py')

    pyfiles = [name for name in os.listdir(dirname)
               if fnmatch(name, '*.py')]


def get_file_stats():
    pyfiles = glob.glob('*.py')

    # Get file sizes and modification dates
    name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name))
                    for name in pyfiles]

    for name, size, mtime in name_sz_date:
        print(name, size, mtime)
    # Alternative: Get file metadata
    file_metadata = [(name, os.stat(name)) for name in pyfiles]
    for name, meta in file_metadata:
        print(name, meta.st_size, meta.st_mtime)


def main():
    pass


if __name__ == "__main__":
    main()
