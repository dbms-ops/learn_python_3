#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/15 20:56
# @user: Administrator
# @fileName: 将简单的方法的类转换成为函数
# @description: 对于只有一个方法的类可以直接转换成为一个函数
#   可以使用 闭包 来将单个方法的类转换成函数

from urllib.request import urlopen


class UrlTemplate():
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


def url_template(template):
    """
        将 只有一个方法的类 UrlTemplate 转换一个函数
    :param template:
    :return:
    """

    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


def url_template_example():
    yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f=,!{fields}')
    for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
        print(line.decode('utf-8'))


def main():
    url_template_example()


if __name__ == '__main__':
    main()
