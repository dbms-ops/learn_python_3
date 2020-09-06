#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-27 23:27 
# user: lixun
# filename: 查找字典的相同点
# description: 在字典中查找相同点，相同的键、相同的值
# 


def dictionary_operations():
    # 在字典中寻找共同点
    a = {
        'x': 1,
        'y': 2,
        'z': 3,
        'c': 5

    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }
    # 寻找字典的相同点，可以在两个字典的keys()和或者item()方法返回的结果集合上面进行操作
    # 查找两个字典的相同 key
    print(a.keys() & b.keys())
    # 查找在 a 中但是不在 b 中的 keys
    print(a.keys() - b.keys())
    # 查找字典中的 values
    print(a.items() & b.items())
    # 通过下列的方式可以过滤某些指定的元素，构造新字典
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)


def main():
    dictionary_operations()


if __name__ == "__main__":
    main()
