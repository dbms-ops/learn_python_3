#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/9 18:22
# @user: Administrator
# @fileName: 打印输出到文件中
# @description: 将 print 函数输出重定向到一个文件中
#   打印字符串到文件中，文件必须以文本模式打开，如果文件是二进制打开就会出错


def print_to_file(filename='/tmp/file.log'):
    with open(filename, 'wt+') as f:
        print("Hello World", file=f)


def main():
    print_to_file()


if __name__ == '__main__':
    main()
