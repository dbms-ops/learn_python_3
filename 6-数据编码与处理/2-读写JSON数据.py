#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-12 13:57 
# user: lixun
# filename: 读写JSON数据
# description:  将 Python数据结构转换成为 JSON，json模块提供两个函数 json.dumps() json.loads()来完成数据转换功能
# 

import json


def json_process():
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    json_str = json.dumps(data)
    print(json_str)


def main():
    pass


if __name__ == "__main__":
    main()
