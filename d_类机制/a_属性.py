'''
属性包括变量和方法
'''

# 类变量和实例实例变量
if __name__ == '__main__':
    import numpy as np


    class Man(object):
        # 直接定义的类的变量，属于类。
        # 类变量实在定义类的时候生成的
        # 其中 gender, avg_height为基本数据类型，immutable
        # lis为列表类型，为mutable的
        gender = 'male'
        avg_height = 1.75
        count = 1
        lis = ['hello', 'world']
        arr = np.zeros((2, 3), dtype=np.int8)

        def __init__(self, name):
            self.name = name  # name在类的构造函数中定义，是属于对象的变量
            self.count += 1  # 这个实际上是实例，相当于self.count = self.count + 1，左边是生成新的实例变量，右边是调用类变量
            self.lis[0] = 'ca'  # 这个是调用类变量，没有生成新的实例变量
            self.arr[0][0] = 1  # 这个是调用类变量，没有生成新的实例变量


    Man.arr

    # 在生成实例之前已经存在类变量
    print(Man.gender)
    Man.lis
    Man.__dict__  # 进行对象管理的内置属性
    Man.name

    a = Man('jason')
    b = Man('tom')
    Man.name  # 虽然实例属性有name，但是类属性还是没有
    Man.arr

    # 通过一个对象a访问一个变量x，变量的查找过程是这样的：
    # 先在对象自身的__dict__中查找是否有x，如果有则返回，否则进入对象a所属的类A的__dict__中进行查找

    # 对象a试图修改一个属于类的 immutable的变量，则python会在内存中为对象a新建一个gender变量，此时a就具有了属于自己的gender变量
    a.gender = 'female'
    a.__dict__

    # 对象b试图修改一个mutable的变量，则python找到类Man的__dict__中的变量lis，
    # 由于lis是可以修改的，因此直接进行修改，而不会给b新生成一个变量。类Man以及类Man
    # 的所有对象都公用这一个lis
    b.lis = ['fuck', 'world']

    a.__dict__  # 属于a的变量，有 name， gender
    b.__dict__  # 属于b的变量，只有name
    Man.__dict__  # 属于类Man的变量，有 gender，avg_height，lis，但是不包括 name
    # name是属于对象的变量

    Man.t = 'test'  # 此时Man的变量又多了t，但是对象a和b中没有变量t。
    # （这里可以看出，对象的变量和类的变量是分开的）

    a.gender  # female
    b.gender  # male

    a.lis  # ['fuck', 'world']
    b.lis  # ['fuck', 'world']

    a.addr = '182.109.23.1'  # 给对象a定义一个变量，对象b和类Man中都不会出现（解释性语言好随性。。）

    '''
    总结：
    1、实例属性在实例的__dict__，在实例的方法中调用属性是优先在实例的__dict__中找，找不到才到类的__dict__中找。
    2、在实例中如果生成一个和类属性同名的属性时，并不是覆盖，实际上是变量空间的同名属性，分属于实例和类。
    3、类属性在类定义的时候已经生成，独立于实例。
    '''


    # ------------------------------------------类属性的访问-------------------------------------------------------------
    # 1、类方法可以通过绑定的cls形参来访问

    # 实例方法可以通过类名来访问和改写
    class Stu1(object):
        _num = 0

        def __init__(self):
            Stu1._num += 1
            print('Another')


    a = Stu1()
    Stu1._num


    # 可以通过self来访问类属性，但是不能修改
    class Stu2(object):
        _num = 0

        def __init__(self):
            self._num += 1
            print(Stu2._num)


    a = Stu2()
    a._num


    # -------------------------------------实例方法访问父类的类属性--------------------------------------------------------
    class Class3(object):
        _num = 0


    class Stu3(Class3):

        def __init__(self):
            Class3._num += 1


    a = Stu3()
    Class3._num

    # 实例方法修改父类的类属性（利用List的bug）
    import numpy as np


    class Parent(object):
        _arr = np.zeros((3, 5))


    class Child(Parent):

        def __init__(self):
            self._arr[0][0] = 1


    a = Child()
    Parent._arr

    a.__dict__


    #
    class B(object):
        a = 0

        def get_workflow(self):
            print('class B a', self.a)
            return self.a


    class A(B):
        a = 1

        def get_workflow(self):
            # B.a = 2
            b = super(A, self).get_workflow()
            print('class A a', b)


    a_obj = A()
    a_obj.get_workflow()
    b_obj = B()
    b_obj.a

    '''
    总结：
    1、实例方法修改类属性的都是生成对应域的实例属性，
    2、在实例方法中修改类属性只有用类名来引用，指定作用域
    3、在类方法中修改也可以
    '''


