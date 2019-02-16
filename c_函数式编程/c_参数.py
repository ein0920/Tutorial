
# 默认参数可变出错的情况1
if __name__ == '__main__':
    def spam(b=[]):
        return b

    a = spam()  # 先运行一次，
    print(a)
    a.append(1)
    a.append(2)
    b = spam()  # 第二次运行会受到第一次的影响
    print(b)  # Carefully observe result
    print('-' * 10)


# 默认参数可变出错的情况2
if __name__ == '__main__':
    def add_end(L=[]):
        L.append('END')
        return L

    # 正常调用时，不会有问题
    add_end([1, 2, 3])
    add_end(['x', 'y', 'z'])

    # 这时候出问题了
    add_end()
    add_end()
    '''
    Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
    因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
    如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
    '''