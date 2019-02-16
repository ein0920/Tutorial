
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


# vars()
if __name__ == '__main__':
    # 返回类实例或者模块的属性
    class Info():
        def __init__(self, name, n):
            self.name = name
            self.n = n

    a = Info('Guido', 89)
    vars(a)


