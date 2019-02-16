
# -----------------------------dict的变体--------------------------------------------------------------------------------
# orderedDict
if __name__ == '__main__':
    '''普通dict的key上无序，orderedDict保持建立的顺序'''
    from collections import OrderedDict
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

    # 普通字典 @ todo
    d = {}

    d['bar'] = 2
    d['spam'] = 3
    d['foo'] = 1
    d['grok'] = 4

    for key in d:
        print(key, d[key])


# defaultDict
if __name__ == '__main__':
    '''
    最初使用字典的时候，只是简单实用dict()，但是如果键不存在，就会报错显示keyerror，
    此时可以考虑使用defaultdict()函数。
    '''
    from collections import defaultdict
    d = defaultdict(list)  # 没有指定value是默认是[]
    d['a'].append(1)  # 即使初始没有指定'a'作为key，初次赋值的时候也不会报错，默认已经指定了。
    d['a'].append(2)
    d['b'].append(4)
    d['a']
    d['c']

    d['d'] = 1  # 可以改数据类型
    d['e']  # 但是不能读取




# -----------------------------tuple的增强-------------------------------------------------------------------------------
# namedtuple
if __name__ == '__main__':
    '''
    namedtuple功能更加强大，你不必再通过索引值进行访问，你可以把它看做一个字典通过名字进行访问，只不过其中的值是不能改变的。
    1、Namedtuple比普通tuple具有更好的可读性，可以使代码更易于维护。
    2、同时与字典相比，又更加的轻量和高效。但是有一点需要注意，就是namedtuple中的属性都是不可变的。
    '''
    from collections import namedtuple

    Animal = namedtuple('Animal', 'name age type')  # 两个参数，分别是tuple的名字和其中域的名字，相当于建立一个Animal的简单类
    Animal.name
    perry = Animal(name='perry', age=31, type='cat')  # 将Animal实例化，需要三个
    perry.age
    perry.age = 32  # 不能修改property

    perry._asdict()

    # namedtuple看上去是创建了一个类，但是其实例可以用tuple的方法
    len(perry)
    a,b,c = perry

    # namedtuple的一个作用是tuple和元素解耦，如果从外部获得一个大元组并存到python的tuple，如果多了一列数据则容易出问题。例如
    from collections import namedtuple

    Stock = namedtuple('Stock', ['name', 'shares', 'price'])

    def compute_cost(records):
        total = 0.0
        for rec in records:
            s = Stock(*rec)
            total += s.shares * s.price
        return total

    # Some Data
    records = [
        ('GOOG', 100, 490.1),
        ('ACME', 100, 123.45),
        ('IBM', 50, 91.15)
    ]
    print(compute_cost(records))

    # namedtuple也可以当字典来用，而且更加节省空间，但是不可变，如果要改变，可以用_replace()方法生成一个新的实例
    from collections import namedtuple

    Stock = namedtuple('Stock', ['name', 'shares', 'price'])

    s = Stock('ACME', 100, 123.45)
    s = s._replace(shares=75)

