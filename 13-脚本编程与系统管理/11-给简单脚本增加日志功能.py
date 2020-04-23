#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-04-23 22:56 
# user: lixun
# filename: 11-给简单脚本增加日志功能
# description: 在脚本和程序中将诊断信息写入日志文件中
# 

import logging




def main():
    # Configure the logging system
    logging.basicConfig(
        filename='app.log',
        level=logging.ERROR
    )
    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    term = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", term)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')


if __name__ == "__main__":
    main()
    