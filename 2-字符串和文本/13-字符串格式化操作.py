#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/2 18:11
# @user: Administrator
# @fileName: 字符串格式化操作
# @description: 字符串基本的对齐操作,
# 

def string_aligned():
    text = 'Hello world'
    print(text.ljust(20))
    print(text.rjust(20))
    print(text.center(20))

    # 上述方式都是接受可选字符填充的
    print(text.rjust(20,'='))
    print(text.center(20,'*'))

    print(format(text,'>20'))
    print(format(text,'<20'))
    print(format(text,'^20'))

    # format 不仅仅适合于字符串对齐,同样适合数值等类型的初始化
    print('{:<10s} {:<10s} {:<10.2f}'.format("hello","world", 11.23457))





def main():
    string_aligned()


if __name__ == '__main__':
    main()
    