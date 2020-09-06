#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-14 23:04 
# user: lixun
# filename: 定义匿名或者内联函数
# description: 当一些函数很简单，仅仅只是计算一个表达式的值的时候，就可以使用 lambda 表达式来代替了
# 


def main():
    """
        lambda 表达式允许你定义简单函数，但是它的使用是有限制的,只能指定 单个表达式，它的值就是最后的返回值;不能够包含以下特性：
            多个语句
            条件表达式
            迭代
            异常处理
    :return:
    """
    # lambda 可以用于代替简单的函数
    add = lambda x, y: x + y
    print(add(2, 3))
    # lambda 表达式典型的使用场景是排序或数据 reduce 等
    names = ['David Beazley', 'Brian Jones',
             'Raymond Hettinger', 'Ned Batchelder']
    print(sorted(names, key=lambda name: name.split()[-1].lower()))


if __name__ == "__main__":
    main()
