#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 20:05
# @user: Administrator
# @fileName: 判断线程是否已经启动
# @description: 启动一个线程,判断线程是否开始运行;
#
"""
    线程的一个关键特性是每个线程都是独立运行且状态不可预测, 如果程序中的其他线程需要通过判断某个线程的状态来确定自己下一步的操作，
    这时线程同步问题就会变得非常棘手,为了解决这些问题，我们需要使用 threading 库中的 Event 对象,Event 对象包含一个可由线程设置的信号标志，
    它允许线程等待某些事件的发生,
    使用Event 来协调线程的启动
"""
from threading import Thread, Event
import time


# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        n -= 1
        time.sleep(1)


def count_down_example():
    # Create the event object that will be used to signal startup
    started_evt = Event()

    # Launch the thread and pass the startup event
    print('Launching countdown')
    t = Thread(target=countdown, args=(10, started_evt))
    t.start()

    # Wait for the thread to start
    started_evt.wait()
    print('countdown is running')


def main():
    count_down_example()


if __name__ == '__main__':
    main()
