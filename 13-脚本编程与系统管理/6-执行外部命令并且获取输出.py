#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/23 21:10
# @user: Administrator
# @fileName: 执行外部命令并且获取输出
# @description: subprocess 的 check_output函数
# 

import subprocess
import shlex

def get_output():
    out_bytes = subprocess.check_output(['netstat', '-a', '-n', '-t'])
    out_text = out_bytes.decode('utf-8')
    print(out_text)

def run_shell():
    # 执行 shell 命令
    out_bytes = subprocess.check_output('grep "python" /etc/passwd', shell=True)
    out_text = out_bytes.decode('utf-8')
    print(out_text)

def get_error():
    try:
        out_bytes = subprocess.check_output(['cmd','args','args'])
    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        code = e.returncode

    out_bytes = subprocess.check_output(['cmd', 'args', 'args'],
                                        stderr=subprocess.STDOUT)
    try:
        out_bytes = subprocess.check_output(['cmd', 'args', 'args'],
                                            timeout=10)
    except subprocess.TimeoutExpired as e:
        raise RuntimeError("Timeout")





def main():
    run_shell()


if __name__ == '__main__':
    main()
    