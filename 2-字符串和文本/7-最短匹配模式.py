#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/2 17:21
# @user: Administrator
# @fileName: 最短匹配模式
# @description: 正则匹配默认是按照贪婪算法进行匹配的,也就是按照最长撇配原则进行匹配,有时候需要按照最短方式进行匹配
#
import re


def string_shorted():
    # 字符串的目的时匹配被 "" 包含的文本, 下面两个例子说明了结果不是期望的
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    print(str_pat.findall(text1))

    text2 = 'Computer says "no." Phone says "yes."'
    print(str_pat.findall(text2))

    # 通过 ? 来修正匹配模式,按照非贪婪模式进行匹配
    str_pat = re.compile(r'\"(.*?)\"')
    print(str_pat.findall(text2))


def main():
    string_shorted()


if __name__ == '__main__':
    main()
    