#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/18 12:00
# @user: Administrator
# @fileName: 定义一个带有参数的装饰器
# @description: 写一个装饰器，给函数添加日志功能，同时允许用户指定日志的级别和其他的选
# 

from functools import wraps
import logging

def logged(level,name=None,message=None):
    """
            Add logging to a function. level is the logging
        level, name is the logger name, and message is the
        log message. If name and message aren't specified,
        they default to the function's module and name.
    :param level:
    :param name:
    :param message:
    :return:
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

def logged_example():
    """

    :return:
    """
    @logged(logging.DEBUG)
    def add(x, y):
        return x + y

    @logged(logging.CRITICAL,'example')
    def spam():
        print('Spam !!!')







def main():
    pass


if __name__ == '__main__':
    main()
    