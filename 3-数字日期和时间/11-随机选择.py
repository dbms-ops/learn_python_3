#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 16:18 
# user: lixun
# filename: 随机选择
# description: 从一个序列中随机抽取若干个元素，或者生成几个随机数
# 

import random

def random_choice_value():
    # 从列表中随机选取一个元素
    values = [1, 2, 3, 4, 5]
    print(random.choice(values))
    # 随机选取多个值
    print(random.sample(values, 2))
    print(random.sample(values, 3))

    # 打乱序列里面元素的顺序
    random.shuffle(values)
    print(values)
    random.shuffle(values)
    print(values)

    # 生成随机数, 在0 10 生成随机数
    print(random.randint(0,10))

    # 获取 N 位随机的二进制整数
    print(random.getrandbits(200))
    # 通过 seed 初始化随机数种子
    random.seed(1345)


def main():
    random_choice_value()


if __name__ == "__main__":
    main()
    