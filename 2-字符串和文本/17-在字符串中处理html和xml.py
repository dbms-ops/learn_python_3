#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/3 15:27
# @user: Administrator
# @fileName: 在字符串中处理html和xml
# @description: 
# 

import html

def html_escape():
    s = 'Elements are written as "<tag>text</tag>".'
    print(s)
    print(html.escape(s))
    print(html.escape(s,quote=False))


def main():
    html_escape()


if __name__ == '__main__':
    main()
    