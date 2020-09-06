#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 15:15 
# user: lixun
# filename: 数字的格式化输出
# description: 对于数字进行格式化后输出
# 


def number_format():
    # 通过format简单的格式化树枝输出
    x = 1234.56789
    print(format(x, '0.2f'))
    print(format(x, '>10.1f'))
    print(format(x, '<10.2f'))
    print(format(x, '^10.3f'),'"')
    print(format(x, ','))
    print(format(x, '0.2E'))

    # 同时指定宽度和精度
    # '[<>^]?width[,]?(.digits)?'
    print('The value is {:0,.2f}'.format(x))


def main():
    number_format()


if __name__ == "__main__":
    main()
