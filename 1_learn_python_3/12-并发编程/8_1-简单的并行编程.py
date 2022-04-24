#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 17:08
# @user: Administrator
# @fileName: 简单的并行编程
# @description: concurrent.futures
# 

import gzip
import io
import glob

from concurrent import futures

def find_robots(filename):
    """
        Find all of the hosts that access robots.txt in a single log file
    :param filename:
    :return:
    """
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                robots.add(fields[0])
    return robots
def find_all_robots(logdir):
    """
        Find all hosts across and entire sequence of files
    :param logdir:
    :return:
    """
    files = glob.glob(f'{logdir}/*.log.gz')
    all_robots = set()
    """
        from concurrent.futures import ProcessPoolExecutor
        
        with ProcessPoolExecutor() as pool:
            do work in parallel using pool
    """
    with futures.ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)
    return all_robots




def main():
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)


if __name__ == '__main__':
    main()
    