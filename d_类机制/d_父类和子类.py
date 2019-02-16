
# super()的用法，子类方法中使用父类的方法
if __name__ == '__main__':
    # ----------------------------------调用父类的方法-------------------------------------------------------------------
    # 1、显式调用父类的方法
    class Parent(object):

        def print_a(self):
            self.a = 1
            print(self.a)


    class Child(Parent):

        def __init__(self):
            pass

        def print_a(self):
            Parent.print_a(self) # 显式地调用父类方法， self不能省略，把self传给父类的方法，父类的self.a其实就是子类实例作用域
            self.a = 2
            print(self.a)


    testa = Child()

    testa.print_a()
    testa.a

    # --------------------------------super来调用------------------------------------------------------------------------
    class SuperClass(object):
        def act(self):
            print("Super Class act method ...")


    class SubClass(SuperClass):
        def act(self):
            super().act()  # 这里不能将self传给act()
            # super(SubClass,self).act()     # py2.x 调用父类，过于复杂，这个可以正常执行
            print("SubClass act method ...")

    sub = SubClass()
    sub.act()


    # 2、多重继承
    class A(object):
        def act(self):
            print("call A act method ....")


    class B(object):
        def act(self):
            print("call B act method ....")


    class C(B, A):  # 搜索的顺序会从B开始搜索，B存在act方法则调用并返回，不再继续搜索
        def act(self):
            super().act()


    c = C()
    c.act()

    # 3、super不支持运算符操作，如super()[index]
    class E(object):
        def __getitem__(self, item):
            print("call E __getitem__ method ...")


    class F(E):
        def __getitem__(self, item):
            print('call F __getitem__ method ..')
            E.__getitem__(self, item)
            super().__getitem__(item)
            super()[item]  # 不支持运算符操作，'super' object is not subscriptable


    f = F()
    f[2]


    # 4、运行时可以改变继承树
    class X(object):
        def m1(self):
            print("call X method")


    class Y(object):
        def m1(self):
            print("call Y method")


    class Z(X):
        def m1(self):
            super().m1()

    z = Z()
    z.m1()
    print("change Z class base for Y ....")
    Z.__bases__ = (Y,)  # 改变继承树
    z.m1()


    # 5、能够在多继承中按照广度优先的继承树搜索关系链来有序地调用与父类相同名称的方法，且在每个子类拥有super的都会执行父类方法
    class IA(object):
        def __init__(self):
            print("call IA init ...")  # 基类IA没有super()，没有意义


    class IB(IA):
        def __init__(self):
            print("call IB init ....")
            super().__init__()


    class IC(IA):
        def __init__(self):
            print("call IC init ....")
            super().__init__()


    class ID(IC, IB):
        def __init__(self):
            print("call ID init ...")
            super().__init__()


    def test_ID():
        d = ID()
        print(ID.mro())


    if __name__ == '__main__':
        test_ID()


    # 6、在父类没有使用super()情况下，在子类中将使用类的继承树搜索方式来匹配父类方法，找到并返回调用，不再继续往下搜索

    class P1(object):
        def __init__(self):
            print("call P1 init ...")


    class P2(object):
        def __init__(self):
            print("call P2 init ...")


    # 以下两种方式等价
    class S(P2, P1):
        pass  # 默认调用父类的构造方法,如果有定义的话并且子类没有调用super()将不会调用父类方法


    class S(P2, P1):
        def __init__(self):
            super().__init__()


    if __name__ == '__main__':
        S()


    # 7、能够在多继承中按照广度优先的继承树搜索关系链来有序地调用与父类相同名称的方法，且在每个子类拥有super的都会执行父类方法
    class IA(object):
        def __init__(self):
            print("call IA init ...")  # 基类IA没有super()，没有意义


    class IB(IA):
        def __init__(self):
            print("call IB init ....")
            super().__init__()


    class IC(IA):
        def __init__(self):
            print("call IC init ....")
            # super().__init__()


    class ID(IC, IB):
        def __init__(self):
            print("call ID init ...")
            super().__init__()


    def test_ID():
        d = ID()
        print(ID.mro())


    if __name__ == '__main__':
        test_ID()


    # 8、子类多继承中,按上述所说的,如果父类存在super()调用，将以广度优先地处理方式进行搜索,比如
    class P1(object):
        def __init__(self):
            print("call P1 init ...")
            super().__init__()


    class P2(object):
        def __init__(self):
            print("call P2 init ...")
            super().__init__()


    class S(P2, P1):
        # 最先搜索到的父类是P2,如果P2有使用super()来调用,那么就会以MRO的方式来搜索并继续往下调用,否则将停止调用
        pass


    def test_s():
        s = S()
        S.mro()


    if __name__ == '__main__':
        test_s()


    # 9、多继承多方法
    class MixSuperA(object):
        def m1(self):
            print("call mix super class A m1 method ...")


    class MixSuperB(object):
        def m2(self):
            print("call mix super class B m2 method ...")


    class SubClassA(MixSuperA):
        def m2(self):
            print("call sub class A m2 method ...")


    class SubClassD(MixSuperA, MixSuperB):
        def m1(self):
            print("call sub class D m1 method ...")
            super().m2()  # 以MRO的搜索方式遍历
            super().m1()  # 以MRO的搜索方式遍历


    if __name__ == '__main__':
        d = SubClassD()
        d.m1()

    # 10、super的参数约束
    class Person(object):
        def __init__(self, name, age):
            print("call person init ...")
            self.__name = name
            self.__age = age


    class Student(Person):
        def __init__(self, age):
            print("call Student init ...")
            super().__init__("keithl", age)  # 这里的super()使用MRO方式进行搜索，对应是Son,而Son只提供一个参数age的传递


    class Son(Person):
        def __init__(self, age):
            print("call son init ...")
            super().__init__("keithl", age)


    class Me(Student, Son):
        pass


    if __name__ == '__main__':
        Me(27)


    # 11、为避免复杂化,定义规范:在每一个被super调用的方法参数签名必须与基类的定义的方法一致
    class Person(object):
        def __init__(self, name, age):
            print("call person init ...")
            self.__name = name
            self.__age = age


    class Student(Person):
        def __init__(self, name, age):
            print("call Student init ...")
            super().__init__(name, age)


    class Son(Person):
        def __init__(self, name, age):
            print("call son init ...")
            super().__init__(name, age)


    class Me(Student, Son):
        pass


    if __name__ == '__main__':
        Me(27)

    # 12、为避免复杂化以及多继承中的方法混淆,最好是在MRO中最后一个调用的方法链中使用super()去覆盖基类的方法,其他的不要使用super()覆盖
    class Person(object):
        def __init__(self, name, age):
            print("call person init ...")
            self.__name = name
            self.__age = age


    class Student(Person):
        pass  # Student不做定义


    class Son(Person):
        def __init__(self, name, age):
            print("call son init ...")
            super().__init__(name, age)


    class Me(Student, Son):
        pass


    if __name__ == '__main__':
        Me(27)

    '''
    1、super()方法在py3.x中可用,py2.x是使用super关键字并传入父类名称和子类self对象
    2、super()调用方法将以MRO的搜索方式进行关系链的调用
    3、在子类中如果没有使用super()将停止关系链的调用
    4、在MRO最右边的顶层基类中不要声明super()语句调用
    5、混合方法使用super()仍然以上述规则来查询

    '''