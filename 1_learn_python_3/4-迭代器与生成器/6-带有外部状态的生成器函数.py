#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-06 16:26 
# user: lixun
# filename: 带有外部状态的生成器函数
# description:
#   定义一个生成器函数，但是会调用某个暴露给用户的外部状态值
#   生成器函数暴露外部状态给用户，可以简单的实现一个类，将生成器函数放在__iter__() 方法中
# 


from collections import deque


class line_history:
    def __init__(self, lines, histlen=4):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        # enumerate(self.lines, 1): 用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
        # 一般用在 for 循环当中
        for line_number, line in enumerate(self.lines, 1):
            self.history.append((line_number, line))
            yield line

    def clear(self):
        self.history.clear()


def main():
    with open('/etc/passwd') as f:
        lines = line_history(f)
        for line in lines:
            if 'python' in line:
                for line_no, hline in lines.history:
                    print(f'{line_no} : {hline}', end='')


if __name__ == "__main__":
    main()
