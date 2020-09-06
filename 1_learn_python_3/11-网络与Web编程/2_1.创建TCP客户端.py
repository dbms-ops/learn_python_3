#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 17:45
# @user: Administrator
# @fileName: 创建TCP客户端
# @description: 创建 TCP 客户端用于访问 TCP 服务器
# 

from socket import socket, AF_INET, SOCK_STREAM


def tcp_client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('localhost', 2001))
    client.send(b'hello')
    print(client.recv(8192))


def main():
    tcp_client()


if __name__ == '__main__':
    main()
