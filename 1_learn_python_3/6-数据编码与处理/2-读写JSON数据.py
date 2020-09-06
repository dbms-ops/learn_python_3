#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-12 13:57 
# user: lixun
# filename: 读写JSON数据
# description: 将 Python数据结构转换成为 JSON，json模块提供两个函数 json.dumps() json.loads()来完成数据转换功能
#


import json
from urllib.request import urlopen
from pprint import pprint
from collections import OrderedDict


def json_process():
    """
        json 模块的常见操作
    :return:
    """
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    json_str = json.dumps(data)
    print(json_str)
    json.dumps(False)
    d = {
        'a': True,
        'b': "Hello",
        'c': None
    }
    print(json.dumps(d))


def json_to_file(filename='/tmp/json.dump'):
    """
        将 字典 json 之后写入文本文件
    :param filename:
    :return:
    """
    data = {
        'name': 'ACME',
        'shares': 100,
        'price': 542.23
    }
    with open(filename, 'w') as f:
        json.dump(data, f)
    with open(filename, 'r') as f:
        data = json.load(f)
        print(data)
        print(data['name'])


def pprint_json():
    """
        通过 pprint 梅花 json 格式数据输出
    :return:
    """
    u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
    resp = json.loads(u.read().decode('utf-8'))
    pprint(resp)


def json_to_ordered_dict():
    s = '{"name": "ACME", "shares": 50, "price": 490.1}'
    data = json.loads(s, object_pairs_hook=OrderedDict)
    print(data)


def main():
    json_to_ordered_dict()

if __name__ == "__main__":
    main()
