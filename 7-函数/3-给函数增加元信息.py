#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 21:40
# @user: Administrator
# @fileName: 给函数增加元信息
# @description: 给函数增加一些额外的信息,用于提示函数的用法
# 

def add_value(x: int, y: int) -> int:
    """
        使用函数参数注解是一个很好的办法，它能提示程序员应该怎样正确使用这个函数,python 解释器不会对这些注解添加任何的语义;
        它们不会被类型检查，运行时跟没有加注解之前的效果也没有任何差距尽管你可以使用任意类型的对象给函数添加注解(例如数字，字符串，对象实例等
        等)，不过通常来讲使用类或者字符串会比较好点
    :param x:
    :param y:
    :return:
    """
    return x + y


def main():
    help(add_value)


if __name__ == '__main__':
    main()
