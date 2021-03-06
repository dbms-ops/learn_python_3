#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/13 18:12
# @user: Administrator
# @fileName: 解析简单的xml数据
# @description: 从一个简单的XML 文档中提取数据
# 

from urllib.request import urlopen
from xml.etree.ElementTree import parse


def parse_xml():
    # Download the RSS feed and parse it
    u = urlopen('https://planetpython.org/rss20.xml')
    doc = parse(u)
    # Extract and output tags of interest
    for item in doc.iterfind('chanel/item'):
        title = item.findtext('title')
        data = item.findtext('pubDate')
        link = item.findtext('link')
        print(title)
        print(data)
        print(link)

def read_xml(filename='/tmp/version_1.xml'):
    doc = parse(filename)
    e = doc.find('channel/title')
    print(e.tag)
    print(e.text)


def main():
    read_xml()


if __name__ == '__main__':
    main()
