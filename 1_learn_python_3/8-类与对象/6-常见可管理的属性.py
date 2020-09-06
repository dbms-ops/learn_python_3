#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 17:39
# @user: Administrator
# @fileName: 常见可管理的属性
# @description: 给某个实例attribute 增加除访问与修改之外的其他处理逻辑,比如类型检查,合法性验证
#   自定义某个属性的一种简单方法是将它定义为一个property

class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class PersonGetSet:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name
    # Setter function
    def set_first_name(self,value):
        if not isinstance(value,str):
            raise TypeError("Excepted a string")
        self._first_name = value
    # Deleter function (optional)
    def del_first_name(self):
        raise AttributeError("can't delete attribute")
    # Make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)



def person_example():
    a = Person('Linux')
    # Calls the getter
    print(a.first_name)
    # Calls the setter
    # a.first_name = 42
    # del a.first_name


def main():
    person_example()


if __name__ == '__main__':
    main()
    