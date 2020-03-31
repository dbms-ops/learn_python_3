#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/31 15:12
# @user: Administrator
# @fileName: 从字典中提取一个子集.py
# @description: 从字典中获取一个字典的子集;
#      从字典中快速的扩区一个字典的子集可以使用字典推导;
# 

def dict_derivation():
    # 利用字典推导从字典中获取 符合条件的字典子集
    price = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    # 字典推导表达式
    price_over_100 = {key: value for key,value in price.items() if value > 100}
    print("price_over_200: ", price_over_100)

    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    price_in_tech_names = {key: value for key, value in price.items() if key in tech_names}
    print("price_in_tech_names: ", price_in_tech_names)
    # 一个更加难理解的方式
    price_in_tech_names = {key: price[key] for key in price.keys() & tech_names}
    print("price_in_tech_names: ", price_in_tech_names)


def dict_function_derivation():
    # 利用 dict() 函数来完成字典推导: 大多数通过字典推导可以做到的,通过创建一个元组序列,然后传递给dict()都是可以实现的
    #
    price = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    price_over_100 = dict((key,value) for key, value in price.items() if value > 100)
    print('price_over_100: ', price_over_100)



def main():
    dict_function_derivation()


if __name__ == '__main__':
    main()
    