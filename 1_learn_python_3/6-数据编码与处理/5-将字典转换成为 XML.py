#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 17:51
# @user: Administrator
# @fileName: 将字典转换成为 XML
# @description: 使用一个Python字典存储数据,并且转换成为XML格式,
# 

from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

def dict_to_xml(tag, d):
    """
        Turn a simple dict of key/value pairs into XML
    :param tag:
    :param d:
    :return:
    """
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


def dict_to_xml_example():
    s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
    e = dict_to_xml('stock', s)
    e.set('_id', '1234')
    print(tostring(e))


def main():
    dict_to_xml_example()


if __name__ == '__main__':
    main()
    