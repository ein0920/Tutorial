
# 类变量和实例变量
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
        arr = np.zeros((2,3),dtype=np.int8)

        def __init__(self, name):
            self.name = name  # name在类的构造函数中定义，是属于对象的变量
            self.count += 1 # 这个实际上是实例，相当于self.count = self.count + 1，左边是生成新的实例变量，右边是调用类变量
            self.lis[0] = 'ca' # 这个是调用类变量，没有生成新的实例变量
            self.arr[0][0] = 1 # 这个是调用类变量，没有生成新的实例变量

    Man.arr

    # 在生成实例之前已经存在类变量
    print(Man.gender)
    Man.lis
    Man.__dict__  # 进行对象管理的内置属性
    Man.name

    a = Man('jason')
    b = Man('tom')
    Man.name # 虽然实例属性有name，但是类属性还是没有
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
        _arr = np.zeros((3,5))

    class Child(Parent):

        def __init__(self):
            self._arr[0][0]=1

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