# 实例方法，类方法、静态方法
if __name__ == '__main__':
    '''
    首先，这三种方法都定义在类中。下面先简单说一下怎么定义和调用的。（PS：实例对象的权限最大。）
    实例方法
        定义：第一个参数必须是实例对象，该参数名一般约定为“self”，通过它来传递实例的属性和方法（也可以传类的属性和方法）；
        调用：只能由实例对象调用。

    类方法
        定义：使用装饰器 @ classmethod。第一个参数必须是当前类对象，该参数名一般约定为“cls”，通过它来传递类的属性和方法（不能传实例的属性和方法）；
        调用：实例对象和类对象都可以调用。

    静态方法
        定义：使用装饰器 @ staticmethod。参数随意，没有“self”和“cls”参数，但是方法体中不能使用类或实例的任何属性和方法；
        调用：实例对象和类对象都可以调用。
    '''

    # ------------------------------------------类方法的应用场景----------------------------------------------------------
    '''
    假设我有一个学生类和一个班级类，想要实现的功能为：
    1、执行班级人数增加的操作、获得班级的总人数；
    2、学生类继承自班级类，每实例化一个学生，班级人数都能增加；
    3、最后，我想定义一些学生，获得班级中的总人数。

    思考：这个问题用类方法做比较合适，为什么？
    因为我实例化的是学生，但是如果我从学生这一个实例中获得班级总人数，在逻辑上显然是不合理的。
    同时，如果想要获得班级总人数，如果生成一个班级的实例也是没有必要的。
    '''


    class ClassTest(object):
        __num = 0

        @classmethod
        def addNum(cls):
            cls.__num += 1

        @classmethod
        def getNum(cls):
            return cls.__num

        # 这里我用到魔术函数__new__，主要是为了在创建实例的时候调用人数累加的函数。
        def __new__(cls):
            ClassTest.addNum()  # 调用类方法要用类名
            return super(ClassTest, cls).__new__(cls)


    class Student(ClassTest):
        def __init__(self):
            self.name = ''


    a = Student()
    b = Student()
    print(ClassTest.getNum())

    # ------------------------------------------静态方法的应用场景--------------------------------------------------------
    '''
    静态方法是类中的函数，不需要实例。
    静态方法主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，不会涉及到类中的属性和方法的操作。
    可以理解为，静态方法是个独立的、单纯的函数，它仅仅托管于某个类的名称空间中，便于使用和维护。
    '''
    import time


    class TimeTest(object):
        def __init__(self, hour, minute, second):
            self.hour = hour
            self.minute = minute
            self.second = second

        @staticmethod
        def showTime():
            return time.strftime("%H:%M:%S", time.localtime())


    print(TimeTest.showTime())
    t = TimeTest(2, 10, 10)
    nowTime = t.showTime()
    print(nowTime)


# python的隐藏设计
if __name__ == '__main__':
    # 实例的隐藏东西
    if __name__ == '__main__':

        class T(object):
            name = 'name'  # 类变量

            def hello(self):  # 实例方法
                print('hello')

        t = T()
        dir(t)
        '''
        ['__class__', '__delattr__', '__dict__', '__doc__', '__getattribute__',
         '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__',  
         '__repr__', '__setattr__', '__str__', '__weakref__', 'hello', 'name']  
        '''

        # 属性可以分为两类，一类是Python自动产生的，如__class__，__hash__等
        # 内置变量
        t.__class__
        t.__dict__  # 存放实例的自定义的属性，不包括类变量和方法。t.hello()不在里面
        t.__doc__
        t.__module__
        t.__weakref__

        # 魔术方法
        t.__new__()
        t.__init__()

        t.__hash__()

        t.__reduce__()
        t.__reduce_ex__()

        t.__setattr__('dir', 2)
        t.__delattr__('dir')

        t.__getattribute__()

        t.__str__()
        t.__repr__()

    # 类的隐藏东西
    if __name__ == '__main__':
        class T(object):
            name = 'name'  # 类属性

            def hello(self):  # 实例方法
                print('hello')

        # 类是type的实例，也有__dict__，包含下面的东西
        T.__dict__
        '''
        mappingproxy({'__dict__': <attribute '__dict__' of 'T' objects>,
              '__doc__': None,
              '__module__': '__main__',
              '__weakref__': <attribute '__weakref__' of 'T' objects>,
              'hello': <function __main__.T.hello>,
              'name': 'name'})
        '''
        # 有些内建类型，如list和string，它们没有__dict__属性，随意没办法在它们上面附加自定义属性。

        '''
        t的属性的搜索顺序，
        1、是否是个自动产生的属性（魔术属性）；
        2、如果是自定义的，在t的__dict__中寻找；
        3、T.__dict__中找；
        4、T的父类(如果T有父类的话)的__dict__中继续查找
        '''

        # --------------------------------------------------------------------------------------------------------------
        # 对于name来说，下面是一样的
        T.name
        T.__dict__['name']
        # 对于hello来说，也是一致
        T.hello
        T.__dict__['hello']

