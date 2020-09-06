#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-09 23:17 
# user: lixun
# filename: 读写字节数据
# description: 读写二进制文件，图片，声音文件
#  使用模式为 rb 或 wb 的 open() 函数来读取或写入二进制数据；
#  ；

import array


def read_write_binary():
    """
        在读写二进制数据的时候，所有返回的数据都是字节字符串格式的，而不是文本字符串，在写入的时候，需要保证参数都是以字节形式对外暴露
        的对象，比如字节字符串，字节数组对象；


    :return:
    """
    with open('somefile.bin', 'rb') as f:
        data = f.read()

    with open('somefile.rb', 'wb') as f:
        f.write(b'Hello, world')

    """
        在读取数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜在的陷阱，索引和迭代动作返回的是字节的值而不是字节字符串；
    """
    # test string
    t = 'Hello world'
    print(t[0])
    for c in t:
        print(c)

    # Byte string
    b = b'Hello world'
    print(b[0])
    for c in b:
        print(c)


def byte_decode_encode():
    with open('somefile.bin', 'rb') as f:
        data = f.read(16)
        text = data.decode('utf-8')
    with open('somefile.bin', 'wb') as f:
        text = 'Hello, world'
        f.write(text.encode('utf-8'))


def read_into():
    """
        二进制 I/O 还有一个鲜为人知的特性就是数组和 C 结构体类型能直接被写入,而不需要中间转换为自己对象, 在 python 3.6 上面尝试没有
        写进去，该特性依赖于平台特性，很有可能存在写入失败的情况
    :return:
    """
    nums = array.array('i', [1, 2, 3, 4])
    with open('/tmp/somefile.bin', 'wb+') as f:
        f.write(nums)

    a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    with open("/tmp/somefile.bin", 'rb') as f:
        f.readinto(a)
    print(a)



def main():
    read_into()


if __name__ == "__main__":
    main()
