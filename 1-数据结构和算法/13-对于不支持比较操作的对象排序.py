#!/data1/Python2.7/bin/python2.7
# -*-coding:utf-8-*-
# @date: 2020/3/30 16:26
# @user: Administrator
# @fileName: 对于不支持比较操作的对象排序.py
# @description: 对于同一个类的实例进行排序,但是类原生是不支持比较操作的
#   通过 sorted()函数来解决这个问题,对于关键字 key 传递一个 callable 对象,该对象对于传入的对象返回一个值,sorted
#   可以用这些值来进行排序;
#   ;

from operator import attrgetter


class User():
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return 'User( {}, {}, {} )'.format(
            self.user_id,
            self.first_name,
            self.last_name)



def sort_not_compare():
    users = [User(23,'li','name'), User(3,'tom', 'mouse'), User(99,'Alice','Bob')]
    print(users)
    # 使用 attrgetter 来构造 key
    print(list(sorted(users, key=attrgetter('user_id'))))
    # 使用 lambda 来构造 key
    print(sorted(users, key=lambda u: -u.user_id))
    print(sorted(users, key=lambda u: u.user_id))
    print(sorted(users, key=attrgetter('last_name', 'first_name')))

    # 上述技巧同样适合与 max 与 min 函数
    print(min(users, key=attrgetter('user_id')))
    print((max(users, key=attrgetter('last_name'))))

    #

def main():
    sort_not_compare()


if __name__ == '__main__':
    main()
