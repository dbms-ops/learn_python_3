#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 20:57
# @user: Administrator
# @fileName: 命令行解析
# @description: 程序解析命令行选项
# 

import argparse


def main():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search some files')
    parser.add_argument(dest='filenames', metavar='filename', nargs='*')
    parser.add_argument('-p', '--pat', metavar='filename', required=True,
                        dest='patterns', action='append',
                        help='text pattern to search for')
    parser.add_argument('-v', dest='verbose', action='store_true',
                        help='verbose mode')
    parser.add_argument('-o', dest='outfile', action='store',
                        help='output file')

    parser.add_argument('--speed', dest='speed', action='store',
                        choices={'slow', 'fast'}, default='slow',
                        help='search speed')

    args = parser.parse_args()

    print(args.filenames)
    print(args.patterns)
    print(args.verbose)
    print(args.outfile)
    print(args.speed)
