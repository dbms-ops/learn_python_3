#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/20 18:10
# @user: Administrator
# @fileName: 通过装饰器扩充类的功能
# @description: 通过反省或者重写类定义的某部分来修改它的行为，但是你又不希望使用继承或元类的方式
#

def log_getattribute(cls):
    # Get the original implementation
    orig_getattribute = cls.__getattribute__

    # Make a new definition
    def new_getattribute(self, name):
        print('getting', name)
        return orig_getattribute(self, name)

    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls


# Example use
@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


def main():
    a = A(42)
    print(a.x)
    print(a.spam())


if __name__ == '__main__':
    main()
