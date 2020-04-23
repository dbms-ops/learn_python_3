#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 20:24
# @user: Administrator
# @fileName: 线程超时定时器
# @description: 
#
"""
    event 对象最好单次使用，就是说，你创建一个event 对象，让某个线程等待这个对象，一旦这个对象被设置为真，你就应该丢弃它
    可以通过 clear() 方法来重置 event 对象，但是很难确保安全地清理event 对象并对它重新赋值.
    使用Condition 对象实现了一个周期定时器，每当定时器超时的时候，其他线程都可以监测到

    event 对象的一个重要特点是当它被设置为真时会唤醒所有等待它的线程
"""

import threading
import time


class PeriodicTimer:

    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True

        t.start()

    def run(self):
        """
            Run the timer and notify waiting threads after each interval
        :return:
        """
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_fot_tick(self):
        """
            Wait for the next tick of the timer
        :return:
        """
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


ptimer = PeriodicTimer(5)
ptimer.start()


def periodic_example():
    pass


def countdown(nticks):
    while nticks > 0:
        ptimer.wait_fot_tick()
        print('T-minus', nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        ptimer.wait_fot_tick()
        print('Counting ', n)
        n += 1


def main():
    threading.Thread(target=countdown, args=(10,)).start()
    threading.Thread(target=countup, args=(5,)).start()


if __name__ == '__main__':
    main()
