#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/1 20:20
# @user: Administrator
# @fileName: 使用shell通配符匹配字符串
# @description:  利用 unix Shell 中的通配符 (*.py, Dat[0-9]*.csv) 匹配文本字符串
# ;

from fnmatch import fnmatch, fnmatchcase

def string_fnmatch():
    # fnmatch 函数适合于简单的文件名和字符匹配,更加强大的功能使用 glob 模块
    # *: 撇配任意多个字符
    result = fnmatch("foo.txt",'*.txt')
    print(result)
    # 匹配任意单个字符
    result = fnmatch('foo.txt', '?oo.txt')
    print(result)
    # 匹配数字集合
    result = fnmatch('Dat45.csv','Dat[0-9]*')
    print(result)
    # 匹配文件名列表
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    result = [name for name in names if fnmatch(name,'Dat*.csv')]
    print(result)
    # fnmatch() 函数对于底层的操作系统的大小写是敏感的在 mac OS 上面是敏感的

    # 完全按照输入的大小写进行匹配
    print(fnmatchcase('foo.txt', '*.TXT'))


def not_file_name():
    # 通过 fnmatchcase 匹配
    addresses = [
        '5412 N CLARK ST',
        '1060 W ADDISON ST',
        '1039 W GRANVILLE AVE',
        '2122 N CLARK ST',
        '4802 N BROADWAY',
    ]
    result = [addr for addr in addresses if fnmatchcase(addr, '* ST')]
    print(result)
    # 支持按照 Unix shell 风格的字符表达式进行匹配
    result = [addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')]
    print(result)


def main():
    not_file_name()


if __name__ == '__main__':
    main()