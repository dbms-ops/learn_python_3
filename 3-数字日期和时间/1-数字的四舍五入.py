#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/3 15:46
# @user: Administrator
# @fileName: 数字的四舍五入
# @description:  对于浮点数进行指定进度的舍入计算
# 


def float_value():
    """
    对于数值进行标准的四舍五入运算, 四舍五入和数值的格式化不等价, 当一个值恰好在两个边界值的中间时，round 恰好会返回离他最近的整数
    1.5 或者 2.5 运算后的到的都是 2
    :return:
    """
    print(round(112.34521, 2))
    print(round(1.27, 1))
    print(round(-1.27, 1))
    print(round(1.235634, 1 ))


def main():
    float_value()


if __name__ == '__main__':
    main()
