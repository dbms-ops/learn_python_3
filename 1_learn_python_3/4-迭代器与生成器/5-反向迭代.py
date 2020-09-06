#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-06 16:00 
# user: lixun
# filename: 反向迭代
# description:
#       序列进行反向迭代, 反向迭代仅仅当对象的大小可预先确定，或者对象实现了 __reversed__() 方法才会生效；
#       如果以上两者都不符合，那么必须先将对象转换成为一个列表；
# 


def file_reversed():
    # 对于文件不存在不满足上面的要求，只能够先转换成为列表，通过列表的方法进行反转
    with open('/etc/password') as f:
        for line in reversed(list(f)):
            print(line, end=' ')


def reversed_iter():
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)


class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


def main():
    for rr in reversed(Countdown(30)):
        print(rr)
    print("Countdown \n")
    for rr in Countdown(30):
        print(rr)


if __name__ == "__main__":
    main()
