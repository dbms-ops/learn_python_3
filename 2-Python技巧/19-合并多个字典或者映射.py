#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-31 23:19 
# user: lixun
# filename: 合并多个字典或者映射
# description: 将多个字典或者映射，从逻辑上合并为单一一个映射；
# 

from collections import ChainMap


def dict_compation():
    # 一个 ChainMap 逻辑上面接受多个字典合并为逻辑上面的一个字典，字典并不是真的合并，ChainMap 只是在内部创建了容纳这些字典的列表；
    # 常见的字典操作都是支持的；
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    c = ChainMap(a, b)

    print(c['x'])
    print(c['y'])

    print(len(c))
    print(c.keys())
    print(c.values())
    print(c.items())


def main():
    dict_compation()


if __name__ == "__main__":
    main()
