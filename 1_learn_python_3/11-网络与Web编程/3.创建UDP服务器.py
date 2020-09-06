#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 17:55
# @user: Administrator
# @fileName: 创建UDP服务器
# @description: 实现一个基于UDP 协议的服务器来与客户端通信
# 

from socketserver import BaseRequestHandler, UDPServer
import time


class TimeHanlder(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


def time_server():
    server = UDPServer(('', 2000), TimeHanlder)
    server.serve_forever()


def main():
    time_server()


if __name__ == '__main__':
    main()
