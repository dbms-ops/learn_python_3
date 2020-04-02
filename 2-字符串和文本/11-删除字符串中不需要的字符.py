#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/2 17:52
# @user: Administrator
# @fileName: 删除字符串中不需要的字符
# @description: 删除字符串任意位置不需要的字符
#
# ;
#
import re


def string_strip():
    # Whitespace stripping
    s = ' hello world \n'
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    # Character stripping
    t = '-----hello====='
    print(t.lstrip("-"))

    # strip只能够对于左右两边的字符串去掉不需要的字符,无法对于字符串中间的字符进行替换
    s = ' hello   world \n'
    print(s.replace(' ',''))
    print(re.sub('\s+',' ',s))


def file_read(filename):
    # 多行文本读取方式;
    with open(filename) as f:
        lines = (line.strip() for line in f)
        for line in lines:
            print(line)


def main():
    string_strip()


if __name__ == '__main__':
    main()
    