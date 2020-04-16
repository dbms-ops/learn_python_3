#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 16:32
# @user: Administrator
# @fileName: 自定义字符串的格式化
# @description: 
# 

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


def date_example():
    d = Date(2012, 12, 21)
    print(format(d))
    print(format(d, 'mdy'))
    print('the date is {:ymd}'.format(d))
    print('The date is {:mdy}'.format(d))


def main():
    date_example()


if __name__ == '__main__':
    main()
