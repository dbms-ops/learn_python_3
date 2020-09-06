#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 17:31
# @user: Administrator
# @fileName: 增量式解析大型XML文档
# @description: 使用较小的内存从一个超大的XML文档中读取数据
#   增量式的数据处理,使用迭代器和生成器进行处理

from xml.etree.ElementTree import iterparse
from collections import Counter

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event =='end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

def read_xml_iter(filename='/tmp/version_2.xml'):
    potholes_by_zip = Counter()
    data = parse_and_remove(filename, 'row/row')
    for pothole in data:
        potholes_by_zip[pothole.findnext('zip')] += 1
    for zipcode, num in potholes_by_zip.most_common():
        print(zipcode, num)


def main():
    read_xml_iter()


if __name__ == '__main__':
    main()
    