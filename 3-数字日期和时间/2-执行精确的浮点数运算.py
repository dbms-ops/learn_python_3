#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 14:35 
# user: lixun
# filename: 执行精确的浮点数运算
# description: 对于浮点数执行精确的计算操作，不允许有任何的小误差出现
#

from decimal import Decimal
from decimal import localcontext

def add_number():
    # 浮点数的计算往往是不准确
    a = 4.2
    b = 2.1
    print(a + b, ((a + b) == 6.3))
    # 通过 decimal 进行准确计算
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a + b, (a + b) == Decimal('6.3'))


def local_context_value():
    #
    a = Decimal('1.3')
    b = Decimal('2.4')
    print(a/b)

    with localcontext() as ctx:
        ctx.prec = 3
        print(a/b)

    with localcontext() as ctx:
        ctx.prec = 12
        print(a/b)


def main():
    local_context_value()


if __name__ == "__main__":
    main()
