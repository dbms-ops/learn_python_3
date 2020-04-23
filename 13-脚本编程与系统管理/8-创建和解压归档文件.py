#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 21:46
# @user: Administrator
# @fileName: 创建和解压归档文件
# @description: 需要创建或解压常见格式的归档文件（比如.tar, .tgz 或.zip）
# 
import shutil

shutil.unpack_archive('Python-3.3.0.tgz')

shutil.make_archive('py33','zip','Python-3.3.0')


def main():
    pass


if __name__ == '__main__':
    main()
    