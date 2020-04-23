#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 20:40
# @user: Administrator
# @fileName: 线程间通信
# @description: 你的程序中有多个线程，你需要在这些线程之间安全地交换信息或数据
"""
    从一个线程向另一个线程发送数据最安全的方式可能就是使用queue 库中的队列, 创建一个被多个线程共享的Queue 对象，这些线程通过使用put()
    和 get()操作来向队列中添加或者删除元素;
"""
from queue import Queue
from threading import Thread

def producer(out_q):
    """
        生产者
    :param out_q:
    :return:
    """
    data = 0
    while True:
        """
            Produce some data
        """
        data += 1
        out_q.put(data)

def consumer(in_q):
    # Get some data
    while True:
        data = in_q.get()
        """
            Process the data
        """

# Create the shared queue and launch both threads
q = Queue()
t_1 = Thread(target=consumer, args=(q,))
t_2 = Thread(target=producer, args=(q,))
t_1.start()
t_2.start()




def main():
    pass


if __name__ == '__main__':
    main()
    