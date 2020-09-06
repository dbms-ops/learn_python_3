#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-11 21:24 
# user: lixun
# filename: 打印不合法的文件名
# description: 打印文件名出现 UnicodeEncodeError， 以及：surrogates not allowed；
#   默认情况下，Python 假定所有文件名都已经根据 sys.getfilesystemencoding()进行编码，但是某些文件名可能未正确编码，
#   ；
# 

def bad_filename(filename):
    return repr(filename)[1:-1]

def print_filename(filename):
    try:
        print(filename)
    except UnicodeEncodeError:
        print(bad_filename(filename))



def main():
    pass

if __name__ == "__main__":
    main()
    