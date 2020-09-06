#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/24 17:34
# @user: Administrator
# @fileName: 输出警告信息
# @description: 自己的程序能生成警告信息
# 
import warnings

def func(x,y,logfile=None, debug=False):
    if logfile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)
    else:
        pass



def main():
    pass


if __name__ == '__main__':
    main()
    