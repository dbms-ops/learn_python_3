#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/3 15:33
# @user: Administrator
# @fileName: 字节字符串上的字符串操作
# @description: 在字节字符串上面执行文本操作
# 

def byte_string():
    data = b'Hello world'
    print(data[0:5])

    data.startswith(b'Hello')
    print(data.split())
    print(data.replace(b'hello',b'Hello Cruel'))


def byte_array():
    data = bytearray(b'Hello World')
    print(data[0:5])

    print(data.startswith(b'hello'))
    print(data.split())
    print(data.replace(b'hello',b'Hello Cruel'))


def byte_note():
    """
    大多数情况下,文本字符串中的操作都可以运用于字节字符串. 字节字符串返回的是整数而不是单独字符串
    对于字节字符串首先需要被解码,才能够很好的进行打印
    :return:
    """
    a = "hello world"
    print(a[0])
    b = b'hello world'
    print(b[0])

    print(b)
    print(b.decode('ascii'))



def main():
    byte_note()


if __name__ == '__main__':
    main()
    