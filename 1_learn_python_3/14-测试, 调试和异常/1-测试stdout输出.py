#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/24 17:04
# @user: Administrator
# @fileName: 测试stdout输出
# @description: 有个方法会输出到标准输出中（sys.stdout）。也就是说它会将文本打印到屏幕上面;
# ;
# 

from io import StringIO
from unittest import TestCase
from unittest.mock import patch

def url_print(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol,host,domain)
    print(url)
class TestURLPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO) as fake_out:
            url_print(protocol,host,domain)
            self.assertEqual(fake_out.getvalue(), expected_url)



def main():
    pass


if __name__ == '__main__':
    main()
    