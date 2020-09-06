#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 15:28 
# user: lixun
# filename: 二八十六进制整数
# description:
# 


def hex_change():
    # Python 指定 八 进制： chmod 0o755 ./file
    x = 1234
    # 转换成 二进制
    print(bin(x))
    print(format(x, 'b'))

    # 转换成八进制
    print(oct(x))
    print(format(x, 'o'))
    # 转化成 16 进制
    print(hex(x))
    print(format(x, 'x'))

    x = -1234
    print(format(x, 'b'))
    print(format(x, 'x'))
    print(2 ** 32 + x, 'b')
    print(2 ** 32 + x, 'x')
    print(int('4d2', 16))


def main():
    hex_change()


if __name__ == "__main__":
    main()
