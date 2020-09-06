#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 20:51
# @user: Administrator
# @fileName: 子类中扩展property
# @description: 扩展定义在父类中的property
# ;
# 

class Person:
    def __init__(self, name):
        self.name = name
    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._name = value
    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")

class SubPerson(Person):
    """
        继承自 Person 并扩展了 name 属性的功能
    """
    @property
    def name(self):
        print("Getting name")
        return super().name
    @name.setter
    def name(self, value):
        print("Setting name to ", value)
        super(SubPerson,SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


def sub_person_example():
    s = SubPerson('Guido')
    print(s)
    print(s.name)
    s.name = "Larry"

# A descriptor

class String:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance,cls):
        if isinstance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Except a string')
        instance.__dict__[self.name] = value
# A class with a descriptor
class Person:
    name = String('name')
    def __init__(self, name):
        self.name = name

# Extending a descriptor with a property
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name
    @name.setter
    def name(self, value):
        print('Setting name to', value)
        super(SubPerson,SubPerson).name.__set__(self,value)
    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson,SubPerson).name.__delete__(self)


def main():
    sub_person_example()


if __name__ == '__main__':
    main()
    