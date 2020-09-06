#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/4/16 17:23
# @user: Administrator
# @fileName: 在类中封装属性名
# @description: 封装类的实例上面的“私有”数据
#   Python 程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果。
#   第一个约定是任何以单下划线_ 开头的名字都应该是内部实现

class A:
    """
        Python 命名的几点规范
            1 非公共名称以单下划线开头
            2 你的代码会涉及到子类，并且有些内部属性应该在子类中隐藏起来，那么才考虑使用双下划线
            3 你定义的一个变量和某个保留关键字冲突, 单下划线作为后缀
    """
    def __init__(self):
        # An internal attribute
        self._internal = 0
        # A public attribute
        self.public = 1
    def public_method(self):
        """
            A public method
        :return:
        """
        return self.public
    def _internal_method(self):

        return self._internal




def main():
    pass


if __name__ == '__main__':
    main()
    