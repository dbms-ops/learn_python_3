#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-12 10:32 
# user: lixun
# filename: 读取CSV数据
# description: 读取 CSV 格式的文件
#   对于常见的CSV 格式的数据都是可以使用 csv 库进行读取的
# ；

import csv
from collections import namedtuple


def read_csv(filename='/tmp/sock.csv'):
    """
        打开 csv 格式的文件，读取头部信息，并且按行进行读取
    :param filename:
    :return:
    """
    with open(filename) as f:
        f_csv = csv.reader(f, delimiter=',')
        headers = next(f_csv)
        print(headers)
        for row in f_csv:
            print(row)


def read_csv_named(filename='/tmp/sock.csv'):
    """

    :param filename:
    :return:
    """
    with open(filename) as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            """
                判断列表长度，文件的末尾可能存在换行符，导致命名元组在处理空行时出错
            """
            if len(r) != 0: row = Row(*r)
            # 通过列名访问命名元组
            print(row.Symbol)
            # 使用列表解析将结果放在一个列表中
        # tuples = [Row(*row) for row in f_csv if len(row) == 6]
        # print(tuples)


def read_csv_dict(filename='/tmp/sock.csv'):
    """
        从 csv 读取的数据保存在字典中
    :param filename:
    :return:
    """
    with open(filename) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row)


def write_to_csv(filename="/tmp/data_example.csv"):
    """
        将 数据 写入成为 CSV 格式
    :param filename:
    :return:
    """
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
            ]
    with open(filename, 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def write_dict_to_csv(filename='/tmp/data_example_dict.csv'):
    """
        将字典格式的数据写入到 CSV文件中
    :param filename:
    :return:
    """
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007', 'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007', 'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
            {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007', 'Time': '9:36am', 'Change': -0.46,
             'Volume': 935000}, ]
    with open(filename, 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)


def convert_type_value_from_list(filename='/tmp/data_example_dict.csv'):
    col_types = [str, float, str, str, float, int]
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            # Apply conversions to the row items,
            row = tuple(convert(value) for convert, value in zip(col_types, row))


def convert_type_value_from_dict(filename='/tmp/data_example_dict.csv'):
    print('Reading as dicts with type conversion')
    field_types = [('Price', float), ('Change', float), ('Volume', int)]
    with open(filename, 'r') as f:
        for row in csv.DictReader(f):
            row.update((key, conversion(row[key]))
                       for key, conversion in field_types)


def main():
    write_to_csv()


if __name__ == "__main__":
    main()
