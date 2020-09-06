#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/24 17:17
# @user: Administrator
# @fileName: 创建自定义异常
# @description: 将底层异常包装成自定义的异常
# 创建新的异常很简单——定义新的类，让它继承自 Exception,

class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

class TimeoutError(NetworkError):
    pass

class ProtocolError(NetworkError):
    pass

try:
    pass
except TimeoutError as e:
    pass
except ProtocolError as f:
    pass
finally:
    pass




def main():
    pass


if __name__ == '__main__':
    main()
    