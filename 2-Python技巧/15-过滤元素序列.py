#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/30 17:26
# @user: Administrator
# @fileName: 过滤元素序列.py
# @description:
#       需求: 对于一个数据序列,利用规则从中提取出一些需要的值或者是缩短序列
#       解决办法: 使用列表推导来完成 上述需求;
#

from itertools import compress


def list_cull():
    # 列表推导可以方便的解决上面的问题,但是结果集很大的时候就会占据很大的内存;
    my_list = [1,4,-5,10,-7,2,3,-1]
    cull_list_positive = [ n for n in my_list if n > 0]
    print(cull_list_positive)
    cull_list_negative = [ n for n in my_list if n < 0]
    print(cull_list_negative)

    # 使用生成器表达式改善内存占用, 使用生成器表达式过滤元素
    pos = (n for n in my_list if n > 0)
    print(next(pos))
    print(next(pos))


def is_int(val):
    # 对于能够转换成为整形的进行保留, 否则丢弃这个值
    try:
        x = int(val)
        return True
    except ValueError:
        return False


def is_int_example():
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    # 利用 filter 函数创建一个迭代器,通过列表转换得到一个列表
    ivalues = list(filter(is_int, values))
    print(ivalues)
    print("the type is: ", type(filter(is_int, values)))
    print("print the first one value: ", next(filter(is_int, values)))

def replace_value():
    # 过滤操作可以用于将 不符合要求的数替换成指定的数值
    clip_neg = [1, 4, 0, 10, 0, 2, 3, 0]
    print("未经修改的数值: ",clip_neg)

    clip_pos = [n if n > 0 else '不符合' for n in clip_neg]
    print("修改后的数值: ", clip_pos)

def compress_count():
    '''
    利用 itertools.compress() 进行数值过滤;
    它以一个iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数
    然后输出iterable 对象中对应选择器为 True 的元素
    当你需要用另外一个相关联的序列来过滤某个序列的时候，这个函数是非常有用的;
    :return:
    '''
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    more_5 = [ n > 2 for n in counts]
    print("True or False: ", more_5)
    print("count 大于5的值:", list(compress(addresses, more_5)))


def main():
    compress_count()

if __name__ == '__main__':
    main()
    