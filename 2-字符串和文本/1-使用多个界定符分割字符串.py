#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/1 15:43
# @user: Administrator
# @fileName: 使用多个界定符分割字符串
# @description: 将一个分隔符不固定的字符串分割成多个字段;
#   使用re.split()来完成这个操作;
# 

import re


def re_split():
    """
    通过 re.split 指定多个字符构建正则表达式,使用该函数时, 如果使用括号捕获分组,被匹配到的文本也会出现在结果列表中
    :return:
    """
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    line_split = re.split(r'[;,\s]\s*', line)
    print(type(line_split))
    print("返回匹配的结果集左右两边的元素", line_split)
    line_split_result = re.split(r'([;|,|\s]\s*)', line)
    print("包含匹配结果集: ", line_split_result)

    # 获取分割字符串 也有可能会用到
    values = line_split_result[::2]
    delimiters = line_split_result[1::2] + ['']
    print(values)
    print(delimiters)

    # 不保留分割字符串,但是使用括号分组正则表达式
    like_line_split = re.split(r'(?:,|;|\s)\s*', line)
    print("使用括号元素的正则表达式查找", like_line_split)


def main():
    re_split()


if __name__ == '__main__':
    main()
