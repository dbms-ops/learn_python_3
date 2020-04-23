#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 21:14
# @user: Administrator
# @fileName: 防止死锁的加锁机制
# @description: 
# 

"""
    一个多线程程序，其中线程需要一次获取多个锁,在多线程程序中，死锁问题很大一部分是由于线程同时获取多个锁造成的,一个线程获取了第一个锁，
    然后在获取第二个锁的时候发生阻塞，那么这个线程就可能阻塞其他线程的执行，从而导致整个程序假死。解决死锁问题的一种方案是为程序中的每
    一个锁分配一个唯一的id，然后只允许按照升序规则来使用多个锁，这个规则使用上下文管理器是非常容易实现的
"""

import threading
from contextlib import contextmanager

# Thread-local state to stored information on locks already acquired

_local = threading.local()


@contextmanager
def acquire(*locks):
    # Sort locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired locks is not violated
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    # Acquire all of the locks
    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse order of acquisition
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')


def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')


def main():
    t_1 = threading.Thread(target=thread_1)
    t_1.daemon = True
    t_1.start()

    t_2 = threading.Thread(target=thread_2)
    t_2.daemon = True
    t_2.start()


if __name__ == '__main__':
    main()
