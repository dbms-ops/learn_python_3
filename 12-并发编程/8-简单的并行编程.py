#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 17:00
# @user: Administrator
# @fileName: 简单的并行编程
# @description: 程序要执行CPU 密集型工作，你想让他利用多核CPU 的优势来运行
#
#
import gzip
import io
import glob


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
    files = glob.glob(logdir + '/*.log.gz')
    all_robots = set()
    for robots in map(find_all_robots, files):
        all_robots.update(robots)
    return all_robots


def main():
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)


if __name__ == '__main__':
    main()
