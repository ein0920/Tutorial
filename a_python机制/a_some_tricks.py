
# *的例子
if __name__ == '__main__':
    # 1、函数定义中，函数使用的
    def func1(*args):
        print(args)

    func1(1,2,3)

    def func2(*args):
        print(*args)

    func2(1,2,3)

    # 函数使用的
    row = ('ACME', 50, 91.5)
    print(*row, sep=',')

    # 拆包
    record = (1,2,3,4,5,6,7)
    _, *middle, _ = record # 拆成list