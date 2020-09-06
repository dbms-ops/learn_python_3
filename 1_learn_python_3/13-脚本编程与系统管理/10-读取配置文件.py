#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 21:59
# @user: Administrator
# @fileName: 10-读取配置文件.py
# @description: 
#

from configparser import ConfigParser




def main():
    cfg = ConfigParser()
    cfg.read('config.ini')
    print(cfg.sections())
    print(cfg.get('installation','library'))
    cfg.getboolean('debug','log_errors')
    

if __name__ == '__main__':
    main()
    