#!/data1/Python-2.7.4/bin/python2.7
# -*-coding:utf-8-*-
# time: 2020-06-20 22:07 
# user: lixun
# filename: 1-configParser
# description: 
# 
import sys
import configparser
from io import StringIO


def test():
    db_conf_write = configparser.ConfigParser(allow_no_value=True)
    db_conf = '/etc/snmp/yyms_agent_db_scripts/db_{port}.conf'.format(port=22)
    db_conf_write.read(db_conf)

    if "MySQL" not in db_conf_write.sections():
        db_conf_write.add_section("MySQL")

    # 添加以下 配置选项
    db_conf_write.set("MySQL", "ip", "127.0.0.1")
    db_conf_write.set("MySQL", "important_level", 1)
    db_conf_write.set("MySQL", "ip", "127.0.0.1")
    db_conf_write.set("MySQL", "business_level", 0)
    db_conf_write.set("MySQL", "user", "db_monitor")
    db_conf_write.set("MySQL", 'status', "online")

    with open(db_conf, 'a+') as configfile:
        db_conf_write.write(configfile)


def main():
    pass


if __name__ == "__main__":
    main()
    