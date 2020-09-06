#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 16:44
# @user: Administrator
# @fileName: 创建一个线程
# @description: 
#
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data

def fetch_url_example():
    pool = ThreadPoolExecutor(10)
    # Submit work to the pool

    a = pool.submit(fetch_url, 'http://www.python.org')
    b = pool.submit(fetch_url, 'http://www.pypy.org')

    # Get the results back
    x = a.result()
    y = b.result()
    print(x, y)


def main():
    fetch_url_example()


if __name__ == '__main__':
    main()
    