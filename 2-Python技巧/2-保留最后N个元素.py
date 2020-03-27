#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/27 16:58
# @user: Administrator
# @fileName: 保留最后N个元素.py
# @description: 通过队列来实现保留最后的 N 个元素
#


from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def main():
    with open(r'D:\pycharm-project\Python3\2-Python技巧\somefile.txt') as f:
        for line, prevlines in search(f, 'python', 10):
            for pline in prevlines:
                print(pline, end=' ')
            print(line, end=' ')
            print('-' * 20)


if __name__ == '__main__':
    main()
