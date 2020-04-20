#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-19 20:41 
# user: lixun
# filename: 利用装饰器强制进行函数上面的类型检查
# description: 某种编程规约，你想在对函数参数进行强制类型检查
#   能对函数参数类型进行断言
# ；

from inspect import signature
from functools import wraps


def type_assert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name, bound_types[name])
                        )
            return func(*args, **kwargs)

        return wrapper

    return decorate


def main():
    @type_assert(int, z=int)
    def spam(x, y, z=42):
        print(x, y, z)

    spam(1, 2, 3)
    spam(1, '2', 3)
    # spam(1,2,'hello')
    print(__debug__)



if __name__ == "__main__":
    main()
