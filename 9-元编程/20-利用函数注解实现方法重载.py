#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/21 21:01
# @user: Administrator
# @fileName: 利用函数注解实现方法重载
# @description: 已经学过怎样使用函数参数注解，那么你可能会想利用它来实现基于类型的方法重载
# 

class Spam:
    def bar(self, x: int, y: int):
        print('Bar 1:', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


def spam_example():
    s = Spam()
    s.bar(2, 3)
    s.bar('hello')


def main():
    spam_example()


if __name__ == '__main__':
    main()
