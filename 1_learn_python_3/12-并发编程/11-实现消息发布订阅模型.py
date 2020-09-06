#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 19:47
# @user: Administrator
# @fileName: 实现消息发布订阅模型
# @description: 基于线程通信的程序，想让它们实现发布/订阅模式的消息通信
# 

from collections import defaultdict

"""
    发布订阅模型是一对多或者多对多的模型
"""

class Exchage:

    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary of all created exchanges
_exchanges = defaultdict(Exchage)


# Return the Exchange instance associated with a given name

def get_exchange(name):
    return _exchanges[name]


class Task:

    def send(self, msg):
        print(msg)


tast_a = Task()
tast_b = Task()

exc = get_exchange('name')
exc.attach(tast_a)
exc.attach(tast_b)
exc.send('msg1')
# exc.send('msg2')

exc.detach(tast_a)
exc.detach(tast_b)


def main():
    pass


if __name__ == '__main__':
    main()
