#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/3 15:46
# @user: Administrator
# @fileName: 数字的四舍五入
# @description:  对于浮点数进行指定进度的舍入计算
# 

def float_value():
    """
    对于数值进行标准的四舍五入运算, 四舍五入和数值的格式化不等价,
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
