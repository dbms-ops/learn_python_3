#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/31 15:40
# @user: Administrator
# @fileName: 映射名称到序列元素
# @description:
#   通过下标访问列表或者元组中元素的代码,往往难以阅读,可以通过名称来访问元素;
#   通过 collections.namedtuple() 函数通过一个普通元组来解决;
#

from collections import namedtuple


def named_tuple():
    # 使用 命名元组对于里面的值是不能够进行更改的
    Subscribe = namedtuple('Subscribe', ['addr', 'joined'])
    sub = Subscribe('jonesy@example.com', '2012-10-19')
    print('sub.addr', sub.addr)
    print('sub joined', sub.joined)


def compute_const(records):
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


def named_tuple_replace():
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])
    s = Stock('ACME', 100, 123.45)
    # 通过 s.shares 修改会直接报错
    # s.shares = 75
    # 通过 s._replace 的方式进行修改
    s = s._replace(shares=75)
    print('修改后的s ', s)


def dict_to_stock(s):
    Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
    stock_prototype = Stock('', 0, 0.0, None, None)
    return stock_prototype._replace(**s)


def main():
    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print(dict_to_stock(a))
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print(dict_to_stock(b))


if __name__ == '__main__':
    main()
