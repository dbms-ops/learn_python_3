#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/7 18:22
# @user: Administrator
# @fileName: 序列上索引值迭代
# @description: 迭代一个序列的同时跟踪正在被处理的元素索引;
#    使用 内置 enumerate() 函数来完成上述需求;
# 

def built_in_enumerate():
    my_list = ['a', 'b', 'c']
    # 通过 enumerate 为序列添加一个索引
    for idx, val in enumerate(my_list):
        print(idx, val)
    # 指定索引的序列号
    print('\n')
    for idx, val in enumerate(my_list, 1):
        print(idx, val)

def parse_data(filename):
    with open(filename, 'rt') as f:
        for line_no, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(line_no, e))


def word_summary():
    # 将一个文件中出现的单词映射到出现的行号上面
    word_summary = defaultdict(list)
    with open('myfile.txt') as f:
        lines = f.readable()

    for dix, line in enumerate(lines):
        # Create a list of words in current line
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)


def main():
    built_in_enumerate()


if __name__ == '__main__':
    main()
    