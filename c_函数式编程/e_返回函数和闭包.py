
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
    
    1、函数可以认为是一个标识符，调用的时候就去运行指定的代码。
    2、如果函数内部又有函数，如果不是返回内部函数的情况下，那么就是为了提高代码复用而做的内部函数。
    3、单外部函数的返回值是内部函数的函数名时，这就是“闭包”。
    '''

# 闭包
if __name__ == '__main__':
    def ExFunc(n):
        _sum = n

        def InsFunc(m):
            return _sum + m

        return InsFunc


    # 不能在函数外部调用内部的函数和变量
    a = InsFunc()
    _sum

    myFunc = ExFunc(10)
    myFunc(2)  #

    myAnotherFunc = ExFunc(20)
    myAnotherFunc()

    myFunc()

    myAnotherFunc()

    '''
    闭包 = 函数块+定义函数时的环境
    在上述例子中，函数块就是InsFunc，环境就是sum
    '''

    # ---------------------------------闭包的注意事项--------------------------------------------------------------------
    # 闭包不能修改外部作用域的变量
    def ExFunc_2(n):
        _sum = n

        def InsFunc_2():
            _sum += 1
            return _sum

        return InsFunc_2

    myFunc_2 = ExFunc_2(3)
    myFunc_2()

    # 需要申明nonlocal，这个就做成一个计数器
    def ExFunc_2(n):
        _sum = n

        def InsFunc_2():
            nonlocal _sum
            _sum += 1
            return _sum

        return InsFunc_2

    myFunc_2 = ExFunc_2(3)
    myFunc_2()

    # --------------------------闭包的常见错误（廖雪峰的例子）-------------------------------
    def count():
        fs = []
        for i in range(1, 4):
            def f():
                return i * i

            fs.append(f)
        return fs

    f1, f2, f3 = count()  # 结果是9，9，9。期待的结果是1，4，9
    '''
    上面例子的问题在于f1, f2, f3作为闭包函数，其他调用变量i是在调用的时候在去找外部环境的i，所以
    '''

    # 解决的办法是
    def count():
        def f(j):
            def g():
                return j * j

            return g

        fs = []
        for i in range(1, 4):
            fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
        return fs


# 闭包的应用范例————1、当闭包执行完后，仍然能够保持住当前的运行环境。
if __name__ == '__main__':
    def create():
        pos = [0,0]
        def player(direction, step):
            # 这里应该首先判断参数direction,step的合法性，比如direction不能斜着走，step不能为负等
            # 然后还要对新生成的x，y坐标的合法性进行判断处理，这里主要是想介绍闭包，就不详细写了。
            new_x = pos[0] + direction[0] * step
            new_y = pos[1] + direction[1] * step
            pos[0] = new_x
            pos[1] = new_y
            # 注意！此处不能写成 pos = [new_x, new_y]，原因在上文有说过
            return pos

        return player

    # 用函数实现了类的功能
    player = create()  # 创建棋子player，起点为原点
    print(player([1, 0], 10))  # 向x轴正方向移动10步
    print(player([0, 1], 20))  # 向y轴正方向移动20步
    print(player([-1, 0], 10))  # 向x轴负方向移动10步

    '''
    每次运行完的内部函数，外部的环境还保留着，所以称为闭包
    '''

'''
用途2————闭包可以根据外部作用域的局部变量来得到不同的结果，
这有点像一种类似配置功能的作用，我们可以修改外部的变量，闭包根据这个变量展现出不同的功能。
比如有时我们需要对某些文件的特殊行进行分析，先要提取出这些特殊行。
这个有点像partial()的作用
'''