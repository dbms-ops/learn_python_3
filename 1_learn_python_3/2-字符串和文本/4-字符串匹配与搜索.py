#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/1 21:39
# @user: Administrator
# @fileName: 字符串匹配与搜索
# @description: 用于匹配或者搜索指定模式的文本
#

import re

def string_function():
    # 对于字面字符串常量可以使用字符串的基本方法
    text = "yeah, but no, but yeah, but no, but yeah"
    print(text == 'yeah')
    print(text.startswith('yeah'))
    print(text.endswith('no'))
    print(text.find('no'))


def string_re():
    text1 = '11/27/2012'
    text2 = 'Nov 27, 2012'
    # 使用 match 进行匹配,总是总字符串的开始进行匹配,如果需要查找任意位置,通过 findAll() 代替
    if re.match(r'\d+\/\d+/\d+',text1):
        print('yes')
    else:
        print('no')

    if re.match(r'\d+\/\d+/\d+',text2):
        print('yes')
    else:
        print('no')


def string_pre_building():
    date_pat = re.compile(r'\d+/\d+/\d+')
    text1 = '11/27/2012'
    if date_pat.match(text1):
        print('yes')
    else:
        print('no')

def string_pre_group():
    # 通过 () 进行分组捕获,可以更好的使用分组
    text1 = '11/27/2012'
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
    result = datepat.match(text1)
    print(result[0])
    print(result[1])
    print(result[2])

    # 迭代的方式进行匹配
    # 匹配可以使用 $ 进行精确匹配
    for m in datepat.finditer(text1):
        print(m.groups())

def main():
    string_pre_group()

if __name__ == '__main__':
    main()
    