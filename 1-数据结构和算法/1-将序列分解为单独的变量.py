#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/27 16:27
# @user: Administrator
# @fileName: 将序列分解为单独的变量.py
# @description: 脚本文件用于将序列分解为单独的单独的变量;
#   任何序列或者可迭代对象都可以通过简单的赋值解压赋值给多个变量;
#   对于这种简单的匹配,要求变量数据和列表中元组的数量是相同的;
from audioop import avg


def assignmentDecompression():
    # 元组赋值解压
    x, y = (4, 5)
    print(x, y)

    # 列表赋值解压
    x, y, z = [1, 2, (3, 4, 5)]
    print(x)
    print(y)
    print(z)

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name, shares, price, date)
    year, mon, day = date
    print(year, mon, day)

    # 解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组, 包括字符串，文件对象，迭代器和生成器;
    # 字符串赋值解压
    s = "Hello"
    a, b, c, d, e = s
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

    # 解压丢弃某些不需要的元素, 通过 _ 等特殊变量丢弃掉不需要的元素
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    _, shares, price, _ = data
    print(shares, price)


# 解压赋值变量,给多个对象,并且解决元素数量和变量名不匹配的问题
# 通过 * 表达式进行变量分解,位置不限制
def assignment_decompression_value_error():
    def drop_first_last(grades):
        first, *middle, last = grades
        return avg(middle)
    user_recovrd = ('Dave','dave@example.com','773-555-1212','847-555-1212')
    name, email, *phone_numbers = user_recovrd
    print(name, email)
    print(phone_numbers)


def main():
    assignmentDecompressionValueError()


if __name__ == '__main__':
    main()
