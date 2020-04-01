#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-29 20:50 
# user: lixun
# filename: 命名切片
# description: 切片：用于在字符串中截取特定的字符串；
#   命名切片：命名切片是通过 splice() 来实现的；
# 


def slice_myself():
    record = '....................100 .......513.25 ..........'
    # 常见的切片方式都是按照下标来进行切片的，这里的切片表示的是切片硬编码，代码的可读性不强
    cost = int(record[20:23]) * float(record[31:37])
    print(cost)


def slice_python():
    # 使用 slice 定义命名切片，可以提高代码的可读性
    record = '....................100 .......513.25 ..........'
    shares = slice(20, 23)
    price = slice(31, 37)
    cost = int(record[shares]) * float(record[price])
    print(cost)


def slice_example():
    # 任何一个切片对象：都包含 start stop step 三个属性
    a = slice(5, 50, 2)
    print(a.start,a.stop,a.step)


def main():
    slice_myself()
    slice_example()


if __name__ == "__main__":
    main()
