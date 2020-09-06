#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/9 16:00
# @user: Administrator
# @fileName: 顺序迭代合并后的排序迭代对象
# @description: 存在一系列序列,, 合并到一个排序序列上面并且进行迭代
# heapq.merge() 函数用于解决这个问题

import heapq


def merge_heapq_example():
    """
        heapq.merge 可迭代特性意味着它不会立马读取所有序列,可以在非常长的序列中使用它,并且不担心开销;
        heapq.merge() 接受的序列必须是受下进行过排序的, 函数本身对于数据不会进行排序,也不会对于输入进行排序检测;
    :return:
    """
    a = [1, 4, 7, 10, 9]
    b = [2, 5, 6, 11]
    for c in heapq.merge(a, b):
        print(c)

def merge_sort_file():
    with open('sorted_file1','rt') as file_1, \
        open('sorted_file2','rt') as file_2, \
        open('merged_file','rt') as out_f:
        for line in  heapq.merge(file_1,file_2):
            out_f.write(line)

def main():
    merge_heapq_example()


if __name__ == '__main__':
    main()
