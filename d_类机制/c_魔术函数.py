
# __new__和__init__的区别
if __name__ == '__main__':
    # -------------------------------------__init__---------------------------------------------------------------------
    # __new__是Python面向对象语言中一个很少用的函数，更多使用的是__init__这个函数。例如：
    class Dog(object):
        def __init__(self):
            '对象一创建完就会调用'
            print('对象初始化')

    dog1 = Dog()


    # -------------------------------------__new__----------------------------------------------------------------------
    '''
    根据官方文档：
        __init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
        __new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。
        
    也就是，__new__在__init__之前被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，
    然后__init__给这个实例设置一些参数。
    '''


    # 用汉字模拟通过系统的方式创建对象即默认的object类中_new_方法创建对象
    # class object:
    #     def __new__(cls, *args, **kwargs):
    #         print("创建对象")
    #         return "系统的方式创建的对象"  # 分配内存位置等底层操作

    class Dog(object):
        def __new__(cls, *args, **kwargs):  # __new__的语法
            # 创建对象时调用
            print('创建对象')
            # 返回默认的父类object通过_new__方法创建的对象,即通过系统的方式创建的对象
            return object.__new__(cls)  # 调用父类的__new__方法，并且返回

        def __init__(self):
            '对象一创建完就会调用'
            print('对象初始化')


    dog1 = Dog()
    print(dog1)


    class A(object):  # -> don t forget the object specified as base

        def __new__(cls):
            print("A.__new__ called")
            return super(A, cls).__new__(cls)  # 另一种调用父类的__new__方法，并且返回

        def __init__(self):
            print("A.__init__ called")

    a = A()

    # ------------------------------不按系统的方式来定义__new__
    class A(object):

        def __new__(cls):
            print("A.__new__ called")   # 因为不是按照系统的方式创建对象,所以就不会调用_init_方法，

        def __init__(self):
            print("A.__init__ called")  # -> is actually never called


    print(A()) #

    # ------------------------------__init__返回的时候：__init__不能返回任何东西
    class A(object):

        def __init__(self):
            print("A.__init__ called")
            return 33  # -> TypeError: __init__ should return None

    A()

    # __new__返回其他类
    class Sample(object):

        def __str__(self):
            return "SAMPLE"


    class A(object):

        def __new__(cls):
            return Sample()

    print(A())

    # 也可以写成
    class Sample(object):

        def __str__(self):
            return "SAMPLE"

    class A(object):
        def __new__(cls):
            return super(A, cls).__new__(Sample)


    print(A())

    '''
    总结：
    1、__new__方法是创建实例时调用的，形参是类参数cls
    2、需要返回，系统的方式是调用并返回父类object的__new__，非常规方式可以返回其他，此时不调用__init，__init__不能返回东西
    '''


# __len__ 要让 len() 函数工作正常，类必须提供一个特殊方法__len__()，它返回元素的个数。
if __name__ == '__main__':
    class Students(object):
        def __init__(self, *args):
            self.names = args

        def __len__(self):
            return len(self.names)


    s = Students(2,3,4)
    len(s)

    #
    class Test_len(object):

        def __init__(self):
            print('没什么事发生！')

        def __len__(self):
            return 12  # len()的时候就调用这个返回

    len(Test_len())


# __next__方法和__iter__方法
if __name__ == '__main__':
    # 使用next函数必须要有__next__方法，但是只有__next__方法不能直接支撑for
    class test():
        def __init__(self, data=1):
            self.data = data

        def __next__(self):
            if self.data > 5:
                raise StopIteration
            else:
                self.data += 1
                return self.data

    c = test()
    next(c)  # 其实就是调用一次__next__
    c.data

    # 这是不能直接使用的
    for cc in c:
        print(cc.__next__())

    for i in range(3):
        print(c.__next__())


    # for需要__iter__的支持，而在__iter__内部需要返回一个有__next__方法的对象
    class test_for():
        def __init__(self, data=1):
            self.data = data

        def __iter__(self):
            return self  # self其实就实例化的test_for对象，除了__iter__外的属性和方法都有

        def __next__(self):
            if self.data > 5:
                raise StopIteration
            else:
                self.data += 1
                return self.data


    for item in test_for(3):
        print(item)


# __getitem__方法；使用[]必须的和__missing__
if __name__ == '__main__':
    # 如果在类中定义了__getitem__()方法，那么他的实例对象（假设为P）就可以这样P[key]取值。
    # 当实例对象做P[key]运算时，就会调用类中的__getitem__()方法。
    class DataTest:

        def __init__(self, id, address):
            self.id = id
            self.address = address
            self.d = {self.id:5, self.address: "192.168.1.1"}

        def __getitem__(self, key):
            return self.d[key]

    data = DataTest(1, "192.168.2.11")
    print(data[1])


    # 可以看出当使用__getitem__来访问一个不存在的key的时候，会调用__miss__()方法

    class safesub(dict):
        def __missing__(self, key):
            return '{%s}' % key

    d = safesub({'a': 3})
    d['a']
    d[8]


# __iter__ 如果一个类要可以用for，必须有__iter__方法，而且需要在在__iter__中返回可迭代对象
if __name__ == '__main__':
    class Node:
        def __init__(self, value):
            self._value = value
            self._children = []

        def __repr__(self):
            return 'Node({!r})'.format(self._value)

        def add_child(self, node):
            self._children.append(node)

        def __iter__(self):  # 要可以对实例使用for，就有有这个
            return iter(self._children)

    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

    #


# __repr__是运行的使用调用，__str__是print的时候调用
if __name__ == '__main__':
    class Pair:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return 'Pair({0.x!r}, {0.y!r})'.format(self)  # 注意这里0是位置

        def __str__(self):
            return '({0.x!s}, {0.y!s})'.format(self)

    p = Pair(3,4)
    p
    print(p)

    # 其中!r的作用如下，!r是使用__repr__输出
    p = Pair(3,4)
    print('p is {0!r}'.format(p))
    print('p is {0}'.format(p))