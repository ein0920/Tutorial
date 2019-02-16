'''
itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是迭代对象，只有用for循环迭代的时候才真正计算。
'''
# groupby
if __name__ == '__main__':
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]

    from itertools import groupby

    rows.sort(key=lambda r: r['date'])
    for date, items in groupby(rows, key=lambda r: r['date']):
        print(date)
        for i in items:
            print('    ', i)

    # 相当于[(name1, group1), (name2, group2), (name2, group2), ...]
    # group1是一个list，list里面将原来的rows的元素分到里面

    grouped = groupby(rows, key=lambda r: r['date'])
    dir(grouped)
    # 没有其他方法了


# compress
if __name__ == '__main__':
    '''compress也是返回迭代器，第一个上目标序列，第二个上筛选序列，返回筛选器中True对应的元素的序列'''
    # 例子1，用TF来做筛选器
    addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK',
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
    counts = [0, 3, 10, 4, 1, 7, 6, 1]

    from itertools import compress

    more5 = [n > 5 for n in counts]
    a = list(compress(addresses, more5)) # addresses是目标列表，more5是布尔列表，一样长，将more5中的True对应多拿下来
    print(a)

    # 例子2，用1,0来做筛选器
    for i in compress("abcdef", [1, 1, 0, 1, 0, 1]):  # a, b, d, f
        print(i)


# 无限循环器count和cycle和repeat
if __name__ == '__main__':
    # count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl + C退出。
    import itertools
    natuals = itertools.count(1)
    for n in natuals:
        print(n)

    # cycle()会把传入的一个序列无限重复下去：
    import itertools
    cs = itertools.cycle('ABC')  # 注意字符串也是序列的一种
    for c in cs:
        print(c)

    # repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
    ns = itertools.repeat('A', 10)
    for n in ns:
        print(n)
    # 打印10次'A'


# chain()
if __name__ == '__main__':
    # chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
    for c in itertools.chain('ABC', 'XYZ'):
        print(c)


# dropwhile
if __name__ == '__main__':
    from itertools import dropwhile

    with open('g_内置模块/somefile.txt') as f:
        for line in dropwhile(lambda line: line.startswith('h'), f):
            print(line, end='')


# islice
if __name__ == '__main__':
    # 对迭代器做切片处理
    def count(n):  # 这个一个无限的迭代器，没有固定长度
        while True:
            yield n
            n += 1


    c = count(0)
    c[10:20]

    # 用islice
    import itertools

    for x in itertools.islice(c, 10, 20):
        print(x)

# 迭代所有可能的组合或者排列，permutations，combinations，combinations_with_replacement
if __name__ == '__main__':
    # 返回所有排列
    items = ['a', 'b', 'c']
    from itertools import permutations

    for p in permutations(items):  # 接受一个元素集合，重排为所有可能的排列，返回元组的形式
        print(p)

    for p in permutations(items, 2):  # 较短的长度
        print(p)

    # 返回所有组合
    items = ['a', 'b', 'c']
    from itertools import combinations

    for p in combinations(items, 3):  # 接受一个元素集合，重排为所有可能的排列，返回元组的形式
        print(p)

    for p in combinations(items, 2):  # 较短的长度
        print(p)

    # 可以重复的组合
    items = ['a', 'b', 'c']
    from itertools import combinations_with_replacement

    for c in combinations_with_replacement(items, 3):
        print(c)