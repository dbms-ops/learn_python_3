#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-31 23:19 
# user: lixun
# filename: 合并多个字典或者映射
# description: 将多个字典或者映射，从逻辑上合并为单一一个映射；
# 

from collections import ChainMap


def dict_compation():
    """
    一个 ChainMap 逻辑上面接受多个字典合并为逻辑上面的一个字典，字典并不是真的合并，ChainMap 只是在内部创建了容纳这些字典的列表；
    常见的字典操作都是支持的；
    如果出现重复值,那么第一次被映射的值会被返回,字典的更新,删除等操作同样只会影响第一个表

    ChainMap
    :return:
    """
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    c = ChainMap(a, b)

    print(c['x']) # Outputs 1 (from a)
    print(c['y']) # Outputs 2 (from b)

    print(len(c))
    print(c.keys())
    print(c.values())
    print(c.items())

    values = ChainMap()
    values['x'] = 2
    values.new_child()
    values['x'] = 3
    values.new_child()
    values['x'] = 4
    print(values)
    values = values.parents
    print(values)

    """
    字典的合并可以参考使用 update 方法,但是在字典更新后,update的结果并不能够同步更新
    """
    a = {
        'x': 1,
        'y': 3
    }

    b = {
        'y': 2,
        'z': 4
    }
    merged = a | b
    print(merged['x'])
    print(merged['y'])
    # 更改字典 a 后, 并不会合并到 merged 中
    # a['d'] = 4
    # print(merged['d'])


def main():
    dict_compation()


if __name__ == "__main__":
    main()
