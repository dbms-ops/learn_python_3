#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 20:02 
# user: lixun
# filename: 内存映射的二进制文件
# description: 内存映射一个二进制文件到一个可变数组中，目的是为了随机访问它的内容或者原地做些修改
# 使用 mmap 模块来内存映射文件

import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    print(size)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


def create_size_file():
    size = 1000000
    with open('/tmp/data', 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x00')


def reassign_slice():
    data = memory_map(filename='/tmp/data')
    print(len(data))
    print(data[:10])
    data[0:11] = b'Hello World'
    data.close()


def verify_change():
    with open('/tmp/data', 'rb') as f:
        print(f.read(11))

    with memory_map('/tmp/data') as m:
        print(len(m))
        print(m[:11])


def main():
    verify_change()


if __name__ == "__main__":
    main()
