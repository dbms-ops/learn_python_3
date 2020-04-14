#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/14 18:07
# @user: Administrator
# @fileName: 解析和修改XML文档
# @description: 读取一个XML文档,并且进行修改,将结果写入XML;
# 

from xml.etree.ElementTree import parse, Element



def read_xml_write_new_xml(filename='/tmp/pred.xml'):
    doc = parse(filename)
    root = doc.getroot()

    # remove  a few elements
    root.remove(root.find('sri'))
    root.remove(root.find('cr'))

    # Insert a few elements after
    print(root.getchildren().index(root.find('nm')))
    e = Element('spam')
    e.text = 'This is spam test'
    root.insert(2, e)

    # Write back to a new file
    doc.write('/tmp/pred_new.xml', xml_declaration=True)


def main():
    read_xml_write_new_xml()


if __name__ == '__main__':
    main()
