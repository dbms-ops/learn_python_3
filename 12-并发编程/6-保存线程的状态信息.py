#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 21:39
# @user: Administrator
# @fileName: 保存线程的状态信息
# @description: 保存正在运行的线程状态,这个状态对于线程是不可见
# 

"""
    在多线程编程中，你需要只保存当前运行线程的状态。要这么做，可使用thread.local() 创建一个本地线程存储对象。对这个对象的属性的保存和读取操作
    都只会对执行线程可见，而其他线程并不可
"""

from socket import socket,AF_INET,SOCK_STREAM
import threading
from functools import partial

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise  RuntimeError('Already connected')
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock


def test(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
    print('Got {} bytes'.format(len(resp)))



def main():
    conn = LazyConnection(('www.python.org', 80))

    t_1 = threading.Thread(target=test, args=(conn, ))
    t_2 = threading.Thread(target=test, args=(conn, ))
    t_1.start()
    t_2.start()
    t_1.join()
    t_2.join()


if __name__ == '__main__':
    main()
    