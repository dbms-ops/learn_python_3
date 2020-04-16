#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 16:47
# @user: Administrator
# @fileName: 对象支持上下文管理协议
# @description: 对象支持上下文管理协议(with 语句)
#   实现__enter__() 和__exit__() 方法 支持 with 语句,

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    """
        类 用于 支持上下文 with 语句, 但是不支持 with 的嵌套
    """
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


class LazyConnectionNested:
    """
        类 用于支持上下文 with 语句, 通过保存 socket 支持 with 嵌套
    """
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        socket.connect(self.address)
        self.connections.append(sock)
        return sock
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()


def lazy_connection_example():
    conn = LazyConnection(('www.python.org', 80))
    with conn as s:
        # conn.__enter__() executes: connection open
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)


def main():
    lazy_connection_example()


if __name__ == '__main__':
    main()
