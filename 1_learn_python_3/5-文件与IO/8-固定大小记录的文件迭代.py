#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 13:15 
# user: lixun
# filename: 固定大小记录的文件迭代
# description: 在一个固定长度记录或者数据块的集合上面进行迭代，而不是在一个文件中一行一行进行迭代，使用 iter 和 functools.partial()
#   函数
# 

from functools import partial

RECORD_SIZE = 32

def open_file():
    """
        文件的读取按照一个固定的长度来进行，而不是一行一行的进行迭代， iter()函数当传递给它一个可调用对象和一个标记值时，会创建一个
        迭代器，迭代器会一致调用传入的可调用对象直到它返回标记值为止，迭代就会终止；
        函数 partital 创建一个每次被调用时从文件中读取固定数目字节的可调用对象，b''表示到达文件结尾时的返回值
    :return:
    """
    with open('somefile.data', 'rb') as f:
        records = iter(partial(f.read, RECORD_SIZE), b'')





def main():
    pass


if __name__ == "__main__":
    main()
    