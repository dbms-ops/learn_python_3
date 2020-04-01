#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/1 20:00
# @user: Administrator
# @fileName: 字符串开头或者结尾匹配
# @description: 通过指定的文本模式去检查字符串的开头或者接维;
#       使用 startswith 或者 endswith
#       ;


import re

def text_find_with():
    # 查找指定接维方式的字符串
    # startswith 和 endswith 参数必须是元组,传递参数时,使用元组进行传递
    filename = "spam.txt"
    print(filename.endswith('txt'))
    # 指定方式开头
    url = "http://www.python.org"
    print(url.startswith('http'))


def file_name_with():
    # 列表解析查找指定开头或者指定结尾的文件
    filenames = [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
    need_file = [name for name in filenames if name.endswith(('.c', '.h')) and name.startswith(('M','s')) ]
    print("the result is: ", need_file)
    print(any(name.endswith('.py') for name in filenames))

def string_split():
    filename = 'spam.txt'
    print(filename[-4:] == ".txt")
    url = 'http://www.python.org'
    print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

def string_math():
    # 使用 re match 来进行字符串匹配
    url = 'http://www.python.org'
    result = re.match('http:|https:|ftp:', url)
    print(result.pos)

def main():
    string_math()


if __name__ == '__main__':
    main()
    