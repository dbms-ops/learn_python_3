#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 21:57 
# user: lixun
# filename: 将字节写入文本文件
# description: 在文本模式打开的文件中写入原始的字节数据；
#   将字节数据直接写入文件的缓冲区中；
# 

import sys

def write_bytes_to_str():
    # print(sys.stdout.write(b'Hello World\n'))
    print(sys.stdout.buffer.write(b'Hello \n'))



def main():
    write_bytes_to_str()


if __name__ == "__main__":
    main()
    