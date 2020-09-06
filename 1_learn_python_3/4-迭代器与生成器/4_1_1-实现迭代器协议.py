#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-06 15:39 
# user: lixun
# filename: 实现迭代器协议
# description:
#    Python 的迭代器协议要求一个 __iter__()方法返回一个特殊的迭代器对象，迭代器对象实现了 __next__()方法，并且通过
#    StopIteration异常标示迭代的完成；
# 

class Node2:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node({!r})'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    '''
    Depth-first traversal
    '''
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None
    def __iter__(self):
        return self
    def __next__(self):
        # Return myself if just started; create an iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        # If processing a child, return its next item
        elif self._child_iter:
            try:
                next_child = next(self._child_iter)
                return next_child
            except StopIteration:
                self._child_iter = None
                return next(self)
        # Advance to the next child and start its iteration
        else:
            self._child_iter = next(self._child_iter).depth_first()
            return next(self)




def main():
    pass


if __name__ == "__main__":
    main()
    