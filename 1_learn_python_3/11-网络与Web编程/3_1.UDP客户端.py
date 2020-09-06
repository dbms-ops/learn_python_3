#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 18:00
# @user: Administrator
# @fileName: UDP客户端
# @description: 
# 

from socket import socket, AF_INET, SOCK_DGRAM


def udp_client():
    client = socket(AF_INET, SOCK_DGRAM)
    client.sendto(b'', ('localhost', 2000))
    print(client.recvfrom(8192))


def main():
    udp_client()


if __name__ == '__main__':
    main()
