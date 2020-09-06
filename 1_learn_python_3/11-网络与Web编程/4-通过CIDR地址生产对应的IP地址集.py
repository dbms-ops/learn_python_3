#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 18:09
# @user: Administrator
# @fileName: 通过CIDR地址生产对应的IP地址集
# @description: 
# 

import ipaddress


def ip_address():
    net = ipaddress.ip_network('123.45.67.64/27')
    for I in net:
        print(I)
    print(net.num_addresses)
    print(net[0])

    a = ipaddress.ip_address('123.45.67.69')
    print(a in net)

    b = ipaddress.ip_address('123.45.67.123')
    print(b in net)


def main():
    ip_address()


if __name__ == '__main__':
    main()
