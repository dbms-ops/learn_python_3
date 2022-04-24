#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 21:12
# @user: Administrator
# @fileName: 可以接受任意数量参数的函数
# @description: 构造一个可接受任意数量参数的函数
#

import html


def avg(first, *rest):
    """
        函数接受任意个数的位置参数
    :param first: 第一个参数
    :param rest: 剩余可能存在的所有参数,，rest 是由所有其他位置参数组成的元组
    :return:
    """
    return (first + sum(rest)) / (1 + len(rest))


def make_element(name, value, **attrs):
    """
        函数通过 **attrs 接受关键字参数
    :param name:
    :param value:
    :param attrs: attrs 是一个包含所有被传入进来的关键字参数的字典
    :return:
    """
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attrs_str = "".join(keyvals)
    return '<{name}{attrs}>{value}</{name}>'.format(
        name=name, attrs=attrs_str, value=html.escape(value)
    )


def make_element_example():
    make_element('item', 'Albatross', size='large', quantity=6)


def any_args(*args, **kwargs):
    print(args)
    print(kwargs)


def main():
    print(avg(1, 2, 3, 4, 5, 6, 7, 8))


if __name__ == '__main__':
    main()
