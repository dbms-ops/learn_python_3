#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-06 20:22 
# user: lixun
# filename: 跳过可迭代对象的开始部分
# description: 遍历一个可迭代对象，但是需要跳过开始的某些元素
# itertools 模块中提供一些函数可以完成这些类似的任务，例如：itertools.dropwhile()，需要传递一个函数和一个可迭代对象，丢弃原有序列
# 中 函数判定为 False 的元素；

from itertools import dropwhile
from itertools import islice


def open_file():
    with open('/etc/passwd') as f:
        for line in f:
            print(line, end='')


def open_file_skip_line():
    # 返回函数指定为 False 的函数
    i = 0
    with open('/etc/passwd') as f:
        for line in dropwhile(lambda line: str(line).startswith('#'), f):
            print(line, end='')
            i += 1
    print(i)


def skip_list():
    # 指定跳过元素的的个数
    item = ['a', 'b', 'c', 1, 4, 6, 15]
    for x in islice(item, 3, None):
        print(x)


def not_suggest_example():
    # 这是常见的写法,但是是不建议的写法
    with open('/etc/passwd') as f:
        while True:
            line = next(f, '')
            if not line.startswith('#'):
                break
        while True:
            print(line, end='')
            line = next(f, None)


def not_suggest_example_1():
    # 这种写法，不仅仅会跳过开头的行，并且会跳过文件里面其他的 # 开头注释的行
    with open('/etc/passwd') as f:
        lines = (line for line in f if not line.startswith('#'))
        for line in lines:
            print(line, end='')


def main():
    skip_list()


if __name__ == "__main__":
    main()
