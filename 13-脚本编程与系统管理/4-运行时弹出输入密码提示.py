#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 21:04
# @user: Administrator
# @fileName: 运行时弹出输入密码提示
# @description: 密码输入提示
# 

import getpass




def main():
    user = getpass.getuser()
    passwd = getpass.getpass()
    print(user,passwd)


if __name__ == '__main__':
    main()
