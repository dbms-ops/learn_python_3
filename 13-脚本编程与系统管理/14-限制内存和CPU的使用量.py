#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/24 15:47
# @user: Administrator
# @fileName: 限制内存和CPU的使用量
# @description: 对于 Unix 系统上面运行的程序设置内存或者 CPU 的使用限制
#
# ;

import os
import signal
import resource


def time_exceeded(singo, frame):
    print('Time is up')
    raise SystemExit(1)


def set_max_runtimes(seconds):
    # Install the signal handler and set a resource limit
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setrlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))


def main():
    set_max_runtimes(10)
    while True:
        pass


if __name__ == '__main__':
    main()
