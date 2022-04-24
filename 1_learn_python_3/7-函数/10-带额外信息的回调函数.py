#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/15 21:10
# @user: Administrator
# @fileName: 带额外信息的回调函数
# @description:
# 

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got: ', result)


def add(x, y):
    return x + y


def apply_sync_example():
    apply_async(add, (2, 3), callback=print_result)
    apply_async(add, ('hello ', 'world'), callback=print_result)


class ResultHandler():
    """
            为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函数,类会保存一个内部序列号，每次接收到一个result 的时候序列号
        加1
    """
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print(f'[{self.sequence}] Got: {result}')


def result_handler_example():
    r = ResultHandler()
    apply_async(add, (2, 3), callback=r.handler)
    apply_async(add, ('hello ', 'world'), callback=r.handler)


def make_handler():
    """
        使用闭包捕获状态值
    :return:
    """
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print(f'[{sequence}] Got: {result}')
    return handler


def make_handler_example():
    handler = make_handler()
    apply_async(add, (2, 3), callback=handler)
    apply_async(add, ('hello ', 'world'), callback=handler)




def main():
    make_handler_example()


if __name__ == '__main__':
    main()
