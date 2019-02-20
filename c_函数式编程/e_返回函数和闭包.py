
# 这是一个返回函数的例子
if __name__ == '__main__':
    # 这是一个简单的求和函数
    def calc_sum(*args):
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    calc_sum(1,2,3)

    # 不需要立刻求和，返回一个求和的函数
    def lazy_sum(*args):
        def sum():
            ax = 0
            for n in args:
                ax = ax + n
            return ax

        return sum

    f = lazy_sum(1, 3, 5, 7, 9)  # 调用lazy_sum是返回内部的sum函数，生成f
    f()  # 调用f的时候才求和

    # 每次调用lazy_sum返回一个新的函数
    f1 = lazy_sum(1, 3, 5, 7, 9)
    f2 = lazy_sum(1, 3, 5, 7, 9)
    f1 == f2  # is False

    '''
    我们在函数lazy_sum中又定义了函数sum，
    并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
    这种称为“闭包（Closure）”的程序结构
    '''

# 闭包
if __name__ == '__main__':
    def count():
        fs = []
        for i in range(1, 4):
            def f():
                return i * i

            fs.append(f)
        return fs


    f1, f2, f3 = count()