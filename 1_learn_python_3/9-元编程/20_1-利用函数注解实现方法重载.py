#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/21 21:05
# @user: Administrator
# @fileName: 利用函数注解实现方法重载
# @description: 
# 
import inspect
import types
import time


class MultiMethod:
    """
        Represents a single multimethod.
    """

    def __init__(self, name):
        self._methods = {}
        self.__name__ = name

    def register(self, meth):
        """
            Register a new method as a multimethod
        :param meth:
        :return:
        """
        sig = inspect.signature(meth)
        # Build a type signature from the method's annotations
        types = []
        for name, parm in sig.parameters.items():
            if name == 'self':
                continue
            if parm.annotation is inspect.Parameter.empty:
                raise TypeError(f'Argument {name} must be annotated with a type')
            if not isinstance(parm.annotation, type):
                raise TypeError(f'Argument {name} annotation must be a type')
            if parm.default is not inspect.Parameter.empty:
                self._methods[tuple(types)] = meth
            types.append(parm.annotation)
        self._methods[tuple(types)] = meth

    def __call__(self, *args):
        """
            Call a method based on type signature of the arguments
        :param args:
        :return:
        """
        types = tuple(type(arg) for arg in args[1:])
        if meth := self._methods.get(types, None):
            return meth(*args)
        else:
            raise TypeError(f'No matching method for types {types}')

    def __get__(self, instance, owner):
        """
            Descriptor method needed to make calls work in a class
        :param instance:
        :param owner:
        :return:
        """
        return types.MethodType(self, instance) if isinstance is not None else self


class MultiDict(dict):
    """
        Special dictionary to build multimethods in a metaclass
    """

    def __setitem__(self, key, value):
        if key in self:
            # If key already exists, it must be a multimethod or callable
            current_value = self[key]
            if isinstance(current_value, MultiMethod):
                current_value.register(value)
            else:
                mvalue = MultiMethod(key)
                mvalue.register(current_value)
                mvalue.register(value)
                super().__setitem__(key, mvalue)
        else:
            super().__setitem__(key, value)


class MultipleMeta(type):
    """
        Metaclass that allows multiple dispatch of methods
    """

    def __new__(cls, clsname, bases, clsdict):
        return type.__new__(cls, clsname, bases, dict(clsdict))

    @classmethod
    def __prepare__(cls, name, bases):
        return MultiDict()


class Spam(metaclass=MultipleMeta):
    def bar(self, x: int, y: int):
        print('Bar 1', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2:', s, n)


class Date(metaclass=MultipleMeta):

    def __init__(self, year: int, month: int, day: int):
        self.yeay = year
        self.month = month
        self.day = day

    def __init__(self):
        t = time.localtime()
        self.__init__(t.tm_year, t.tm_mon, t.tm_mday)


def main():
    s = Spam()
    print(s.bar(2, 3))
    print(s.bar('Hello'))


if __name__ == '__main__':
    main()
