#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 18:26
# @user: Administrator
# @fileName: 启动与停止线程
# @description: 为需要并发执行的代码创建/销毁线程
# threading 库可以在单独的线程中执行任何的在Python 中可以调用的对象;
# 创建一个Thread 对象并将你要执行的对象以target 参数的形式提供给该;

import time
from threading import Thread

import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)


# create and launch a thread

def t_start():
    # 传递参数 daemon,后台执行的线程无法通过 join方法进行等待,后台线程无法等待，
    # 不过，这些线程会在主线程终止时自动销毁
    t = Thread(target=countdown, args=(10,), daemon=True)
    t.start()
    # t.join 出现表示在这里等待线程执行结束,通过join可以保证线程按照顺序执行
    t.join()
    if t.is_alive():
        print('Still running')
    else:
        print('Completed')

class CountdownTask:
    """
        无法结束一个线程，无法给它发送信号，无法调整它的调度，也无法执行其他高级操作
    """
    def __init__(self):
        self._running = True
    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(1)

def count_down_task_example():
    c = CountdownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()
    c.terminate()
    t.join()

class IOTask:
    """
        由于全局解释锁（GIL）的原因，Python 的线程被限制到同一时刻只允许一个线程执行这样一个执行模型。所以，Python 的线程更适用于处理I/O
        和其他需要并发执行的阻塞操作（比如等待I/O、等待从数据库获取数据等等），而不是需要多处理器并行的计算密集型任务
    """
    def terminate(self):
        self._running = False

    def run(self,sock):
        # sock is a socket
        sock.settimeout(5)
        while self._running:

            try:
                data = sock.recv(8192)
                break
            except sock.timeout:
                continue
        return



def main():
    t_start()


if __name__ == '__main__':
    main()
