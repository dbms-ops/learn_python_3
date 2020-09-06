#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/21 21:36
# @user: Administrator
# @fileName: 避免重复的属性方法
# @description: 在类中需要重复的定义一些执行相同逻辑的属性方法,比如类型检查等
# 

def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(
                '{} must be a {}'.format(name, expected_type)
            )
        setattr(self, storage_name, value)

    return prop


class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    tom = Person('mouse', 12)
    print(tom.name, tom.age)
    jerry = Person(12,41)


if __name__ == '__main__':
    main()
