#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/22 15:17
# @user: Administrator
# @fileName: tom.py
# @description: 
# 
import sys
def spam():
    print(sys._getframe().f_code.co_name)

def grok():
    print(sys._getframe().f_code.co_name)

blah = 42

__all__ = [
    'spam',
    'grok'
]
