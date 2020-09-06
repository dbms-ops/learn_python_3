#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-12 09:48 
# user: lixun
# filename: 序列化Python对象
# description: 将 Python 对象序列化为一个字节流，用于将其保存到一个文件中、存储到数据库中或者通过网络进行传输
#   序列化可以使用pickle模块，将一个对象保存到文件中；
# ；

import pickle


def serialization_pickle():
    """
        将 Python 对象转换成字节流，存储到二进制文件中使用 dump 存储到字符串中使用 dumps
    :return:
    """
    data = [1, 2, 3, 4, 5, 6, (1, 2, 3, 4), (1, 2, 3, [1, 2, 4])]
    # 将 Python 对象转换成字节流
    with open("/tmp/data.bin", 'wb') as f:
        pickle.dump(data, f)
    # 将 Python 转换成为字符串
    s_data = pickle.dumps(data)
    print(s_data)


def load_data():
    """
        从文件中恢复对象使用 load，从字符串中，恢复对象使用loads
    :return:
    """
    # 从文件中恢复对象
    with open("/tmp/data.bin", 'rb') as f:
        data = pickle.load(f)
    # 从字节流中恢复对象
    data = [1, 2, 3, 4, 5, 6, (1, 2, 3, 4), (1, 2, 3, [1, 2, 4])]
    # 将 Python 转换成为字符串
    s_data = pickle.dumps(data)
    print(s_data)
    data_load = pickle.loads(s_data)
    print(data_load)


def main():
    load_data()


if __name__ == "__main__":
    main()
