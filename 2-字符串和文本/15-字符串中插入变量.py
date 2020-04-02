#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/2 20:19
# @user: Administrator
# @fileName: 字符串中插入变量
# @description: 在内嵌的字符串中,插入变量
# 

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




def main():
    string_insert_value()
    s = '{name} has {n} messages.'
    a = Info('Guido',23)
    print(s.format_map(vars(a)))



if __name__ == '__main__':
    main()
    