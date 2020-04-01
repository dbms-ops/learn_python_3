#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/27 18:14
# @user: Administrator
# @fileName: 有序字典.py
# @description: 默认的字典是无序的,通过 collections 来创建有序字典,有序的含义是按照插入的顺序进行排序,并不是进行排序的字典
# 

from collections import OrderedDict


def ordered_dict():
    # 有序字典是通过 双向链表来实现的,双向链表的内存开销是普通字典的 2 倍
    order_dict = OrderedDict()
    order_dict['foo'] = 1
    order_dict['bar'] = 2
    order_dict['spam'] = 6
    order_dict['grok'] = 4

    for key in order_dict:
        print(key, order_dict[key])


def main():
    ordered_dict()


if __name__ == '__main__':
    main()
    