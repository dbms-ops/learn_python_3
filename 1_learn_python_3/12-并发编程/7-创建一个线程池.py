#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 16:27
# @user: Administrator
# @fileName: 创建一个线程池
# @description: 一个工作者线程池,用来相应客户端请求或执行其他的工作
#   concurrent.futures 函数库有一个ThreadPoolExecutor 类可以被用来完成这个任务;
# ;

from socket import AF_INET,SOCK_STREAM,socket
from concurrent.futures import ThreadPoolExecutor

def echo_client(sock, client_adrr):
    """
        Handle a client connection
    :param sock:
    :param client_adrr:
    :return:
    """
    print('Got connection from', client_adrr)
    while True:
        msg = sock.recv(65535)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()

def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)

echo_server(('',15000))


def main():
    pass


if __name__ == '__main__':
    main()
    