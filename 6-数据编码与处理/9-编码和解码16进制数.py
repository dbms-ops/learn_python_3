#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 18:32
# @user: Administrator
# @fileName: 编码和解码16进制数
# @description: 将一个16进制的字符串解码成为一个字节字符串,或者将一个字节字符串编码成为一个十六进制字符串
#   使用 binascii 模块来完成编码和解码

import base64
import binascii

def encode_decode_bytes():
    # Initial byte string
    s = b'hello'
    # Encode as hex
    h = binascii.b2a_hex(s)
    print(h)
    # Decode back to bytes
    print(binascii.a2b_hex(h))

def encode_decode_bytes_base():
    # Initial byte string
    s = b'hello'
    # Encode as hex
    h = base64.b16encode(s)
    print(h)
    # Decode back to bytes
    print(base64.b16decode(h))


def main():
    encode_decode_bytes()
    encode_decode_bytes_base()

if __name__ == '__main__':
    main()
    