# 属性检查的几个方式————1、set和get（比较low的方法）
if __name__ == '__main__':
    # 如何对属性进行校验呢 比如有个要保证 age 属性 它只能是int类型且大小处于0到100之间？
    class Student:
        def __init__(self):
            pass

        def get(self):
            return self.age

        def set(self, age):
            if isinstance(age, int) and 0 < age < 100:
                self.age = age
            else:
                print("请输入合法的年龄")


    stu = Student()

    stu.set(110)  # 请输入合法的年龄

    stu.set(10)

    print(stu.get())  # 10


# 属性检查的几个方式————2、@property装饰
if __name__ == '__main__':
    class Student:
        def __init__(self):
            pass

        @property
        def age(self):
            return self.value

        @age.setter
        def age(self, value):
            if isinstance(value, int) and 0 < value < 100:
                self.value = value
            else:
                print("请输入合法的年龄")


    stu = Student()

    stu.age = 10
    print(stu.age)  # 10


# 属性检查的几个方式————3、属性描述符__set__, __get__, __delete__（类似的属性有几十个，不可能每个都定义一个@property）
if __name__ == '__main__':
    class Int_validation:
        def __get__(self, instance, owner):  # 两个参数，instance和cls（owner）
            return self.value

        def __set__(self, instance, value):  # 两个参数，instance和value
            if isinstance(value, int) and 0 < value < 100:
                self.value = value  # 这个要注意 要用value，不能用instance 否则会陷入死循环
            else:
                print("请输入合法的数字")

        def __delete__(self, instance):
            pass


    class Student:
        age = Int_validation()  # 使用的时候就是在类变量中实例化


    stu = Student()  # 再实例化，
    stu.age = 50  # 实际上是调用Student.age.__set__
    Student.age
    print(stu.age)


# descriptor的第二种用途，用instance.__dict__来调用
if __name__ == '__main__':
    # 在类变量中用
    class Integer:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, int):
                raise TypeError('Expected an int')
            instance.__dict__[self.name] = value

        def __delete__(self, instance):
            del instance.__dict__[self.name]


    class Point:
        x = Integer('x')  # 放到类变量中使用
        y = Integer('y')

        def __init__(self, x, y):
            self.x = x  # 再成为实例变量
            self.y = y


    if __name__ == '__main__':
        p = Point(2, 3)  # 实例化Point
        print(p.x)  # 实际上调用的是Point.x.__get__(p, Point)
        Point.x  # 实际上调用的是Point.x.__get__(None, Point)
        p.y = 5
        try:
            p.x = 2.3
        except TypeError as e:
            print(e)


# 第三个__set__的例子：修改父类中的property
if __name__ == '__main__':
    # Example of managed attributes via properties

    class String:
        def __init__(self, name):
            self.name = name

        def __get__(self, instance, cls):
            if instance is None:
                return self
            return instance.__dict__[self.name]

        def __set__(self, instance, value):
            if not isinstance(value, str):
                raise TypeError('Expected a string')
            instance.__dict__[self.name] = value


    class Person:
        name = String('name')

        def __init__(self, name):
            self.name = name


    class SubPerson(Person):
        @property
        def name(self):
            print('Getting name')
            return super().name

        @name.setter
        def name(self, value):
            print('Setting name to', value)
            super(SubPerson, SubPerson).name.__set__(self, value)

        @name.deleter
        def name(self):
            print('Deleting name')
            super(SubPerson, SubPerson).name.__delete__(self)


    if __name__ == '__main__':
        a = Person('Guido')
        print(a.name)
        a.name = 'Dave'
        print(a.name)
        try:
            a.name = 42
        except TypeError as e:
            print(e)


# descriptor的第四种用法，惰性属性
if __name__ == '__main__':
    # 使用描述符来实现，有点装饰器的意味
    class lazyproperty:
        def __init__(self, func):
            self.func = func

        def __get__(self, instance, cls):
            if instance is None:
                return self
            else:
                value = self.func(instance)
                setattr(instance, self.func.__name__, value)
                return value


    if __name__ == '__main__':
        import math


        class Circle:
            def __init__(self, radius):
                self.radius = radius

            @lazyproperty
            def area(self):
                print('Computing area')
                return math.pi * self.radius ** 2

            @lazyproperty
            def perimeter(self):
                print('Computing perimeter')
                return 2 * math.pi * self.radius


        c = Circle(4.0)  # 此时没有计算
        c.radius
        c.area  # 此时计算
        c.perimeter  # 此时也进行了计算
        c.perimeter  # 再次调用就没有计算了
