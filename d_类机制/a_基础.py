
# 1、简单例子
if __name__ == '__main__':

    class Student(object):

        def __init__(self, name, score):
            self.name = name  # 属性，property，实例的属性
            self.score = score

        def print_score(self):  # 方法：method
            print('%s: %s' % (self.name, self.score))


    bart = Student('Bart Simpson', 59)  # bart的实例，instance，Student是类
    lisa = Student('Lisa Simpson', 87)
    bart.print_score()
    lisa.print_score()

    # 类和实例
    bart  # <__main__.Student at 0xbe7decd128> Student的一个实例
    Student  # __main__.Student __main__中一个类

    # 类中的方法，实例方法第一个参数永远的self，表明调用的时候针对实例化后的实例

    # 数据封装，OOP的一个特点就是将数据和相关的函数封装在一起，隐藏了内部的复杂逻辑，
    # 提供对外的功能，只把需要的内容（property）和功能（method）暴露畜类
    bart.name
    bart.score
    bart.print_score()

    # 在外部赋值，不太安全的一个行为，容易不小心破坏逻辑上的一致性
    bart.name = 'abc'


# 访问限制
if __name__ == '__main__':
    # 不让外部访问的内部方法的机制成为访问限制，复杂的逻辑需要用到很多不需要对外的变量
    # python没有确实的机制来限制访问

    # python使用命名规则来区分内部属性和方法，_internal
    class A:

        def __init__(self):
            self._internal = 0
            self.public = 1

    # __private_method这个是名称重整属性，会重整为_B__private_method，这样属性不能通过继承而覆盖
    class B:
        def __init__(self):
            self.__private = 0

        def __private_method(self):
            print('B.__private_method', self.__private)

        def public_method(self):
            self.__private_method()


    class C(B):
        def __init__(self):
            super().__init__()
            self.__private = 1  # Does not override B.__private

        # Does not override B.__private_method()
        def __private_method(self):
            print('C.__private_method')

    c = C()
    c.public_method()

    # lambda_这样的变量是为了区分关键字
    lambda_ = 1


# 继承
if __name__ == '__main__':
    class Animal(object):
        def run(self):
            print('Animal is running...')


    class Dog(Animal):

        def run(self):
            print('Dog is running...')


    class Cat(Animal):

        def run(self):
            print('Cat is running...')

    '''
    继承的作用
    1、相似的类可以复用代码，
    2、继承的第二个好处需要我们对代码做一点改进，可以覆盖父类的同名方法和属性
    '''


# 多态
if __name__ == '__main__':
    class Animal(object):
        def run(self):
            print('Animal is running...')


    class Dog(Animal):

        def run(self):
            print('Dog is running...')


    class Cat(Animal):

        def run(self):
            print('Cat is running...')


    a = list()  # a是list类型
    b = Animal()  # b是Animal类型
    c = Dog()  # c是Dog类型
    isinstance(a, list)
    isinstance(b, Animal)

    isinstance(c, Dog)
    isinstance(c, Animal)  # c既属于Dog，也属于Animal，这就是多态


# 获取对象的信息，type(), isinstance(), dir()
if __name__ == '__main__':
    # --------------------type()----------------------------------------------------------------------------------------
    type(123)
    type(abs)

    # --------------------isinstance()----------------------------------------------------------------------------------
    # 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

    # 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
    isinstance([1, 2, 3], (list, tuple))

    # --------------------dir()-----------------------------------------------------------------------------------------
    dir('ABC')

    # ---------------------getattr()、setattr()以及hasattr()-------------------------------------------------------------
    class MyObject(object):

        def __init__(self):
            self.x = 9

        def power(self):
            return self.x * self.x


    obj = MyObject()

    hasattr(obj, 'x')  # 有属性'x'吗？
    hasattr(obj, 'y')  # 有属性'y'吗？

    setattr(obj, 'y', 19)  # 设置一个属性'y'
    getattr(obj, 'y')  # 获取属性'y'
    '''
    这三个内置函数的其实是非常基础的函数，
    1、一个简单的用途就是可以用字符串'x'来访问和赋值 obj.x
    '''