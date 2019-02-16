
# __dict__属性
if __name__ == '__main__':

    # Python一切皆对象，python是用__dict__来管理对象的
    class A(object):
        """
        Class A.
        """

        # 类变量
        a = 0
        b = 1

        def __init__(self):
            # 实例变量覆盖了类变量，但是类变量的值没有变
            self.a = 2
            self.b = 3

        def test(self):
            print('a normal func.')

        @staticmethod
        def static_test(self):
            print('a static func.')

        @classmethod
        def class_test(self):
            print('a calss func.')

    # 类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类__dict__里的
    A.__dict__


    obj = A()
    obj.__dict__ # 对象的__dict__中存储了一些self.xxx的一些东西
    A.__dict__ # 类变量的a还是0，b还是1，实例变量的a=2，b=3


    # --------------------------------------下面这些是没有__dict__的------------------------------------------------------
    num = 3
    ll = []
    dd = {}

    num.__dict__
    ll.__dict__
    dd.__dict__

    # --------------------------------------父类和子类的__dict__---------------------------------------------------------
    class Parent(object):
        a = 0
        b = 1
        count = 0

        def __init__(self):
            self.a = 2
            self.b = 3

        def p_test(self):
            pass


    class Child(Parent):
        a = 4
        b = 5

        def __init__(self):
            super(Child, self).__init__()
            Parent.count += 1 # 实际上把类属性当成一个外部变量来修改
            # self.a = 6
            # self.b = 7

        def c_test(self):
            pass

        def p_test(self):
            pass

    Parent.count

    p = Parent()
    c = Child()
    Parent.count

    Parent.__dict__
    Child.__dict__

    p.__dict__
    c.__dict__


#
if __name__ == '__main__':
    pass