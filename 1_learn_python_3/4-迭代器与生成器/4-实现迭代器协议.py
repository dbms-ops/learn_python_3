#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 22:05 
# user: lixun
# filename: 实现迭代器协议
# description:
#   构建一个支持迭代操作的自定义对象，并且希望找到一个能够实现迭代协议的简单方法
#   在一个对象上实现迭代协议最简单的方式就是使用一个生成器函数;
#   深度优先遍历树形节点的生成器;


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_path(self):
        # 实现深度过滤，depth_first()，返回自己本身并迭代每一个 子节点并通过调用子节点的 depth_first()，使用 yield from 返回对应的
        # 元素
        yield self
        for c in self:
            yield from c.depth_path()


def main():
    root = Node(0)
    child_1 = Node(1)
    child_2 = Node(2)
    root.add_child(child_1)
    root.add_child(child_2)
    child_1.add_child(Node(3))
    child_1.add_child(Node(4))
    child_2.add_child(Node(5))

    for ch in root.depth_path():
        print(ch)


if __name__ == "__main__":
    main()
