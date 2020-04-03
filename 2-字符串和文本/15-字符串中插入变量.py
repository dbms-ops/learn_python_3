#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/2 20:19
# @user: Administrator
# @fileName: 字符串中插入变量
# @description: 在内嵌的字符串中,插入变量
# 

import sys

def string_insert_value():
    s = '{name} has {n} messages.'
    print(s.format(name='Guido',n=37))
    name='Guido'
    n=37
    print(s.format_map(vars()))

class Info:
    def __init__(self,name, n):
        self.name = name
        self.n = n

def lose_value():
    """
    对于 format 以及 format_map() 不能够很好的处理变量缺失的情况

    """
    s = '{name} has {n} messages.'
    s.format(name="Guido")
    print(s)

class safesub(dict):
    """
    用于防止 key 找不到
    """
    def __missing__(self, key):
        return '{' + key + '}'

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))



def main():
    string_insert_value()
    s = '{name} has {n} messages.'
    a = Info('Guido',23)
    print(s.format_map(vars(a)))
    # lose_value()
    name= "lixun"
    print(s.format_map(safesub(vars())))
    print(sub("hello {name}"))
    print(sub('You have {n} messages.'))
    print(sub('Your favorite color is {color}'))





if __name__ == '__main__':
    main()
    