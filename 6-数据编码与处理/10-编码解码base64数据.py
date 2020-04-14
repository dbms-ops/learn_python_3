#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 20:42
# @user: Administrator
# @fileName: 编码解码base64数据
# @description: 使用base64格式解码或者编码二进制数据
#

import base64


def encode_decode_base64():
    # Some byte data
    s = b'hello'
    # Encode as Base64
    a = base64.b64encode(s)
    # Decode from Base64
    print(base64.b16decode(a))


def main():
    encode_decode_base64()


if __name__ == '__main__':
    main()
