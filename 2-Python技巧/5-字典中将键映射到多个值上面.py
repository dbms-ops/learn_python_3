#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/27 18:01
# @user: Administrator
# @fileName: 字典中将键映射到多个值上面.py
# @description: 将一个 key 映射到多个值的字典,一键多值字典[multidict]
# 通过 collections 创建一键多值字典

from collections import defaultdict

def multidict():
    # 通过上述方式创建一键多值字典
    b = {
        'a': [1, 2, 3, 4],
        'b': (4, 5, 7)
    }

    d_list = defaultdict(list)
    d_list['a'].append(1)
    d_list['a'].append(2)
    d_list['b'].append(3)
    d_list['b'].append(4)
    d_list['b'].append(5)

    d_set = defaultdict(set)

    d_set['a'].add(1)
    d_set['b'].add(2)
    d_set['c'].add(3)
    d_set['d'].add(4)
    d_set['e'].add(5)

    print(d_list.get('a'))
    print(d_set)


def main():
    multidict()


if __name__ == '__main__':
    main()
