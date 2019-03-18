
# map
if __name__ == '__main__':
    # map(function, iterable, …) 对iterable的元素使用函数处理，并返回结果
    def square(x):  # 计算平方数
        return x ** 2

    map(square, [1, 2, 3, 4, 5])


# ord
if __name__ == '__main__':
    ord('a')  # 返回字符对应的十进制码
    ord('\t')


# vars() 返回类实例或者模块的属性
if __name__ == '__main__':
    # 返回类实例或者模块的属性
    class Info():
        def __init__(self, name, n):
            self.name = name
            self.n = n

    a = Info('Guido', 89)
    vars(a)

# getattr
if __name__ == '__main__':
    class A(object):
        bar = 1

    a = A()

    a.bar
    d = getattr(a, 'bar')  # 获取属性 bar 值，相当于a.bar
    getattr(a, 'bar2')  # 属性 bar2 不存在，触发异常

# hasattr
if __name__ == '__main__':
    class test():
        name = "xiaohua"

    def run(self):

        return "HelloWord"

    t = test()
    hasattr(t, "name")  # 判断对象有name属性
    hasattr(t, "run")  # 判断对象有run方法

# setattr
if __name__ == '__main__':
    class test():
        ...
        name = "xiaohua"

    def run(self):
        ...
        return "HelloWord"

    t = test()
    hasattr(t, "age")  # 判断属性是否存在
    setattr(t, "age", "18")  # 为属相赋值，并没有返回值
    hasattr(t, "age")  # 属性存在了
