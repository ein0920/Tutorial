
# 最简单的用法，next和for
if __name__ == '__main__':
    # yield生成器
    def simple_gen():
        yield 1
        yield 2
        yield 3
        yield 4

    def for_gen(n):
        for i in range(1, n):
            yield i**2

    a = for_gen(5)
    next(a)

    # ()的生成器
    b = (x**2 for x in range(1, 5))
    b.__next__()

    # for驱动生成器
    c = (x**2 for x in range(1, 5))
    for num in c:
        print(num)

    # sum也可以驱动
    d = (x**2 for x in range(1, 5))
    sum(d)


# send的用法，
if __name__ == '__main__':
    # 生成器的send用法 generator.send(value)
    def test():
        i = 1
        while i < 5:
            temp = yield i ** 2
            print(temp)
            i += 1

    t = test()

    # 第一次运行只能使用next或者send(None)
    t.send('good')  # 这样是报错的
    print(t.__next__())  # 预激
    # send的作用相当于使生成器继续运行，并且传递的参数为yield的返回值(程序中即temp的值)
    print(t.send("Hello World"))  # 先传给temp，在跑到下一个yield处
    print(t.__next__())  # 相当于send(None) 此时temp = None


# 生成全排列的list版和生成器版
if __name__ == '__main__3':

    def permutation(list1, n = None):
        if n is None:
            n = len(list1)

        if n == 1 and len(list1) >= 1:
            rst = []
            for item in list1:
                rst.append([item])
            return rst
        rst = []
        for i in range(len(list1)):
            v = [list1[i]]
            rest = list1[:i] + list1[i+1:]
            p = permutation(rest, n - 1)
            for subp in p:
                rst.append(v + subp)
        return rst

    permutation([1,2,3,4,5], 3)

    # 生成器版
    def permutation_gen(list1, n=None):
        if n is None:
            n = len(list1)
        if n == 1 and len(list1) >= 1:
            for item in list1:
                yield [item,]
        for i in range(len(list1)):
            v = [list1[i]]
            rest = list1[:i] + list1[i+1:]
            p_gen = permutation(rest, n-1)
            for subp in p_gen:
                yield v + subp

    for t in permutation_gen([1,2,3,4,5], 3):
        print(t)

    # 另外一个生成器版
    def perm(items, n=None):
        if n is None:
            n = len(items)
        for i in range(len(items)):
            v = items[i:i + 1]  # 使用字符串分片，取其中的元素
            if n == 1:  # 如果是第一次循环，则打印第一个字符和第二个字符
                yield v
            else:
                rest = items[:i] + items[i + 1:]  # i + 1表示接着上次运行的状态i的值进行切片，取后面的值字符
                for p in perm(rest, n - 1):  # 递归调用本生成器，进行循环，此就是之前描述的特定规则
                    yield v + p

    for t in perm([1,2,3,4,5], 3):
        print(t)


# 这个是改写fib的gen
if __name__ == '__main__':
    # 生成器版
    from collections import deque
    def fib_gen(n):
        for i in range(1, n + 1):
            if i == 1:
                yield 1
            elif i == 2:
                yield 1
            else:
                lastRst = fib_gen(i-1)
                lastTwo = deque(maxlen=2)
                for last in lastRst:
                    lastTwo.append(last)
                yield lastTwo[0] + lastTwo[1]

    for t in fib_gen(10):
        print(t)

    # list版
    def fib_list(n):
        # 初值
        if n ==1:
            return [1]  # 初值凑成输出的形式
        elif n == 2:
            return [1,1]  # 初值凑成输出的形式
        else:
            #
            rst = fib_list(n-1)  # 前一层递归的结果
            rst.append(rst[-1] + rst[-2])  # 用前一层递归的结果凑成输出的形式
            return rst
    fib_list(10)


# yield from 的例子
if __name__ == '__main__':
    '''
    第一个用途是替代for
    '''
    def chain(*iterables):
        for it in iterables:
            for i in it:
                yield i

    s = 'ABC'
    t = tuple(range(3))
    list(chain(s, t))

    def chain(*iterables):
        for i in iterables:
            yield from i

    list(chain(s, t))

    '''
    第二个用途是递归
    '''
    from collections import Iterable

    def flatten(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                yield from flatten(x)
            else:
                yield x

    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for x in flatten(items):
        print(x)

    # 如果不用yield from
    def flatten_2(items, ignore_types=(str, bytes)):
        for x in items:
            if isinstance(x, Iterable) and not isinstance(x, ignore_types):
                for i in flatten(x):  # 这个递归如果不是直接yield from flatten(x)，而是还有其他操作就不能用yield from了
                    yield i
            else:
                yield x

    #-----------------------------------------------
    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten_2(items):
        print(x)


    '''
    第三个用途就是
    yield from常用来代替内层for循环 与 打开双通道
    但是大部分情况下yield from并不单独使用，而是伴随着asyncio库使用，实现异步操作（一异步操作后面讲）
    从Python 3.5开始引入了新的语法 async 和 await ，而await替代的就是yield from（为了不与实现内层for循环的yield from误解）

    '''