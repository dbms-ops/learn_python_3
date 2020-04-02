#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/2 17:45
# @user: Administrator
# @fileName: 多行匹配模式
# @description: 跨越多行进行文本匹配;
#   ;
# 

import re

def string_multi():
    text = """
         /* this is a comment */
        /* this is a
        multiline comment */
    """
    commnet = re.compile(r'/\*((?:.)*?)\*/',flags=re.DOTALL)
    print(commnet.findall(text))


def main():
    string_multi()


if __name__ == '__main__':
    main()
    