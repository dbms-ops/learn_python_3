#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 20:33 
# user: lixun
# filename: 手动遍历迭代器
# description:  迭代器是 Python 最强大的功能之一，迭代器不仅仅是用来处理序列中元素的方法；
# 

# 手动遍历迭代器，但是不使用 for 循环，使用 next函数，并且捕捉StopIteration函数


def manual_iter():
    # 通过while 循环遍历迭代器，并且捕捉异常
    with open('/etc/password') as f:
        try:
            while True:
                line = next(f)
                print(line, end=' ')
        except StopIteration:
            pass

def manual_iter_none():
    #
    with open('/etc/password') as f:
        while True:
            # next支持两个参数，第二个表示默认参数
            line = next(f, None)
            if line is None:
                break
            print(line, end=' ')

def know_iter():
    # 通常对于迭代都是从头到尾，但是偶尔也需要对于迭代进行精准的控制
    item = [1, 2, 3]
    # Get the iterator, Invokes items.__iter__()
    it = iter(item)
    # Run the iterator
    print(next(it))  # Invokes it.__next__()
    print(next(it))
    print(next(it))
    """
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module> StopIteration
    """
    print(next(it))



def main():
    pass


if __name__ == "__main__":
    main()
    