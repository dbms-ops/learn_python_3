#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/27 18:28
# @user: Administrator
# @fileName: 字典计算.py
# @description: 对于字典进行各种计算,最大值,最小值,排序等
#   用于对于字典执行: 最小值 最大值,排序等计算


def dictionary_calculation():
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # 对于字典进行操作,首先需要将 键和值反转过来
    # zip()函数了解下
    min_price = min(zip(prices.values(), prices.keys()))
    print(min_price)
    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)
    print(sorted(zip(prices.values(), prices.keys())))

    # 不利用 zip 最常见的一种处理方式
    print(min(prices.values()))
    print(min(prices.keys()))
    print()
    print(min(prices, key=lambda k: prices[k]))
    print(min(prices, key=lambda k: prices[k]), prices[min(prices, key=lambda k: prices[k])])


def main():
    dictionary_calculation()


if __name__ == '__main__':
    main()
