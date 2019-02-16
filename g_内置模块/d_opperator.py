
# itemgetter和attrgetter的用法
if __name__ == '__main__':
    """itemgetter，它构建的函数会返回提取的值构成的元组"""

    # 例子1
    from operator import itemgetter
    b = itemgetter(0, 2)  # 注意这里不是指从0到2的区间，而是指第0、2的数据
    a = [{1, 2}, 3, 4]
    b(a)  # 相当于(a[0], a[2])

    # 例子2
    data = [
        ('老王', 18, 175, 75),
        ('阿汤哥', 15, 165, 70),
        ('罗宾森', 23, 180, 100),
        ('小风', 10, 171, 60),
        ('黄佬', 20, 175, 65),
    ]

    get_c_d = itemgetter(2, 3)
    for value in data:
        print(get_c_d(value))

    """attrgetter，itemgetter相当于(a[0], a[2])，attrgetter相当于a.name，a.age"""
    from collections import namedtuple
    from operator import attrgetter

    size = namedtuple('size', 'height weight')
    stu = namedtuple('stu', 'name age size')
    data = [
        ('老王', 18, 175, 75),
        ('阿汤哥', 15, 165, 70),
        ('罗宾森', 23, 180, 100),
        ('小风', 10, 171, 60),
        ('黄佬', 20, 175, 65),
    ]
    data_stu = [stu(name, age, size(height, weight)) for name, age, height, weight in data]

    get_name_age = attrgetter('name', 'size.height')

    for value in sorted(data_stu, key=attrgetter('size.height')):
        print(get_name_age(value))


