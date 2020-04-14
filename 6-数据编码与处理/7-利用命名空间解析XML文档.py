#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 18:22
# @user: Administrator
# @fileName: 利用命名空间解析XML文档
# @description: 解析某个XML文档,但是文档使用了 xml 命名空间
#
from xml.etree.ElementTree import parse, Element

class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)

def read_xml_example():
    ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
    doc = Element('/tmp/pred_3.xml')
    doc.find(ns('content/{html}html'))
    print(doc.findtext(ns('content/{html}html/{html}head/{html}title')))


def main():
    read_xml_example()


if __name__ == '__main__':
    main()
