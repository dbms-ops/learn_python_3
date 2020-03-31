#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/30 17:07
# @user: Administrator
# @fileName: 通过某个字段将记录进行分组.py
# @description: 对于字典或者实例的序列,然后根据某个特定的字段进行分组,比如 date 进行迭代分组;
#    通过 itertools.groupby() 进行分组;
#

from operator import itemgetter
from itertools import groupby


def dict_group_by():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    # 需要实现上面的操作,先对于 date 字段进行排序,然后在进行 groupby
    # Sort by the desired field first
    rows.sort(key=itemgetter('date'))
    for date,items in groupby(rows,key=itemgetter('date')):
        print(date)
        for item in items:
            print(' ', item)
    # sort 函数可以对于 key 字段进行排序, 将相同的 date 字段放在一起;
    # groupby 函数用于查找连续的相同值,根据 key 返回相同的元素序列;
    # ;


def main():
    dict_group_by()


if __name__ == '__main__':
    main()
    