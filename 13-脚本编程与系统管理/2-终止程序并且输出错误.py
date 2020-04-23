#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 20:54
# @user: Administrator
# @fileName: 终止程序并且输出错误
# @description: 向标准错误打印一条消息并返回某个非零状态码来终止程序运行
# 

def exit_program():
    raise SystemExit('It tailed')


def main():
    exit_program()


if __name__ == '__main__':
    main()
