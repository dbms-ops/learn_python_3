#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 21:07
# @user: Administrator
# @fileName: 给关键部分加锁
# @description: 对于多线程程序中的临界区进行加锁
# 多线程程序中安全使用可变对象，你需要使用threading 库中的Lock 对象

import threading

class SharedCounter:
    """
        A counter object that can be shared by multiple threads
    """
    def __init__(self, initial_value = 0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta = 1):
        """
            Increment the counter with locking
        :param delta:
        :return:
        """
        with self._value_lock:
            self._value += delta

    def decr(self, delta = 1):
        """
            Decrement the counter with locking
        :param delta:
        :return:
        """
        with self._value_lock:
            self._value -= delta



def main():
    pass


if __name__ == '__main__':
    main()
    