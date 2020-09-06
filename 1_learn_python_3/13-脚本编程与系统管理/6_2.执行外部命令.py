#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 21:30
# @user: Administrator
# @fileName: 执行外部命令
# @description: 对子进程做更复杂的交互，比如给它发送输入
# 

import subprocess

def subprocess_example():
    """

    :return:
    """
    text = b"""
        hello world
        this is a test
        goodbye
    """
    # Launch a command with pipes
    p = subprocess.Popen(['wc'],
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE)
    # Send the data and get the output
    stdout, stderr = p.communicate(text)

    # To interpret as text, decode
    out = stdout.decode('utf-8')
    err = stderr.decode('utf-8')




def main():
    pass


if __name__ == '__main__':
    main()
    