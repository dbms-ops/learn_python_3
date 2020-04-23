#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 16:19
# @user: Administrator
# @fileName: 作为客户端 与 HTTP 服务交互
# @description: 通过HTTP 协议以客户端的方式访问多种服务,下载数据或者与基于REST 的API 进行交互。
# 
from urllib import request, parse
import requests


def get_example():
    # Base URL being accessed
    url = "http://httpbin.org/get"
    parms = {
        'name1': 'values1',
        'name2': 'value2'
    }

    # Dictionary of query parameters (if any)
    querystring = parse.urlencode(parms)

    # Make a GET request and read the response
    u = request.urlopen(url + '?' + querystring)
    resp = u.read()
    print(resp)


def post_example():
    # Base URL being accessed
    url = 'http://httpbin.org/post'

    # Dictionary of query parameters (if any)
    parms = {
        'name1': 'value1',
        'name2': 'value2'
    }

    # Encode the query string
    querystring = parse.urlencode(parms)

    # Make a POST request and read the response
    u = request.urlopen(url, querystring.encode('ascii'))
    resp = u.read()
    print(resp)
    print(type(resp))


def requests_head():
    resp = requests.head('http://www.python.org/index.html')

    status = resp.status_code
    print(status)
    print(resp.headers)
    print(type(resp.headers.get('Server')))


def main():
    requests_head()


if __name__ == '__main__':
    main()
