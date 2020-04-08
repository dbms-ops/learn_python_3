#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-08 23:09 
# user: lixun
# filename: 创建数据处理管道
# description: 通过类似于管道的方式迭代处理数据，对于大量的数据，不能够一次放入内存中；
#   通过生成器函数来实现管道；
# 

import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    '''
        Find all filenames in a directory tree that match a shell wildcard pattern
    '''
    for path, dir_list, file_list in os.walk(top):
        for name in fnmatch.filter(file_list, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    '''
        Open a sequence of filenames one at a time producing a file object. The file is closed immediately when
        proceeding to the next iteration.
    '''
    for filename in filenames:
        if str(filename).endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif str(filename).endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    '''
        Chain a sequence of iterators together into a single sequence.
    :param iterators:
    :return:
    '''
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    '''
        Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# 将上面的函数连接起来创建一个管道
def create_pipe_link():
    lognames = gen_find('access-log*', 'www')
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    for line in pylines:
        print(line)


def main():
    pass


if __name__ == "__main__":
    main()
