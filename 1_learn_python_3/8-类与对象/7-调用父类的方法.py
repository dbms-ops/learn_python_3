#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 20:24
# @user: Administrator
# @fileName: 调用父类的方法
# @description: 在子类中调用父类的某个已经被覆盖的方法
#    为了调用父类(超类) 的一个方法，可以使用super() 函数;

class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        # Call parent spam()
        super().spam()


class C:
    def __init__(self):
        self.x = 0


class D(C):
    def __init__(self):
        # super()函数用于初始化父类的初始化函数
        super().__init__()
        self.y = 1


class Proxy:
    def __init__(self, obj):
        self._obj = obj
    # Delegate attribute lookup to internal obj
    def __getattr__(self, item):
        return getattr(self._obj, item)
    # Delegate attribute assignment
    def __setattr__(self, key, value):
        # Call original __setattr__
        if key.startswith('_'):
            super().__setattr__(key,value)
        else:
            setattr(self._obj, key, value)



def main():
    pass


if __name__ == '__main__':
    main()
