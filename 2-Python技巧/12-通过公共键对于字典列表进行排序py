#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-29 21:14 
# user: lixun
# filename: 通过某个关键字排序一个字典列表
# description: 使用 operator 模块的 itemgetter 函数，用于进行排序
# 

from operator import itemgetter


def keys_sort_dict():
    # sort 函数本身是支持使用 keys 指定排序的键的，itemgetter 就是用来构建 这个 key 的，构建方式同样适合于 max(), min()函数；
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]

    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_fname)
    print(rows_by_uid)
    # itemgetter 支持对于多个 key 进行排序
    rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    print(rows_by_lfname)
    print("the max uid is: ", max(rows, key=itemgetter('uid')))
    print("the min uid is: ", min(rows, key=itemgetter('uid')))



def main():
    keys_sort_dict()


if __name__ == "__main__":
    main()
