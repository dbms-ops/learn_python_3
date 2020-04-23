#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-23 23:12 
# user: lixun
# filename: 实现一个计时器
# description:
# 

import time

class Timer:
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
        end = self._func
        self.elapesd += end - self._start
        self._start = None



def main():
    pass


if __name__ == "__main__":
    main()
    