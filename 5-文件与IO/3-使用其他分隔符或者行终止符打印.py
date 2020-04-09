#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-09 23:03 
# user: lixun
# filename: 使用其他分隔符或者行终止符打印
# description: 使用print()函数，改变默认的分隔符或者行尾符
# 使用 print() 函数中使用 sep和 end 关键字参数


def print_sep_end():
    print('ACME', 50, 51.90, 91.5)
    print('ACME', 50, 51.90, sep=',')
    print('ACME', 50, 51.90, sep=',', end='!!!\n')
    print(','.join(('ACME', '50', '51.90')))
    for i in range(5):
        print(i, end=' ')
    row = ('ACME', '50', '51.90')
    print(','.join(str(x) for x in row))
    print(*row, sep=',')


def main():
    print_sep_end()


if __name__ == "__main__":
    main()