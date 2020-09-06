#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/21 21:50
# @user: Administrator
# @fileName: 局部变量域中执行代码
# @description: 在使用范围内执行某个代码片段,并且希望在之后的所有结果都是不可见的
#   ;
# ;


def test():
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)


def main():
    test()


if __name__ == '__main__':
    main()
