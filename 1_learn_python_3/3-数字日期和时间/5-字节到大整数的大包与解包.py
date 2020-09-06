#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 15:45 
# user: lixun
# filename: 字节到大整数的大包与解包
# description: 将字节字符串解压成一个整数，或者将一个大整数转换成为字节字符串
#


def data_bytes():
    # 将 byte 解析为整数
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(len(data))
    print(int.from_bytes(data, 'little'))
    print(int.from_bytes(data, 'big'))

    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, 'big'))
    print(x.to_bytes(16,'little'))



def main():
    data_bytes()


if __name__ == "__main__":
    main()
    