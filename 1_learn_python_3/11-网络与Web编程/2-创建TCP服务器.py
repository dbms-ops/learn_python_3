#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 17:40
# @user: Administrator
# @fileName: 创建TCP服务器
# @description: 实现一个 tcp 服务器,实现 TCP 协议 和 客户端通信
#

from socketserver import BaseRequestHandler,TCPServer
from socketserver import ThreadingTCPServer

class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:

            msg = self.request.recv(8192)
            if not msg:
                break
            print(msg)
            self.request.send(msg)

def tcp_single_thread():
    # 创建单线程TCP服务器
    server = TCPServer(('', 2001), EchoHandler)
    server.serve_forever()

def tcp_multithreading():
    # 创建多线程 TCP 服务器
    server_Multi = ThreadingTCPServer(('', 2001), EchoHandler)
    server_Multi.serve_forever()

def main():
    tcp_multithreading()


if __name__ == '__main__':
    main()
    