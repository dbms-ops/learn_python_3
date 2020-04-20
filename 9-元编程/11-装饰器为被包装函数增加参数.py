#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/20 17:44
# @user: Administrator
# @fileName: 装饰器为被包装函数增加参数
# @description: 在装饰器中给被包装函数增加额外的参数，但是不能影响这个函数现有的调用规则,
# 使用关键字参数来给被包装函数增加额外参数;
# 

from functools import wraps


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


def main():
    spam(1, 2, 3, debug=True)


if __name__ == '__main__':
    main()
