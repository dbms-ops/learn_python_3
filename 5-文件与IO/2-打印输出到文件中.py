#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/9 18:22
# @user: Administrator
# @fileName: 打印输出到文件中
# @description: 将 print 函数输出重定向到一个文件中
# 

def print_to_file(filename='/tmp/file.log'):
    with open(filename, 'rt+') as f:
        print("Hello World", file=f)



def main():
    print_to_file()

if __name__ == '__main__':
    main()
    