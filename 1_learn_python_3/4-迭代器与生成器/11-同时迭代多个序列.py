#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/8 17:08
# @user: Administrator
# @fileName: 同时迭代多个序列
# @description: 同时迭代多个序列,每次分别从一个序列中取出一个元素
#   需要同时迭代多个序列, 使用 zip() 函数

from itertools import zip_longest


def zip_example():
    # zip 迭代, 返回的是一个元组(x,y)的迭代器, 其中 x 来源于a, y来自于b;
    # 一旦到达某个序列的结尾, 迭代宣告结束;
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 15, 62, 99]

    for x, y in zip(xpts, ypts):
        print(x, y)


def zip_longest_example():
    # itertools.zip_longest() 来代替执行输出最长的序列
    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for one in zip_longest(a, b, fillvalue=0):
        print(one)


def dict_zip_example():
    # 将下列序列打包并且声称一个字典
    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]
    dict_zip = dict(zip(headers, values))
    print(dict_zip)
    # 打印 zip 函数中的对应元素, zip()函数返回的结果是是一个迭代器，可以使用 list 函数保存在列表中
    for i in zip(headers, values):
        print(i)
    print(list(zip(headers, values)))


def main():
    dict_zip_example()


if __name__ == '__main__':
    main()
