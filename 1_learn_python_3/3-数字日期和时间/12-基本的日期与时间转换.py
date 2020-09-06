#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-04 16:44 
# user: lixun
# filename: 基本的日期与时间转换
# description: 执行简单的时间转换，天到秒，小时到分钟的转换
# 

from datetime import timedelta
from datetime import datetime


def detetime_change():
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)
    c = a + b
    print(c.days)
    print(c.seconds / 3600)
    print(c.total_seconds() / 3600)


def datetime_express():
    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))
    b = datetime(2012, 12, 21)
    d = b - a
    print(d.days)
    now = datetime.today()
    print(now)
    print(now + timedelta(days=-1,minutes=10))
    # datetime 是会自动处理闰年的
    a = datetime(2020, 3, 1)
    b = datetime(2020, 4, 3)
    print(a -b)
    print((a-b).days)
    c = datetime(2020,7,6)
    print((b-a).days)



def main():
    datetime_express()


if __name__ == "__main__":
    main()
