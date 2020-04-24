#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/24 17:11
# @user: Administrator
# @fileName: 单元测试中的对象打补丁
# @description: 单元测试中需要给指定的对象打补丁,用来断言它们在测试中的期望行为
# 

from unittest.mock import patch
import example

@patch('example.func')
def test(x, mock_func):
    # Uses patched example.func
    example.func(x)
    mock_func.assert_called_with(x)

with patch('example.func') as mock_func:
    # Uses patched example.func
    example.func(x)
    mock_func.assert_called_with(x)



def main():
    p = patch('example.com')
    mock_func = p.start()
    example.func(x)
    mock_func.assert_called_with(x)
    p.stop()


if __name__ == '__main__':
    main()
    