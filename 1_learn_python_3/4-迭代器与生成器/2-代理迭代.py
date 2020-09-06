#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 20:58 
# user: lixun
# filename: 代理迭代
# description: 构建一个自定义的那个容器对象，里面包含有列表，元祖，或者其他可迭代对象，需要在新容器对象执行迭代操作
# 代理迭代：Python 的迭代器协议需要 __iter__() 方法返回一个实现了 __next__() 方法的 迭代器对象，这里的 iter() 函数的使用简化了代码，
#  iter(s) 只是简单的通过调用 s. __iter__() 方法来返回对应的迭代器对象
#


class Node():
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


def main():
    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_2)
    for I in root:
        print(I)


if __name__ == "__main__":
    main()
