#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-03-28 18:17 
# user: lixun
# filename: 删除序列相同的元素，并且保持顺序
# description: 在一个序列上面，保持序列的元素，并且消除序列的重复值
#       hashable 类型：Python 内置的不可变类型都是可 hash 的，字典的 key 和set 使用了hash；
#       列表和字典都是不可hash的；；
#       带 yield 的函数都是生成器,而不仅仅是一个函数；
#       函数：
#           1、在第一次调用时就会执行，并且返回结果；
#           2、函数通过return返回结果，当执行到；return 语句时，返回结果，函数执行结束；
#       yield：
#           1、通过yield进行返回，得到的就是一个迭代器；
#           2、迭代器在初始化时，并不会执行，调用next()方法时会执行；
#           3、迭代器在 yield时返回，下次调用从yield下一条语句开始执行；


def dedupe(items):
    # 该方法适合于序列中的元素为 hashable 时可用,该函数同样可以用于消除文件中的重复行
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dedupe_test():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))


def dedupe_hash(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
        seen.add(val)


def dudupe_hash_test():
    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(list(dedupe_hash(a, key=lambda d: (d['x'], d['y']))))
    print(list(dedupe_hash(a, key=lambda d: d['x'])))


def main():
    dedupe_test()
    dudupe_hash_test()


if __name__ == "__main__":
    main()
