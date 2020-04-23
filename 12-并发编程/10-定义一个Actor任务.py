#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 19:31
# @user: Administrator
# @fileName: 定义一个Actor任务
# @description: 定义跟actor 模式中类似“actors”角色的任务
#   actor 模式是一种最古老的也是最简单的并行和分布式计算解决方案,一个actor 就是一个并发执行的任务，只是简单的执行发送给它的消息任务。
#   响应这些消息时，它可能还会给其他actor 发送更进一步的消息, actor 之间的通信是单向和异步的。因此，消息发送者不知道消息是什么时候被发送，
#   也不会接收到一个消息已被处理的回应或通知;

from queue import Queue
from threading import Thread, Event


# Sentinel used for shutdown
class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        """
            Send a message to the actor
        :param msg:
        :return:
        """
        self._mailbox.put(msg)

    def recv(self):
        """
            Receive an incoming message
        :return:
        """
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()

    def close(self):
        """
            Close the actor, thus shutting it down
        :return:
        """
        self.send(ActorExit)

    def start(self):
        """
            Start concurrent execution
        :return:
        """
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        """
            Run method to be implemented by the user
        :return:
        """
        while True:
            msg = self.recv()


# Sample ActorTask
class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got: ', msg)


def main():
    p = PrintActor()
    p.start()
    p.send('Hello')
    p.close()
    p.join()


if __name__ == '__main__':
    main()
