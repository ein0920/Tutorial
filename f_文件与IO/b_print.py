
if __name__ == '__main__':
    with open('f_文件与IO/somefile.txt', 'wt') as f:
        print('Hello, world!', file=f)  # 将print的内容输出到txt文件中

if __name__ == '__main__':
    print('ACME', 50, 91.5)
    print('ACME', 50, 91.5, sep=',')
    print('ACME', 50, 91.5, sep=' ', end='!!\n')

    for i in range(5):
        print(i, end=' ')

    row = ('ACME', 50, 91.5)
    print(*row, sep=',')