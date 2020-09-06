#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-23 23:12 
# user: lixun
# filename: 实现一个计时器
# description:
# 

import time


class Timer:
    """
        time.perf_counter: 计算函数执行的完整时间
        time.process_time: 用于计算进程花费的 CPU 时间
    """
    def __init__(self, func=time.perf_counter):
        self.elapesd = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already statred')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not stared')
        end = self._func()
        self.elapesd += end - self._start
        self._start = None

    def reset(self):
        self.elapesd = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.stop()


def count_down(n):
    while n > 0:
        n -= 1


def main():
    t = Timer()
    t.start()
    count_down(100000)
    t.stop()
    print(t.elapesd)
    with t:
        count_down(10000)
    print(t.elapesd)
    with Timer() as t2:
        count_down(1000000)
    print(t2.elapesd)


if __name__ == "__main__":
    main()
