#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/2 19:20
# @user: Administrator
# @fileName: 小字符串合并成大字符串
# @description: 将几个小的字符串合并成一个大的字符串
# 

def string_join():
    # 字符串在一个列表中,或者 iterator 中,最快的方式就是使用join方法
    parts = ["Is", "Chicago", "Not", "Chicago?"]
    print(' '.join(parts))
    print(','.join(parts))
    print(''.join(parts))
    # 对于少数的字符串使用 + 就可以满足
    a = "Is Chicago"
    b = "Not Chicago"
    print(a + " " + b)
    print('{} {}'.format(a,b))
    # 字符串拼接一定不能够使用 下面的方式,下面的方式会引起内存复制以及垃圾回收机制,带来很大的性能损失
    s = ""
    for p in parts:
        s += p
    print(s)
    # 计较聪明的方式: 使用生成器表达式来进行字符串拼接
    data = ["ACME", 50,91.1]
    print(','.join(str(d) for d in data))

    # Ugly: 常见的几种字符串拼接操作
    c = "123"
    print(a + ":" + b + ":" + c )
    print(":".join([a,b,c]))
    # 推荐的写法:
    print(a, b, c, sep = ':')


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


def combine(source,maxsize):
    # 生成器函数只需要按照指定的片段去拼接字符串就可以了
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += 1
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)


def main():
    string_join()
    print(' '.join(sample()))



if __name__ == '__main__':
    main()
    