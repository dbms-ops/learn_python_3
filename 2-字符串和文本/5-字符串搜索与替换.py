#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/2 10:54
# @user: Administrator
# @fileName: 字符串搜索与替换
# @description: 在字符串中搜索和匹配指定的文本模式
#
#   ;

import re
from calendar import month_abbr

def string_replace():
    # 对于字符串字面量,直接使用 str.replace()方法进行替换
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.replace('yeah','yep'))
    # 对于复杂模式的匹配,请使用 re 模块的 sub()函数
    # sub(1,2,3):
    sub()
    # 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字
    # 比如\3 指向前面模式的捕获组号
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))

def string_callback():
    # 对于相同模式的替换使用编译加快性能
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.sub(r'\3-\1-\2', text))


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return "{} {} {}".format(m.group(2), mon_name, m.group(3))



def main():
    text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    print(datepat.sub(change_date, text))


if __name__ == '__main__':
    main()
    