#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 20:47
# @user: Administrator
# @fileName: 读写二进制数组数据
# @description: 读写一个二进制数组的结构化数据到Python 元组中
#

from struct import Struct


def write_records(records, format, f):
    """
        Write a sequence of tuples to a binary file of structures
    :param records:
    :param format:
    :param f:
    :return:
    """
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def write_records_example(filename='/tmp/data.b'):
    """
        调用 write_records 行数将records 写入到文件中
    :param filename:
    :return:
    """
    records = [
        (1, 2.3, 4.5),
        (6, 7.8, 9.0),
        (12, 13.4, 56.7)
    ]
    with open(filename, 'wb') as f:
        write_records(records, '<idd', f)


def read_record(format, f):
    """
        从 records 文件中读取对应的数据文件
    :param format:
    :param f:
    :return:
    """
    read_struct = Struct(format)
    chuncks = iter(lambda: f.read(read_struct.size), b'')
    return (read_struct.unpack(chunck) for chunck in chuncks)


def read_record_example(filename='/tmp/data.b'):
    """
        调用 read_record 文件,按照record大小读取文件
    :param filename:
    :return:
    """
    with open(filename, 'rb') as f:
        for rec in read_record('<idd', f):
            print(rec)


def unpack_records(format, data):
    """
        一次读取文件中的所有内容
    :param format:
    :param data:
    :return:
    """
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


def unpack_resords_example(filename='/tmp/data.b'):
    """
        调用 unpack_records 函数,一次性读取里面的所有内容
    :param filename:
    :return:
    """
    with open(filename, 'rb') as f:
        data = f.read()

    for rec in unpack_records('<idd', data):
        print(rec)


def main():
    unpack_resords_example()


if __name__ == '__main__':
    main()
