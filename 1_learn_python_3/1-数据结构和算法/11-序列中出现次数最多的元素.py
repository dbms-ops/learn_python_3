#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-29 21:04 
# user: lixun
# filename:  序列中出现次数最多的元素
# description: 查询一个序列中出现次数最多的元素；
#   通过：collections.Counter 用于解决上述问题；
# 

from collections import Counter


def collections_counter():
    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the',
        'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under'
    ]

    # 底层实现上 Counter 接受任意的 可 hashable 元素构成的序列； 一个 counter 对象就是一个字典，用于将元素的次数 作为值
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)
    print(word_counts['not'])


def main():
    collections_counter()


if __name__ == "__main__":
    main()
