#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/2 16:34
# @user: Administrator
# @fileName: 忽略大小写的字符串查找
# @description:
#    需要忽略大小写进行查找, 需要给 re 模块提供对应的标志
# ;
# 

import re


def string_ignore_case():
    text = 'UPPER 1  PYTHON,  23 lower python, 34563 Mixed  231 Python'
    result_digital = re.findall('\d{2,3}', text)
    print(result_digital)
    result_case = re.findall('python', text, flags=re.IGNORECASE)
    print(result_case)
    # 改例子在查找的时候忽略了大小写,再替换时,统一替换成小写,如果要按照对应的大小写进行替换,参考下面的方法
    print(re.sub('python', 'snake', text, flags=re.IGNORECASE))


def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


def main():
    string_ignore_case()
    text = 'UPPER 1  PYTHON,  23 lower python, 34563 Mixed  231 PyThon'
    result = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
    print(result)

if __name__ == '__main__':
    main()
