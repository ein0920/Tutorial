# --------------------------------------list----------------------------------------------------------------------------
# list的元素操作
if __name__ == '__main__':
    # 生成一个list
    a_list = [2, 3, 7, None]
    tup = ('foo', 'bar', 'baz')
    b_list = list(tup)

    # 1、元素操作
    b_list.append('dwarf')  # append只能append元素，不能append list。两个list用extend
    b_list.insert(1, 'red')  # insert比append耗费时间，
    foo = b_list.pop(2)  # 按照位置来删去，并且返回给foo
    b_list.append('foo')
    b_list.remove('foo')  # 按照元素来删去

    # 元素是否在list中
    'dwarf' in b_list


# list的list间操作
if __name__ == '__main__':
    foo = [4, None, 'foo'] + [7, 8, (2, 3)]  # 比较耗费资源
    x = [4, None, 'foo']
    x.extend([7, 8, (2, 3)])  # 比较节省资源


# 排序
if __name__ == '__main__':
    # sort有三个参数cmp(func)，key(func)，reverse(TF)
    a = [7, 2, 5, 1, 3]
    a.sort() # 修改了自身

    # 1key
    b = ['saw', 'small', 'He', 'foxes', 'six']
    b.sort(key=len)  # 按照长度来排序，key只能接受输入一个参数的函数

    # 2 cmp
    # 下面是自定义函数来排序，自定义函数的格式
    def cmp_ignore_case(s1, s2):
        u1 = s1.upper()
        u2 = s2.upper()
        if u1 < u2:
            return -1  # 前面小，返回-1
        if u1 > u2:
            return 1  # 前面大，返回1
        return 0

    sorted(b, cmp_ignore_case) # @todo python 3.6不适用

    c = b.sort(cmp_ignore_case)


# 4、有序插入，按照顺序插入
if __name__ == '__main__':

    import bisect
    c = [1, 2, 2, 2, 3, 4, 7]
    bisect.bisect(c, 2)  # 需要插入的位置
    bisect.bisect(c, 5)

    bisect.insort(c, 6)  # 按照该位置插入后的结果。替换掉c


# 选取，切片，查找元素位置
if __name__ == '__main__':
    seq = [7, 2, 3, 7, 5, 6, 0, 1]
    seq[1:5]
    # 还可以赋值
    seq[3:4] = [6, 3]
    # 首尾可以去掉
    seq[:5]
    seq[3:]
    seq[-4:]
    # 还可以设定步长
    seq[::2]

    # index方法，输入值返回位置首次出现的位置
    seq.index(2)


# 相关的内置函数-zip和reversed
if __name__ == '__main__':
    seq1 = ['foo', 'bar', 'baz']
    seq2 = ['one', 'two', 'three']
    zip(seq1, seq2)
    # 拆对子，unzip
    pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'),
                ('Schilling', 'Curt')]
    first_names, last_names = zip(*pitchers)
    first_names
    last_names

    # 4、reversed
    list(reversed(range(10)))


# tuple一些用法
if __name__ == '__main__':
    # 1、创建
    tup = 4, 5, 6
    tuple([4, 0, 2])
    tup = tuple('string')

    # 2、连接，不能append，因为是定长的
    (4, None, 'foo') + (6, 0) + ('bar',)

    # 3、*乘法 # 和list一样，增殖而不知点乘
    ('foo', 'bar') * 4

    # 4、拆包（相当于取值，只是简单一点，跟函数返回多个变量一样）
    tup = (4, 5, 6)
    a, b, c = tup

    # 5、其他方法
    # 5.1 count
    a = (1, 2, 2, 2, 3, 4, 2)
    a.count(2)  # 数一下有多少个2

    # 5.2 输入值查找位置
    a.index(2)


# dict的简单操作
if __name__ == '__main__':
    # 1、生成
    # key是无序的唯一的
    empty_dict = {}
    d1 = {'a': 'some value', 'b': [1, 2, 3, 4]}
    mapping = dict(zip(range(5), reversed(range(5))))  # 用dict(zip来创建，用对子开生成
    d1.items()  # 拆成对子

    # key只能是hashable的对象，不能是变量名
    {a:2,b:2}  #是不行的
    a = 1; b=4
    {a: 2, b: 2}  # 就可以了



    # 2、元素操作
    d1[7] = 'an integer'  # 插入
    d1['b']  # 访问
    'b' in d1  # 只看是不是在key里面
    d1.has_key('c')  # 是否有c这个key

    d1[5] = 'some value'
    d1['dummy'] = 'another value'
    del d1[5]  # del关键字需要输入key
    ret = d1.pop('dummy')  # pop方法需要输入key

    d1.keys()
    d1.values()  # 返回list，两个顺序相同

    # 3、dict间操作
    d1.update({'b': 'foo', 'c': 12})  # 同key更新，不存在则插入


# dict的默认值get方法，default
if __name__ == '__main__':
    # 就是输入一个值，如果存在于key中就返回value，如果不存在则返回default，不更新如原来的dict
    d1.get(5, 'non-exist')

    # 一个归类的模块，如果word[0]在key中则append到values里面，如果不在则生成一个新的key
    words = ['apple', 'bat', 'bar', 'atom', 'book']
    from collections import defaultdict

    by_letter = defaultdict(list)
    for word in words:
        by_letter[word[0]].append(word)

    # 或者使用setdefault方法，如果不存在该key的话则新开一个key，并且将value设为[]。
    # append是另外一个方法，
    by_letter = {}
    for word in words:
        letter = word[0]
        by_letter.setdefault(letter, []).append(word)


# hash，clear，copy，iterkeys
if __name__ == '__main__':
    words = ['apple', 'bat', 'bar', 'atom', 'book']
    from collections import defaultdict

    by_letter = defaultdict(list)
    # 5、key必须是不变对象（可哈希）
    hash((1, 2, [2, 3]))  # 含有不可哈希的元素

    # 6、clear，清空自身
    by_letter.clear()

    # 7、复制自身
    by_letter.copy()

# -------------------------------推导式和生成器----------------------------------------------------------------------------------
if __name__ == '__main__':
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]

    # All positive values
    pos = [n for n in mylist if n > 0]

    # 生成器
    nums = [1,2,3,4,5]
    s = sum(x*x for x in nums)