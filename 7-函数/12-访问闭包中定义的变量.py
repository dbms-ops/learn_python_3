#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 15:06
# @user: Administrator
# @fileName: 访问闭包中定义的变量
# @description: 扩展某个函数中的闭包,允许访问和修改函数内部的变量
#   通常来讲，闭包的内部变量对于外界来讲是完全隐藏的

def sample():
    """
        添加方法访问闭包里面的值,类似于类,提供方法,访问类里面的变量
    :return:
    """
    n = 0

    # Closure function
    def func():
        print('n = ', n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


def inline_sample():
    f = sample()
    f()
    f.set_n(10)
    f()
    f.get_n()


def main():
    inline_sample()


if __name__ == '__main__':
    main()
