#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-12 09:27 
# user: lixun
# filename: 创建临时文件和文件夹
# description: 在程序运行时，创建一个临时的文件或者目录，在使用完成之后可以自动销毁；
#   使用 tempfile 模块中的函数来完成上述需求
# 

from tempfile import TemporaryFile
from tempfile import NamedTemporaryFile
from tempfile import TemporaryDirectory


def create_temp_file():
    """
        临时文件在 函数返回，或者使用 close 关闭后文件会自动被删除
        文本文件打开 模式 w+t：读写
        二进制文件打开 模式：w + b：读写，支持和 open函数一样的参数
        with TemporartFile('w+t',encoding='utf-8',errors='ignore') as f:
            通过上面函数创建的文件都是匿名的，文件所在的目录都是不存在的
    :return:
    """
    with TemporaryFile('w+t') as f:
        # Read/write to the file
        f.write('Hello World\n')
        f.write("testing\n")

        f.seek(0)
        data = f.read()
        print(data)
        f.close()


def create_named_temp_file():
    """
        创建一个位于 /tmp/目录下的临时文件，传递 delete=False 表示在使用完成后，不删除该文件
    :return:
    """
    with NamedTemporaryFile('w+t',delete=False) as f:
        print('filename is ', f.name)
        with open(f.name, 'w') as temp_f:
            temp_f.write('Hello world\n')

def create_temp_dir():
    """
        该目录使用完成后，目录和目录里面的内容都会自动被删除
    :return:
    """
    with TemporaryDirectory() as dirname:
        print('dirname is', dirname)




def main():
    create_named_temp_file()


if __name__ == "__main__":
    main()