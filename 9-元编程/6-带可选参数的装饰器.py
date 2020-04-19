#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-19 20:08 
# user: lixun
# filename: 带可选参数的装饰器
# description: 写一个装饰器，既可以不传参数给它，也可以传递可选参数给它
# 

from functools import wraps, partial

import logging


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None: return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged
def add(x, y):
    return x + y


# @logged 装饰器可以同时不带参数或者带参数
@logged(level=logging.CRITICAL, name='example')
def spam():
    print('spam')


"""
    # Example use
    @logged
    def add(x, y):
        return x + y
    上面的调用和下面的调用是等价的
    def add(x, y):
        return x + y
    add = logged(add)
    
    @logged(level=logging.CRITICAL, name='example')
    
    def spam():
        print('Spam!')
    
    def spam():
        print('Spam!')
    spam = logged(level=logging.CRITICAL, name='example')(spam)
    
"""

def main():
    pass


if __name__ == "__main__":
    main()
