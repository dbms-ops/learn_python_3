#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/18 10:34
# @user: Administrator
# @fileName: 实现一种数据模型或者类型系统
# @description: 在对某些实例属性赋值时进行检查, 自定义属性赋值函数，这种情况下最好使用描述器
# 

class Descriptor:
    """
        Base class. Uses a descriptor to set a value
    """

    def __init__(self, name, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    """
        # Descriptor for enforcing types
    """
    expected_type = type(None)

    def __set__(self, instance, value):
        if not instance(value, self.expected_type):
            raise TypeError(f"Excepted {len(self.expected_type)}")
        super().__set__(instance, value)


class Unsigned(Descriptor):
    """
        # Descriptor for enforcing values
    """

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Excepted > 0")
        super().__set__(instance, value)


class MaxSized(Descriptor):
    """
        # Descriptor for enforcing values
    """

    def __init__(self, name=None, **opts):
        if 'size'  not in opts:
            raise TypeError("missing size option")
        super().__init__(name, **opts)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError(f"size must be < {str(self.size)}")
        super().__set__(instance, value)


def main():
    pass


if __name__ == '__main__':
    main()
