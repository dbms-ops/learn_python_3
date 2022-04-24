#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 13:25 
# user: lixun
# filename: 读取二进制数据到可变缓冲区中
# description: 直接读取二进制数据到可变缓冲区中，而不需要任何的中间复制操作；或者原地修改数据并且写回到一个文件中;
#       使用文件对象的 readinto() 方法;
# 

import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


def read_into_buffer_example():
    with open('/tmp/sample.bin', 'wb') as f:
        f.write(b'Hello world')
    buf = read_into_buffer('/tmp/sample.bin')
    print(buf)

    with open('/tmp/newsample.bin', 'wb') as f:
        f.write(buf)


def bytearray_example():
    record_size = 32  # size of each record
    buf = bytearray(record_size)
    with open('somefile', 'rb') as f:
        while True:
            n = f.readinto(buf)
            if n < record_size:
                break


def main():
    read_into_buffer_example()


if __name__ == "__main__":
    main()
