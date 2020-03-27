# -*-coding:utf-8-*-
#!/data1/Python3.5/bin/python3.5


# 文件操作在Python 2 和 Python 3 上面是存在区别的，这里说明对于Python 3 的文件操作方式
#

path = "/root/tmp/pycharm_project_368/file_encoding"

with open(path, "wb") as file_encoding:
    write_string = "Never too old to learn, never too late to turn."
    file_encoding.write(write_string.encode("utf-8"))

with open(path,'rb') as file_decoding:
    data = file_decoding.read()
    print(data)
    print(type(data))
    print(data.decode('utf-8'))
#



if __name__ == '__main__':
    pass

