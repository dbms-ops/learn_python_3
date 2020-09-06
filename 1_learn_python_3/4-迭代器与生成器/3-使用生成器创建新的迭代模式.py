#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 21:30 
# user: lixun
# filename: 使用生成器创建新的迭代模式
# description: 实现一个自定义的迭代模式，不同于 range(), reverse()函数；需要自定义生成器函数来实现
#

def frange(start,stop, increment):
    # 一个函数中只要有一个 yield 语句，可以将函数转转换成为一个生成器，生成器只能用于进行迭代器操作
    x = start
    while x < stop:
        yield x
        x += increment


def countdown(n):
    """
    一个生成器函数主要特征是它只会回应在迭代中使用到的 next 操作。一旦生成器 函数返回退出，迭代终止。我们在迭代中通常使用的 for
    语句会自动处理这些细节，所以你无需担心
    :param n:
    :return: 生成器函数
    """
    print('starting to count from ', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')


def main():
    for n in frange(0,4,0.5):
        print(n)
    print(list(frange(0, 1, 0.125)))


if __name__ == "__main__":
    main()
    