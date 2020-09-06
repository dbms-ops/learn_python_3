#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 20:35 
# user: lixun
# filename: 测试文件是否存在
# description: 测试一个文件或者目录是否存在
# 

import os

def os_path_exists():
    # 使用 os.path 进行文件测试，需要注意和考虑的是文件权限的问题，尤其是在获取文件元数据的时候
    print(os.path.exists('/home/passwd'))
    print(os.path.exists('/tmp/spam'))

    print(os.path.isfile('/etc/passwd'))
    print(os.path.isdir('/etc/passwd'))

    print(os.path.islink('/usr/local/bin/python3'))
    print(os.path.realpath('/usr/local/bin/python3'))

    print(os.path.getsize('/etc/passwd'))
    print(os.path.getmtime("/etc/passwd"))



def main():
    pass


if __name__ == "__main__":
    main()
    