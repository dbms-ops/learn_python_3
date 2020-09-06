#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 16:10 
# user: lixun
# filename: 分数运算
# description: 分数运算
# 

from fractions import Fraction


def fractions_caculate():
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(a + b)
    c = a * b
    print(c.numerator)
    print(c.denominator)
    print(float(c))
    print(c.limit_denominator(8))

    x = 3.75
    y = Fraction(*x.as_integer_ratio())
    print(y)


def main():
    fractions_caculate()


if __name__ == "__main__":
    main()
    