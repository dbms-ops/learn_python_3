#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/9 16:37
# @user: Administrator
# @fileName: 迭代器代替 while 无限循环
# @description: 使用迭代器代替 while 无限循环
#   ;

import sys

def readers_ugly(s,CHUNCKSIZE):
    # 通常接受网络数据的方式, 不建议
    while True:
        data = s.recv(CHUNCKSIZE)
        if data == b'':
            break
        print(data)

def readers_better(s, CHUNCKSIZE):
    for chunk in iter(lambda : s.recv(CHUNCKSIZE), b''):
        print(chunk)


def reader_files():
    with open('/etc/passwd', 'rt') as f:
        # iter()函数 接受一个可选的callable 对象和一个标记(结尾) 值作为输入参数;
        for chunck in iter(lambda :f.read(10), ''):
            n = sys.stdout.write(chunck)


def main():
    reader_files()


if __name__ == '__main__':
    main()
    