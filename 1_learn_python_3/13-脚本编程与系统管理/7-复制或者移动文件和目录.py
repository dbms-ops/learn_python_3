#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 21:37
# @user: Administrator
# @fileName: 复制或者移动文件和目录
# @description: 复制或者移动文件或者目录,但是不调用 shell 命令
# 

import shutil


def ignore_pyc_files(filenames):
    return (for name in filenames if name.endswith('.pyc'))


def shutil_example(src, dest):
    # Copy src to dst. (cp src dst)
    shutil.copy(src, dest)

    # Copy files, but preserve metadata (cp -p src dst)
    shutil.copy(src, dest)

    # Copy directory tree (cp -R src dst)
    shutil.copytree(src, dest)

    # Move src to dst (mv src dst)
    shutil.move(src, dest)

    # 复制目录保留符号连接
    shutil.copytree(src, dest, symlinks=True)
    shutil.copytree(src, dest, ignore=ignore_pyc_files)


def main():
    pass


if __name__ == '__main__':
    main()
